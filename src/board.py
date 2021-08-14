from typing import Optional


class Board:
    def __init__(self, grid_numbers: list[int], strip_numbers: list[Optional[int]]):
        self._grid_numbers = grid_numbers
        self._strip_numbers = strip_numbers

    def grid_numbers(self) -> list[int]:
        return self._grid_numbers

    def strip_numbers(self) -> list[Optional[int]]:
        return self._strip_numbers