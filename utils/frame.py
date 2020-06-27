from pygame import Surface

from typing import Tuple

from utils.texture import Texture
from utils.config import CONFIG

class Frame:
    """Frame class."""

    def __init__(self, duration: float, relative_path: str,
        size = (1, 1), offset = (0, 0), flippable = (False, False)
    ):
        self.duration = duration
        self.texture = Texture(relative_path, size, offset, flippable)

    def on_init(self) -> None:
        """Load texture and fps-friendly duration upon initialization."""
        self.duration = int(self.duration * CONFIG.fps)
        self.texture.on_init()

    def on_render(self, surface: Surface,
        surface_position: Tuple[int, int],
        flipped = (False, False)
    ) -> None:
        """Render on given surface."""
        self.texture.on_render(surface, surface_position, flipped)