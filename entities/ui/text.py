from pygame import Surface
from mixins.position import Position

from utils.localization import LOCALIZATION
from utils.font import FONT
from utils.colors import DARK

class Text(Position):
    """Text class."""

    def __init__(self, key: str, size: int, color = DARK):
        self.key = key
        self.size = size
        self.color = color
        self.__surf = None
        self.__rect = None

    def on_init(self) -> None:
        """Create surface upon initialization."""

        self.__surf, _ = FONT.font.render(
            getattr(LOCALIZATION, self.key), self.color, size = self.size)
        self.__rect = self.__surf.get_rect()

    def on_render(self, surface: Surface) -> None:
        """Render on given surface."""

        surface.blit(self.__surf, self.get_position(), self.__rect)