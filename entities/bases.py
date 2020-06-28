from mixins.textured import Textured
from utils.texture import Texture

class Base(Textured):
    textures = {
        "light"  : Texture("base/dark.png"),
        "medium" : Texture("base/medium.png"),
        "hard"   : Texture("base/hard.png")
    }