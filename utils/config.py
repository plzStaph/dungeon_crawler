from pygame import HWSURFACE, DOUBLEBUF, FULLSCREEN
from typing import Tuple

from utils.jsonHandler import loadFromJson, saveToJson

class Config:
    """Config class. Interacts with config.json file."""

    def on_init(self) -> None:
        """Load config into json file."""
        loadFromJson(self, "config.json")

    def get_texture_factor(self) -> int:
        """Return texture factor."""
        return int(self.grid_size/16)

    def get_screen_size(self) -> Tuple[int, int]:
        """Return screen size as tuple."""
        return (self.screen_width, self.screen_height)

    def get_screen_flags(self) -> int:
        """Return screen flags"""
        flags = HWSURFACE | DOUBLEBUF
        if not self.fullscreen: return flags
        return (flags | FULLSCREEN)

    def save(self) -> None:
        """Save config into json file."""
        saveToJson(self, "config.json")

CONFIG = Config()