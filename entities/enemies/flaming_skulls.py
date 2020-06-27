from mixins.animated import Animated
from mixins.health import Health

from utils.frame import Frame

class NormalFlamingSkull(Animated, Health):
    maxHealth = 4
    animations = {
        "idle" : [
            Frame(0.2, "enemies/flaming_skulls/normal/idle_0.png", flippable=(True, False)),
            Frame(0.2, "enemies/flaming_skulls/normal/idle_1.png", flippable=(True, False)),
            Frame(0.2, "enemies/flaming_skulls/normal/idle_2.png", flippable=(True, False)),
            Frame(0.2, "enemies/flaming_skulls/normal/idle_3.png", flippable=(True, False))
        ]
    }

class EliteFlamingSkull(Animated):
    maxHealth = 6
    animations = {
        "idle" : [
            Frame(0.2, "enemies/flaming_skulls/elite/idle_0.png", flippable=(True, False)),
            Frame(0.2, "enemies/flaming_skulls/elite/idle_1.png", flippable=(True, False)),
            Frame(0.2, "enemies/flaming_skulls/elite/idle_2.png", flippable=(True, False)),
            Frame(0.2, "enemies/flaming_skulls/elite/idle_3.png", flippable=(True, False))
        ]
    }