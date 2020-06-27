from mixins.textured import Textured
from utils.texture import Texture

class IronHatch(Textured):
    textures = {
        "closed": Texture("hatches/iron/closed.png"),
        "open": Texture("hatches/iron/open.png", size=(1, 2), offset=(0, -1))
    }

class GoldenHatch(Textured):
    textures = {
        "closed": Texture("hatches/gold/closed.png"),
        "open": Texture("hatches/gold/open.png", size=(1, 2), offset=(0, -1))
    }