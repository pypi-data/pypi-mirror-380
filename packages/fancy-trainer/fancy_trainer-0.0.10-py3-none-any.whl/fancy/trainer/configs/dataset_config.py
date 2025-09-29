from typing import MutableMapping, Callable, Optional

from ..configs import ImporterConfig
from fancy import config as cfg
from torch.utils.data import DataLoader, Dataset  # type: ignore


class DatasetConfig(ImporterConfig):
    param = cfg.Option(default={}, type=cfg.process.flag_container)

    batch_size = cfg.Option(default=1, type=int)
    shuffle = cfg.Option(default=False, type=bool)
    pin_memory = cfg.Option(default=True, type=bool)
    num_workers = cfg.Option(default=0, type=int)
    transform: Optional[Callable] = None
    target_transform: Optional[Callable] = None

    def set_transforms(
        self, transform: Optional[Callable], target_transform: Optional[Callable]
    ):
        self.transform = transform
        self.target_transform = target_transform

    @property
    def loader(self) -> DataLoader:
        loader = DataLoader(
            self.dataset,
            shuffle=self.shuffle,
            pin_memory=self.pin_memory,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
        )

        return loader

    # TODO transform and target_transform
    @property
    def dataset(self) -> Dataset:
        cls = self.imported
        if not isinstance(cls, type):
            raise ValueError("Dataset type should be a class method_name.")
        if not issubclass(cls, Dataset):
            raise ValueError(f"Incorrect dataset type: {cls}.")
        if not isinstance(self.param, MutableMapping):
            raise ValueError("param must be instance of MutableMapping")
        dataset = cls(
            transform=self.transform,  # type: ignore
            target_transform=self.target_transform,  # type: ignore
            **self.param,  # type: ignore
        )

        return dataset
