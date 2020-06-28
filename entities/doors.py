from mixins.textured import Textured
from utils.texture import Texture

class IronSingleDoor(Textured):
    textures = {
        "closed": Texture("doors/iron/single/closed.png"),
        "open_up": Texture("doors/iron/single/open_up.png", offset=(0, -1)),
        "open_down": Texture("doors/iron/single/open_down.png")
    }

class IronDoubleDoor(Textured):
    textures = {
        "closed": Texture("doors/iron/double/closed.png"),
        "open_up": Texture("doors/iron/double/open_up.png", offset=(0, -1)),
        "open_down": Texture("doors/iron/double/open_down.png")
    }

class GoldenSingleDoor(Textured):
    textures = {
        "closed": Texture("doors/gold/single/closed.png"),
        "open_up": Texture("doors/gold/single/open_up.png", offset=(0, -1)),
        "open_down": Texture("doors/gold/single/open_down.png")
    }

class GoldenDoubleDoor(Textured):
    textures = {
        "closed": Texture("doors/gold/double/closed.png"),
        "open_up": Texture("doors/gold/double/open_up.png", offset=(0, -1)),
        "open_down": Texture("doors/gold/double/open_down.png")
    }