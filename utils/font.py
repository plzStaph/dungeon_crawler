from pygame import Surface
from pygame import freetype

from typing import Tuple
from utils.config import CONFIG

class Font:
    """Font class. Selects localization safe font."""

    def __init__(self):
        self.font = None

    def on_init(self) -> None:
        """Load font based on current localization setting."""
        self.font = freetype.Font(f'assets/fonts/monogram_extended_{CONFIG.localization}.ttf')

FONT = Font()