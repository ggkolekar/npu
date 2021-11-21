from abc import ABC, abstractmethod, abstractproperty
class Shape(ABC):
    def __init__(self, name:str) -> None:
        self._name = name
        @abstractmethod
    def surfaceArea(self) -> float:
    pass
    def display(self):
        print('name:', self._name)