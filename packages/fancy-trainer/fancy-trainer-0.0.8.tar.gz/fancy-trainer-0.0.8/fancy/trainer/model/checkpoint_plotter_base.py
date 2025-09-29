from abc import ABC, abstractmethod
from typing import Dict
from matplotlib.figure import Figure

from . import Checkpoint


class CheckpointPlotterBase(ABC):
    @abstractmethod
    def plot(self, checkpoint: Checkpoint) -> Dict[str, Figure]:
        pass
