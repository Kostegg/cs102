import abc

from life import GameOfLife


class UI(abc.ABC):
<<<<<<< HEAD
    def __init__(self, life: GameOfLife) -> None:
        self.life = life

    @abc.abstractmethod
=======

    def __init__(self, life: GameOfLife) -> None:
        self.life = life

    @abc.abstractmethod:
>>>>>>> daaaf63... Initial commit
    def run(self) -> None:
        pass
