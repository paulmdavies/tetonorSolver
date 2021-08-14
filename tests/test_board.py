from unittest import TestCase
from unittest.mock import MagicMock

from src.board import Board


class TestBoard(TestCase):
    def setUp(self):
        self.grid_numbers = MagicMock()
        self.strip_numbers = MagicMock()
        self.board = Board(self.grid_numbers, self.strip_numbers)

    def test_should_return_grid_numbers(self):
        self.assertEqual(
            self.grid_numbers,
            self.board.grid_numbers()
        )

    def test_should_return_strip_numbers(self):
        self.assertEqual(
            self.strip_numbers,
            self.board.strip_numbers()
        )
