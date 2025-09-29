from functools import cached_property
from torch import Tensor
from fancy import config as cfg

from . import ImporterConfig


class LossFunctionConfig(ImporterConfig):
    param = cfg.Option(default={}, type=cfg.process.flag_container)

    @cached_property
    def loss_func(self):
        if isinstance(self.imported, type):
            return self.imported(**self.param)
        return self.imported

    def eval_loss(self, data: Tensor, target: Tensor):
        return self.loss_func(data, target)
