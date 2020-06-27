from typing import  Tuple

class Position:
    """Position class. Keeps reference to position and flipped axis."""

    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_flipped = False
        self.y_flipped = False

    def with_position(self, x: int, y: int) -> object:
        """Set position and return self."""
        self.x = x
        self.y = y
        return self

    def get_position(self) -> Tuple[int, int]:
        """Return position as tuple."""
        return (self.x, self.y)

    def with_flipped(self, x_flipped: bool, y_flipped: bool) -> object:
        """Set flipped axis and return self."""
        self.x_flipped = x_flipped
        self.y_flipped = y_flipped
        return self

    def get_flipped(self) -> Tuple[bool, bool]:
        """Return flipped axis as tuple."""
        return (self.x_flipped, self.y_flipped)