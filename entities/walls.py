from mixins.textured import Textured
from utils.texture import Texture

class Wall(Textured):
    textures = {
        "corner_0" : Texture("walls/corner_0.png", flippable=(True, False)),
        "corner_1" : Texture("walls/corner_1.png", flippable=(True, False)),
        "horizontal_0" : Texture("walls/horizontal_0.png", flippable=(True, False)),
        "horizontal_1" : Texture("walls/horizontal_1.png", flippable=(True, False)),
        "horizontal_2" : Texture("walls/horizontal_2.png", flippable=(True, False)),
        "horizontal_3" : Texture("walls/horizontal_3.png", flippable=(True, False)),
        "horizontal_4" : Texture("walls/horizontal_4.png", flippable=(True, False)),
        "horizontal_5" : Texture("walls/horizontal_5.png", flippable=(True, False)),
        "horizontal_6" : Texture("walls/horizontal_6.png", flippable=(True, False)),
        "horizontal_7" : Texture("walls/horizontal_7.png", flippable=(True, False)),
        "horizontal_8" : Texture("walls/horizontal_8.png", flippable=(True, False)),
        "horizontal_9" : Texture("walls/horizontal_9.png", flippable=(True, False)),
        "vertical_0" : Texture("walls/vertical_0.png", flippable=(True, False)),
        "vertical_1" : Texture("walls/vertical_1.png", flippable=(True, False))
    }