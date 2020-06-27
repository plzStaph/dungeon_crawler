from pygame.locals import *
from pygame.event import Event

from mixins.managed import Managed
from mixins.container import Container

from entities.text import Text

class StartScreen(Managed, Container):
    """Start Screen class."""

    def __init__(self):
        Managed.__init__(self)
        Container.__init__(self)
        self.entities = [
            Text("game_title", 60).with_position(100, 50)
        ]

    def on_event(self, event: Event) -> None:
        """Catch events for the Start Screen."""
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.manager.changeScreen("level")
        Container.on_event(self, event)