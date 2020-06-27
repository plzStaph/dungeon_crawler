from mixins.textured import Textured
from utils.texture import Texture

class Coin(Textured):
    texture = Texture("items/gold_coin.png")

class IronKey(Textured):
    texture = Texture("items/keys/iron.png")

class GoldKey(Textured):
    texture = Texture("items/keys/gold.png")