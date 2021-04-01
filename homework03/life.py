import pathlib
import random
<<<<<<< HEAD
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
=======

from typing import List, Optional, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool=True,
        max_generations: Optional[float]=float('inf')
>>>>>>> daaaf63... Initial commit
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

<<<<<<< HEAD
    def create_grid(self, randomize: bool = False) -> Grid:
=======
    def create_grid(self, randomize: bool=False) -> Grid:
>>>>>>> daaaf63... Initial commit
        # Copy from previous assignment
        pass

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        pass

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        pass

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        pass

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        pass

    @staticmethod
<<<<<<< HEAD
    def from_file(filename: pathlib.Path) -> "GameOfLife":
=======
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
>>>>>>> daaaf63... Initial commit
        """
        Прочитать состояние клеток из указанного файла.
        """
        pass

<<<<<<< HEAD
    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
=======
    def save(filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
>>>>>>> daaaf63... Initial commit
