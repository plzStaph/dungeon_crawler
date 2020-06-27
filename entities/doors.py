from mixins.textured import Textured
from utils.texture import Texture

class IronSingleDoor(Textured):
    textures = {
        "closed": Texture("doors/iron/single/closed.png"),
        "open_up": Texture("doors/iron/single/open_up.png", size=(1, 2), offset=(0, -1)),
        "open_down": Texture("doors/iron/single/open_down.png", size=(1, 2))
    }

class IronDoubleDoor(Textured):
    textures = {
        "closed": Texture("doors/iron/double/closed.png", size=(2, 1)),
        "open_up": Texture("doors/iron/double/open_up.png", size=(2, 2), offset=(0, -1)),
        "open_down": Texture("doors/iron/double/open_down.png", size=(2, 2))
    }

class GoldenSingleDoor(Textured):
    textures = {
        "closed": Texture("doors/gold/single/closed.png"),
        "open_up": Texture("doors/gold/single/open_up.png", size=(1, 2), offset=(0, -1)),
        "open_down": Texture("doors/gold/single/open_down.png", size=(1, 2))
    }

class GoldenDoubleDoor(Textured):
    textures = {
        "closed": Texture("doors/gold/double/closed.png", size=(2, 1)),
        "open_up": Texture("doors/gold/double/open_up.png", size=(2, 2), offset=(0, -1)),
        "open_down": Texture("doors/gold/double/open_down.png", size=(2, 2))
    }