from mixins.animated import Animated
from mixins.health import Health

from utils.frame import Frame

class NormalSwordSkeleton(Animated, Health):
    maxHealth = 10
    animations = {
        "idle" : [
            Frame(0.25, "enemies/skeletons/normal/sword/idle_0.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/normal/sword/idle_1.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/normal/sword/idle_2.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/normal/sword/idle_3.png", flippable=(True, False))
        ]
    }

class EliteSwordSkeleton(Animated, Health):
    maxHealth = 15
    animations = {
        "idle" : [
            Frame(0.25, "enemies/skeletons/elite/sword/idle_0.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/elite/sword/idle_1.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/elite/sword/idle_2.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/elite/sword/idle_3.png", flippable=(True, False))
        ]
    }

class NormalScytheSkeleton(Animated, Health):
    maxHealth = 8
    animations = {
        "idle" : [
            Frame(0.25, "enemies/skeletons/normal/scythe/idle_0.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/normal/scythe/idle_1.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/normal/scythe/idle_2.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/normal/scythe/idle_3.png", flippable=(True, False))
        ]
    }

class EliteScytheSkeleton(Animated, Health):
    maxHealth = 10
    animations = {
        "idle" : [
            Frame(0.25, "enemies/skeletons/elite/scythe/idle_0.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/elite/scythe/idle_1.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/elite/scythe/idle_2.png", flippable=(True, False)),
            Frame(0.25, "enemies/skeletons/elite/scythe/idle_3.png", flippable=(True, False))
        ]
    }