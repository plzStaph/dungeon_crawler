from mixins.textured import Textured
from utils.texture import Texture

class SmallHealthPotion(Textured):
    texture = Texture("items/potions/health/small.png")

class BigHealthPotion(Textured):
    texture = Texture("items/potions/health/big.png")

class SmallManaPotion(Textured):
    texture = Texture("items/potions/mana/small.png")

class BigManaPotion(Textured):
    texture = Texture("items/potions/mana/big.png")