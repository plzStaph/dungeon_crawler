from pygame import Surface

from typing import List
from random import randint

from mixins.position import Position

from utils.frame import Frame

class Animated(Position):
    """Animated class."""

    animations = {}
    init_frames = False

    def __init__(self, animation: str):
        Position.__init__(self)
        self.active_animation = animation
        self.frame_counter = 0
        self.tick_counter = 0

    def on_init(self) -> None:
        """Load textures upon initialization."""
        if not self.init_frames:
            for animation in self.animations.values():
                for frame in animation:
                    frame.on_init()
            self.init_frames = True

        self.tick_counter = randint(0, self.get_frame().duration)

    def get_frames(self) -> List[Frame]:
        """Return the frames for current animation."""
        return self.animations[self.active_animation]

    def get_frame(self) -> Frame:
        """Return the current frame."""
        return self.get_frames()[self.frame_counter]

    def on_update(self) -> None:
        """Update animation ticks upon update."""
        if self.tick_counter < self.get_frame().duration - 1:
            self.tick_counter += 1
        else:
            self.tick_counter = 0
            if self.frame_counter < len(self.get_frames()) -1:
                self.frame_counter += 1
            else:
                self.frame_counter = 0

    def on_render(self, surface: Surface) -> None:
        """Render entity on surface."""
        self.get_frame().on_render(surface,
            self.get_position(), self.get_flipped())