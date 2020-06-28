from pygame import image, transform, Surface

from typing import Tuple

from utils.config import CONFIG

class Texture:
    """Texture class."""

    def __init__(self, relative_path: str,
        offset = (0, 0), flippable = (False, False)
    ):
        self.image = None
        self.flippable = flippable
        self.path = f'assets/textures/{relative_path}'
        self.offset = offset

    def on_init(self) -> None:
        """Load image upon initialization."""
        _image = image.load(self.path)
        _rect = _image.get_rect()
        
        self.image = transform.scale(_image, (
            _rect.width * CONFIG.get_texture_factor(),
            _rect.height * CONFIG.get_texture_factor()
        ))

        if all(self.flippable):
            self.image_flipped_xy = transform.flip(
                self.image, True, True)
        if self.flippable[0]:
            self.image_flipped_x = transform.flip(
                self.image, True, False)
        if self.flippable[1]:
            self.image_flipped_y = transform.flip(
                self.image, False, True)

    def get_image(self, flipped: Tuple[bool, bool]) -> Surface:
        """Return current image."""
        image = self.image
        if all(flipped):
            image = self.image_flipped_xy
        elif flipped[0]:
            image = self.image_flipped_x
        elif flipped[1]:
            image = self.image_flipped_y
        return image

    def on_render(self, surface: Surface,
        surface_position: Tuple[int, int],
        flipped = (False, False)
    ) -> None:
        """Render on given surface."""
        surface.blit(self.get_image(flipped), (
            (surface_position[0] + self.offset[0]) * CONFIG.grid_size,
            (surface_position[1] + self.offset[1]) * CONFIG.grid_size
        ))