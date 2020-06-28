from mixins.textured import Textured
from utils.texture import Texture

class Base(Textured):
    textures = {
        "light"  : Texture("base/light.png"),
        "medium" : Texture("base/medium.png"),
        "dark"   : Texture("base/dark.png")
    }