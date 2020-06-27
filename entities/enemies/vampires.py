from mixins.animated import Animated
from mixins.health import Health

from utils.frame import Frame

class NormalVampire(Animated, Health):
    maxHealth = 20
    animations = {
        "idle" : [
            Frame(0.25, "enemies/vampires/normal/idle_0.png", flippable=(True, False)),
            Frame(0.25, "enemies/vampires/normal/idle_1.png", flippable=(True, False)),
            Frame(0.25, "enemies/vampires/normal/idle_2.png", flippable=(True, False)),
            Frame(0.25, "enemies/vampires/normal/idle_3.png", flippable=(True, False))
        ]
    }

class EliteVampire(Animated):
    maxHealth = 30
    animations = {
        "idle" : [
            Frame(0.25, "enemies/vampires/elite/idle_0.png", flippable=(True, False)),
            Frame(0.25, "enemies/vampires/elite/idle_1.png", flippable=(True, False)),
            Frame(0.25, "enemies/vampires/elite/idle_2.png", flippable=(True, False)),
            Frame(0.25, "enemies/vampires/elite/idle_3.png", flippable=(True, False))
        ]
    }