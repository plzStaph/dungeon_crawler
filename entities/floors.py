from mixins.textured import Textured
from utils.texture import Texture

class Crack(Textured):
    textures = {
        "0"  : Texture("floors/cracks/crack_0.png"),
        "1"  : Texture("floors/cracks/crack_1.png"),
        "2"  : Texture("floors/cracks/crack_2.png"),
        "3"  : Texture("floors/cracks/crack_3.png"),
        "4"  : Texture("floors/cracks/crack_4.png"),
        "5"  : Texture("floors/cracks/crack_5.png"),
        "6"  : Texture("floors/cracks/crack_6.png"),
        "7"  : Texture("floors/cracks/crack_7.png"),
        "8"  : Texture("floors/cracks/crack_8.png"),
        "9"  : Texture("floors/cracks/crack_9.png"),
        "10" : Texture("floors/cracks/crack_10.png"),
        "11" : Texture("floors/cracks/crack_11.png"),
        "12" : Texture("floors/cracks/crack_12.png"),
        "13" : Texture("floors/cracks/crack_13.png")
    }

class Border(Textured):
    textures = {
        "side" : Texture("floors/borders/side.png"),
        "2sides_parallel" : Texture("floors/borders/2sides_parallel.png"),
        "2sides_perpendicular" : Texture("floors/borders/2sides_perpendicular.png"),
        "3sides" : Texture("floors/borders/3sides.png"),
        "4sides" : Texture("floors/borders/4sides.png"),
        "corner" : Texture("floors/borders/corner.png")
    }