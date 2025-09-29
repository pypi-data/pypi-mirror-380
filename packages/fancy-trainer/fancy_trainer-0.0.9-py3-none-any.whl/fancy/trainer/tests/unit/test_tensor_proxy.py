from copy import deepcopy

import pytest
import torch

from fancy.trainer.model import TensorProxy


class TestTensorProxy:
    tensors = [
        torch.tensor([0, 1, 2, 3]),
        torch.tensor([0, 0, 2, 3]),
        torch.tensor([0, 1, 0, 3]),
        torch.tensor([0, 1, 2, 0]),
    ]

    @pytest.fixture()
    def tensor(self):
        return TensorProxy(deepcopy(self.tensors))

    def test_initialize_no_tensor_in(self):
        with pytest.raises(ValueError):
            TensorProxy()

    def test_initialize_tensor_idx_out_of_bound(self):
        with pytest.raises(IndexError):
            TensorProxy([torch.tensor([0, 1, 2, 3])], tensor_idx=1)

    def test_not_exists_attribute(self, tensor: TensorProxy):
        with pytest.raises(AttributeError):
            tensor.abcd()  # type: ignore

    @pytest.mark.parametrize(
        "tensor_idx,expected_tensor",
        [(i, tensor.clone()) for i, tensor in enumerate(tensors)],
    )
    def test_tensor_method(self, tensor_idx, expected_tensor, tensor: TensorProxy):
        tensor.current_tensor_idx = tensor_idx
        assert torch.equal(tensor, expected_tensor)
        assert torch.equal(tensor.view(-1), expected_tensor)
        assert torch.equal(tensor + 2, expected_tensor + 2)
        assert torch.equal(tensor - 2, expected_tensor - 2)
        assert torch.equal(tensor * 2, expected_tensor * 2)
        assert torch.equal(tensor / 2, expected_tensor / 2)
        assert tensor[0] == expected_tensor[0]
        assert torch.equal(tensor[1:], expected_tensor[1:])
        assert torch.equal(tensor[:2], expected_tensor[:2])
        assert torch.equal(tensor[2:4], expected_tensor[2:4])
        assert torch.equal(tensor[::1], expected_tensor[::1])
        assert isinstance(tensor + 2, TensorProxy)
        assert isinstance(tensor[0], TensorProxy)
        assert isinstance(tensor[0].item(), int)
        tensor += 2  # type: ignore
        assert isinstance(tensor, TensorProxy)
        assert torch.equal(tensor, expected_tensor + 2)

    def test_shallow_copy_disabled(self, tensor: TensorProxy):
        tensor_idx = 2
        tensor.current_tensor_idx = tensor_idx
        real_tensor = tensor + 2
        assert isinstance(real_tensor, TensorProxy)
        assert all(
            torch.equal(real, original)
            for i, (real, original) in enumerate(
                zip(real_tensor._tensors, tensor._tensors)
            )
            if i != tensor.current_tensor_idx
        )
        assert torch.equal(real_tensor._tensors[tensor_idx], self.tensors[tensor_idx] + 2)
        with TensorProxy.shallow_copy_mode(tensor, is_enabled=False):
            real_tensor = tensor + 2
            assert not isinstance(real_tensor, TensorProxy)
            assert isinstance(real_tensor, torch.Tensor)

            # nested
            with TensorProxy.shallow_copy_mode(tensor, is_enabled=True):
                real_tensor = tensor + 2
                assert isinstance(real_tensor, TensorProxy)

            real_tensor = tensor + 2
            assert not isinstance(real_tensor, TensorProxy)
            assert isinstance(real_tensor, torch.Tensor)

    def test_apply_all(self, tensor: TensorProxy):
        other = torch.zeros(6, dtype=torch.int32)
        with TensorProxy.apply_all(tensor, other, is_enabled=True):
            other += 2
            tensor += 2  # type: ignore
        assert all(
            torch.equal(added_tensor, original + 2)
            for added_tensor, original in zip(tensor._tensors, self.tensors)
        )
        assert torch.equal(other, torch.tensor([2] * 6, dtype=torch.int32))
