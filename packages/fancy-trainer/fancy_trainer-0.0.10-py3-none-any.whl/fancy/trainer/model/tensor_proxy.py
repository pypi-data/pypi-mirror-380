from contextlib import contextmanager
from typing import Callable, List, Optional, Iterable

import torch

METHOD_SHOULD_NOT_FORWARD = [
    "__torch_function__",
]


class TensorProxy(torch.Tensor):
    _tensors: List[torch.Tensor]
    _current_tensor_idx: int
    _shallow_copy_enabled: bool
    _apply_all_enabled: bool

    def __init__(self, tensors: Optional[List[torch.Tensor]] = None, tensor_idx: int = 0):
        if tensors is None:
            tensors = []
        self._tensors = tensors
        self._shallow_copy_enabled = True
        self._apply_all_enabled = False
        if len(self._tensors) > 0:
            if tensor_idx < len(self._tensors):
                self._current_tensor_idx = tensor_idx
            else:
                raise IndexError(
                    f"tensor_idx out of bound: {tensor_idx} >= {len(self._tensors)}"
                )
        else:
            raise ValueError("Need at least one tensor.")

    def __new__(cls, *args, **kwargs):
        return super(TensorProxy, cls).__new__(cls)

    def __dir__(self):
        return object.__dir__(self)

    def __str__(self):
        return (
            type(self).__name__.lower()
            + "{"
            + f"tensor_idx: {self._current_tensor_idx}, "
            f"current_tensor:{self.current_tensor}" + "}"
        )

    def __repr__(self):
        return str(self)

    @property
    def current_tensor_idx(self) -> int:
        return self._current_tensor_idx

    @current_tensor_idx.setter
    def current_tensor_idx(self, val: int) -> None:
        self._current_tensor_idx = val

    @property
    def num_tensors(self) -> int:
        return len(self._tensors)

    @property
    def current_tensor(self) -> torch.Tensor:
        return self._tensors[self._current_tensor_idx]

    def set_shallow_copy_mode(self, enable: bool) -> None:
        self._shallow_copy_enabled = enable

    @staticmethod
    def apply_all(*proxies: torch.Tensor, is_enabled: bool = True):
        return TensorProxy._set_modes(proxies, is_enabled, "_apply_all_enabled")

    @staticmethod
    def shallow_copy_mode(*proxies: torch.Tensor, is_enabled: bool):
        return TensorProxy._set_modes(proxies, is_enabled, "_shallow_copy_enabled")

    @staticmethod
    @contextmanager
    def _set_modes(proxies: Iterable[torch.Tensor], value: bool, mode: str):
        enabled_list = []
        for proxy in proxies:
            if isinstance(proxy, TensorProxy):
                enabled_list.append(getattr(proxy, mode))
                setattr(proxy, mode, value)
            enabled_list.append(None)
        try:
            yield
        finally:
            for i, proxy in enumerate(proxies):
                if enabled_list[i] is not None:
                    setattr(proxy, mode, enabled_list[i])

    @classmethod
    def __torch_function__(cls, func, types, args=(), kwargs=None):
        types = [torch.Tensor if tp is cls else tp for tp in types]
        args = [arg.current_tensor if isinstance(arg, cls) else arg for arg in args]
        if kwargs is not None:
            kwargs = {
                key: arg.current_tensor if isinstance(arg, cls) else arg
                for key, arg in kwargs
            }
        return torch.Tensor.__torch_function__(func, types, args, kwargs)


def _wrapper(method_name):
    def _forward(self: TensorProxy, *args, **kwargs):
        method = getattr(self.current_tensor, method_name)
        result = method(*args, **kwargs)
        if self._apply_all_enabled and isinstance(result, torch.Tensor):
            tensors: List[Optional[torch.Tensor]] = [None] * self.num_tensors
            current_tensor_idx = self._current_tensor_idx
            tensors[current_tensor_idx] = result
            for i in range(self.num_tensors):
                if i == current_tensor_idx:
                    continue
                self._current_tensor_idx = i
                tensors[i] = getattr(self.current_tensor, method_name)(*args, **kwargs)
            self._current_tensor_idx = current_tensor_idx
            result = TensorProxy(tensors, tensor_idx=current_tensor_idx)  # type: ignore
        elif self._shallow_copy_enabled and isinstance(result, torch.Tensor):
            tensors = self._tensors.copy()  # type: ignore
            tensors[self._current_tensor_idx] = result
            result = TensorProxy(tensors, tensor_idx=self._current_tensor_idx)  # type: ignore

        return result

    return _forward


for name in (
    set(dir(torch.Tensor)).difference(dir(object)).difference(METHOD_SHOULD_NOT_FORWARD)
):
    if isinstance(getattr(torch.Tensor, name), Callable):
        try:
            setattr(TensorProxy, name, _wrapper(name))
        except AttributeError:
            pass
