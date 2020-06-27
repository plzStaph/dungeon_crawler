from pygame import image, transform, Surface

from typing import Tuple

from utils.config import CONFIG

class Texture:
    """Texture class."""

    def __init__(self, relative_path: str,
        size = (1, 1), offset = (0, 0), flippable = (False, False)
    ):
        self.image = None
        self.flippable = flippable
        self.path = "assets/textures/" + relative_path
        self.size = size
        self.offset = offset

    def on_init(self) -> None:
        """Load image upon initialization."""
        self.image = transform.scale(image.load(self.path), (
            self.size[0] * CONFIG.display_size,
            self.size[1] * CONFIG.display_size
        ))

        if any(self.flippable):
            self.flipped_image = {}
            if self.flippable[0]:
                self.flipped_image["x"] = transform.flip(self.image, True, False)
            if self.flippable[1]:
                self.flipped_image["y"] = transform.flip(self.image, False, True)
            if all(self.flippable):
                self.flipped_image["xy"] = transform.flip(self.image, True, True)

    def get_image(self, flipped: bool) -> Surface:
        """Return current image."""
        image = self.image
        if any(self.flippable):
            if flipped[0]:
                image = self.flipped_image["x"]
            elif flipped[1]:
                image = self.flipped_image["y"]
            elif all(flipped):
                image = self.flipped_image["xy"]
        return image

    def on_render(self, surface: Surface,
        surface_position: Tuple[int, int],
        flipped = (False, False)
    ) -> None:
        """Render on given surface."""
        surface.blit(self.get_image(flipped), (
            (surface_position[0] + self.offset[0]) * CONFIG.display_size,
            (surface_position[1] + self.offset[1]) * CONFIG.display_size
        ))