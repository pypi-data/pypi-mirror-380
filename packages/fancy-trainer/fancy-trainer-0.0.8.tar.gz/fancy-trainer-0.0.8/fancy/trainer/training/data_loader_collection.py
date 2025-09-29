from dataclasses import dataclass
from typing import Optional

from torch.utils.data import DataLoader  # type: ignore


@dataclass
class DataLoaderCollection:
    train_loader: DataLoader
    test_loader: DataLoader
    valid_loader: Optional[DataLoader] = None
