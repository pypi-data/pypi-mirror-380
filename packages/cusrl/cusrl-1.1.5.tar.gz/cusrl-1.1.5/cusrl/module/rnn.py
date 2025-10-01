from typing import TypeAlias, cast

import torch
from torch import Tensor, nn

from cusrl.module.module import Module, ModuleFactory
from cusrl.utils.nest import map_nested
from cusrl.utils.recurrent import compute_sequence_lengths, split_and_pad_sequences, unpad_and_merge_sequences
from cusrl.utils.typing import Memory

__all__ = ["Gru", "Lstm", "Rnn", "concat_memory", "scatter_memory", "gather_memory"]


class RnnBase(nn.Module):
    def __init__(self, input_size: int, hidden_size: int):
        super().__init__()
        self.input_size: int = input_size
        self.hidden_size: int = hidden_size

    def forward(self, input: Tensor, memory: Memory = None) -> tuple[Tensor, Memory]:
        raise NotImplementedError


RnnLike: TypeAlias = nn.RNNBase | RnnBase


class RnnFactory(ModuleFactory["Rnn"]):
    def __init__(self, module_cls: str | type[RnnLike], **kwargs):
        self.module_cls: str | type[RnnLike] = module_cls
        self.kwargs = kwargs

    def __call__(self, input_dim: int, output_dim: int | None = None):
        # RNN / LSTM / GRU
        module_cls = getattr(nn, self.module_cls) if isinstance(self.module_cls, str) else self.module_cls
        return Rnn(module_cls, input_size=input_dim, output_dim=output_dim, **self.kwargs)

    def __getattr__(self, item):
        if item in (kwargs := super().__getattribute__("kwargs")):
            return kwargs[item]
        raise AttributeError(f"Object '{type(self).__name__}' has no attribute '{item}'.")

    def to_dict(self):
        return {"module_cls": self.module_cls, **self.kwargs}


class Rnn(Module):
    """A generic wrapper for recurrent neural networks (RNNs).

    This module provides a unified interface for various RNN-like layers (e.g.,
    `nn.RNN`, `nn.LSTM`, `nn.GRU`), handling different input scenarios such as
    single tensors, sequences with termination signals, and packed sequences.

    It automatically handles memory (hidden state) management, including
    resetting states for new episodes within a batch.

    Args:
        rnn (type[RnnLike] | RnnLike):
            The RNN class (e.g., `nn.LSTM`) or an instantiated RNN module.
        output_dim (int | None, optional):
            The dimension of the output. If not None, an linear layer is added
            to project the RNN's output to this dimension. Defaults to None.
        **kwargs:
            Additional keyword arguments passed to the RNN constructor if `rnn`
            is a class.
    """

    Factory = RnnFactory

    def __init__(self, rnn: type[RnnLike] | RnnLike, output_dim: int | None = None, **kwargs):
        if isinstance(rnn, type):
            rnn = rnn(**kwargs)
        if getattr(rnn, "batch_first", False):
            raise ValueError("RNNs with `batch_first=True` are not supported.")
        if getattr(rnn, "bidirectional", False):
            raise ValueError("RNNs with `bidirectional=True` are not supported.")
        super().__init__(rnn.input_size, output_dim or rnn.hidden_size, is_recurrent=True)
        self.rnn = rnn
        self.output_proj = nn.Linear(rnn.hidden_size, output_dim) if output_dim else nn.Identity()

    def forward(
        self,
        input: Tensor,
        memory: Memory = None,
        *,
        done: Tensor | None = None,
        sequential: bool = True,
        pack_sequence: bool = False,
        **kwargs,
    ) -> tuple[Tensor, Memory]:
        """Forward pass through the recurrent neural network.

        This method handles both single-steped or sequential data. It resets the
        recurrent state for finished episodes within a sequence when the `done`
        tensor is provided.

        Args:
            input (Tensor):
                Input tensor of shape :math:`(L, ..., N, Ci)` if sequential else
                :math:`(..., N, Ci)`, where :math:`L` is the sequence length,
                :math:`N` is the batch size, and :math:`Ci` is the input channel
                dimension.
            memory (Memory, optional):
                The recurrent state from the previous step. Defaults to None,
                which initializes a zero state.
            done (Tensor | None, optional):
                A boolean tensor of shape :math:`(L, N)` indicating
                terminations. If provided, the memory is reset for the
                corresponding batch entries where `done` is True. Requires
                ``sequential`` to be True. Defaults to None.
            sequential (bool):
                If True, the input is treated as a sequences. Otherwise, it's
                treated as a single batch of data. Defaults to True.
            pack_sequence (bool):
                If True and ``done`` is provided, the input sequence is packed to
                preserve the final recurrent state. Defaults to False.

        Outputs:
            - **output** (Tensor):
                The output tensor of shape :math:`(L, ..., N, Co)` if sequential
                else :math:`(..., N, Co)`, where :math:`Co` is the output
                channel dimension.
            - **memory** (Memory):
                The updated recurrent state.
        """
        if done is not None:
            if not sequential:
                raise ValueError("`done` can only be provided when `sequential` is True.")
            latent, memory = self._forward_rnn_sequence(input, memory, done, pack_sequence=pack_sequence)
        else:
            latent, memory = self._forward_rnn_tensor(input, memory, sequential=sequential)
        return self.output_proj(latent), memory

    def _forward_rnn_tensor(
        self,
        input: Tensor,
        memory: Memory = None,
        sequential: bool = True,
    ) -> tuple[Tensor, Memory]:
        reshaped_input, reshaped_memory = self._reshape_input(input, memory, sequential=sequential)
        reshaped_latent, reshaped_output_memory = self.rnn(reshaped_input, reshaped_memory)
        return self._reshape_output(reshaped_latent, reshaped_output_memory, input.shape, sequential=sequential)

    def _forward_rnn_sequence(
        self,
        input: Tensor,
        memory: Memory,
        done: Tensor,
        pack_sequence: bool = False,
    ) -> tuple[Tensor, Memory]:
        padded_input, mask = split_and_pad_sequences(input, done)
        scattered_memory = scatter_memory(memory, done)
        if pack_sequence:
            if input.dim() != 3:
                raise ValueError(f"Input of RNNs must be 3D to be packed, got {input.dim()}.")
            sequence_lens = compute_sequence_lengths(done)
            reshaped_padded_input, reshaped_scattered_memory = self._reshape_input(padded_input, scattered_memory)
            reshaped_packed_input = nn.utils.rnn.pack_padded_sequence(
                reshaped_padded_input, lengths=sequence_lens.cpu(), enforce_sorted=False
            )
            reshaped_packed_latent, reshaped_scattered_output_memory = self.rnn(
                reshaped_packed_input, reshaped_scattered_memory
            )
            reshaped_padded_latent, _ = nn.utils.rnn.pad_packed_sequence(reshaped_packed_latent)
            padded_latent, scattered_output_memory = self._reshape_output(
                reshaped_padded_latent, reshaped_scattered_output_memory, padded_input.shape
            )
            output_memory = gather_memory(scattered_output_memory, done)
        else:
            padded_latent, _ = self._forward_rnn_tensor(padded_input, scattered_memory)
            output_memory = None
        latent = unpad_and_merge_sequences(padded_latent, mask)
        return latent, output_memory

    def _reshape_input(
        self,
        input: Tensor,
        memory: Memory,
        sequential: bool = True,
    ) -> tuple[Tensor, Memory]:
        if input.dim() < 3:
            # ( C )    -> ( 1, 1, C )
            # ( N, C ) -> ( 1, N, C )
            input = input.reshape(1, -1, input.size(-1))
        if input.dim() >= 3:
            # ( L, N, C )    -> ( L, N, C )     if sequential else ( 1, L * N, C )
            # ( L, R, N, C ) -> ( L, R * N, C ) if sequential else ( 1, L * R * N, C )
            input = input.reshape(input.size(0) if sequential else 1, -1, input.size(-1))
            if memory is not None:
                memory = map_nested(lambda m: m.flatten(1, -2), memory)
        return input, memory

    def _reshape_output(
        self,
        output: Tensor,
        memory: Memory,
        original_input_shape: tuple[int, ...],
        sequential: bool = True,
    ) -> tuple[Tensor, Memory]:
        output = output.reshape(*original_input_shape[:-1], output.size(-1))
        if memory is not None and len(original_input_shape) >= 3:
            memory = map_nested(
                lambda m: m.unflatten(-2, original_input_shape[1 if sequential else 0 : -1]),
                memory,
            )
        return output, memory

    def step_memory(self, input: Tensor, memory: Memory = None, sequential: bool = True, **kwargs):
        original_input_shape = input.shape
        input, memory = self._reshape_input(input, memory, sequential=sequential)
        latent, memory = self.rnn(input, memory)
        _, memory = self._reshape_output(latent, memory, original_input_shape, sequential=sequential)
        return memory


class LstmFactory(ModuleFactory["Lstm"]):
    def __init__(self, hidden_size: int, num_layers: int = 1, bias: bool = True, dropout: float = 0.0, **kwargs):
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.bias = bias
        self.dropout = dropout
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __call__(self, input_dim: int, output_dim: int | None = None):
        return Lstm(input_dim=input_dim, output_dim=output_dim, **self.__dict__)


class Lstm(Rnn):
    Factory = LstmFactory

    def __init__(
        self,
        input_dim: int,
        hidden_size: int,
        num_layers: int = 1,
        bias: bool = True,
        dropout: float = 0.0,
        output_dim: int | None = None,
        **kwargs,
    ):
        super().__init__(
            nn.LSTM,
            input_size=input_dim,
            output_dim=output_dim,
            hidden_size=hidden_size,
            num_layers=num_layers,
            bias=bias,
            dropout=dropout,
            **kwargs,
        )


class GruFactory(ModuleFactory["Gru"]):
    def __init__(self, hidden_size: int, num_layers: int = 1, bias: bool = True, dropout: float = 0.0, **kwargs):
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.bias = bias
        self.dropout = dropout
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __call__(self, input_dim: int, output_dim: int | None = None):
        return Gru(input_dim=input_dim, output_dim=output_dim, **self.__dict__)


class Gru(Rnn):
    Factory = GruFactory

    def __init__(
        self,
        input_dim: int,
        hidden_size: int,
        num_layers: int = 1,
        bias: bool = True,
        dropout: float = 0.0,
        output_dim: int | None = None,
        **kwargs,
    ):
        super().__init__(
            nn.GRU,
            input_size=input_dim,
            hidden_size=hidden_size,
            num_layers=num_layers,
            bias=bias,
            dropout=dropout,
            output_dim=output_dim,
            **kwargs,
        )


def concat_memory(memory1: Memory, memory2: Memory) -> Memory:
    """Concatenates two memory tensors along the batch dimension."""
    if type(memory1) is not type(memory2):
        raise TypeError("Memories must be of the same type to concatenate.")
    if memory1 is None:
        return None
    if isinstance(memory1, Tensor):
        memory2 = cast(Tensor, memory2)
        return torch.cat((memory1, memory2), dim=-2)
    return tuple(concat_memory(m1, m2) for m1, m2 in zip(memory1, memory2))


def scatter_memory(memory: Memory, done: Tensor) -> Memory:
    """Restructures memory tensors from a batch of sequences into a batch of
    episodes.

    This function takes RNN hidden states (``memory``) collected from a batch of
    parallel environments and a `done` tensor that marks episode boundaries. It
    reorganizes the memory so that each element in the new batch dimension
    corresponds to a single, complete or partial episode.

    Args:
        memory (Memory):
            The memory tensor(s) to be scattered of shape :math:`(..., N, C)`,
            where :math:`N` is the batch size and :math:`C` is the channel
            dimension.
        done (Tensor):
            A boolean tensor of shape :math:`(L, C, 1)` indicating episode
            terminations.

    Returns:
        memory (Memory):
            The scattered memory tensor(s) with shape :math:`(..., Ns, C)`,
            where `Ns` is the number of contiguous sequences in the batch.
    """
    if memory is None:
        return None
    if isinstance(memory, tuple):
        return tuple(scatter_memory(mem, done) for mem in memory)

    done = done.squeeze(-1)
    seq_indices = done[:-1].sum(dim=0).cumsum(dim=0)
    seq_indices += torch.arange(1, seq_indices.size(0) + 1, device=done.device)
    num_seq: int = seq_indices[-1].item()
    seq_indices[-1] = 0
    seq_indices = seq_indices.roll(1)

    result_shape = list(memory.shape)
    result_shape[-2] = num_seq
    result = memory.new_zeros(*result_shape)
    result[..., seq_indices, :] = memory
    return result


def gather_memory(memory: Memory, done: Tensor) -> Memory:
    if memory is None:
        return None
    if isinstance(memory, tuple):
        return tuple(gather_memory(mem, done) for mem in memory)

    done = done.squeeze(-1)
    seq_indices = done[:-1].sum(dim=0).cumsum(dim=0)
    seq_indices += torch.arange(0, seq_indices.size(0), device=done.device)
    result = memory[..., seq_indices, :].clone()
    result[..., done[-1], :] = 0.0  # Clear the last hidden state
    return result
