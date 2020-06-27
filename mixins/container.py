from pygame import Surface
from pygame import draw
from pygame.event import Event

from mixins.position import Position

from utils.config import CONFIG
from utils.colors import LIGHT

class Container(Position):
    """Coordinator class."""

    def __init__(self):
        Position.__init__(self)
        self.__display_surf = None
        self.entities = []
        self.__init = False

    def on_init(self) -> None:
        """Run on_init hook on all entities."""
        if not self.__init:
            self.__display_surf = Surface(CONFIG.get_screen_size())
            for entity in self.entities:
                if hasattr(entity, "on_init"):
                    entity.on_init()
            self.__init = True

    def on_event(self, event: Event) -> None:
        """Run on_event hook on all entities."""
        for entity in self.entities:
            if hasattr(entity, "on_event"):
                entity.on_event(event)

    def on_update(self) -> None:
        """Run on_update hook on all entities."""
        for entity in self.entities:
            if hasattr(entity, "on_update"):
                entity.on_update()

    def on_render(self, surface: Surface) -> None:
        """Run on_render hook on all entities."""
        self.__display_surf.fill(LIGHT)
        for entity in self.entities:
            if hasattr(entity, "on_render"):
                entity.on_render(self.__display_surf)
        surface.blit(self.__display_surf, self.get_position())

    def on_quit(self) -> None:
        """Run on_quit hook on all entities."""
        for entity in self.entities:
            if hasattr(entity, "on_quit"):
                entity.on_quit()