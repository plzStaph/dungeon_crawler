from pygame import Surface

from mixins.position import Position

from utils.texture import Texture

class Textured(Position):
    """Texture class."""

    texture = None
    textures = {}
    init_textures = False

    def __init__(self, state = ""):
        Position.__init__(self)
        self.active_state = state

    def on_init(self) -> None:
        """Load textures upon initialization."""
        if not self.init_textures:
            if self.texture and self.textures:
                raise ValueError("Cannot have a single and multiple textures simultaneosly!")
            elif self.texture:
                self.texture.on_init()
            else:
                for texture in self.textures.values():
                    texture.on_init()
            self.init_textures = True

    def get_texture(self) -> Texture:
        """Return current texture."""
        if self.texture: return self.texture
        return self.textures[self.active_state]

    def on_render(self, surface: Surface) -> None:
        """Render entity on given surface."""
        self.get_texture().on_render(surface,
            self.get_position(), self.get_flipped())