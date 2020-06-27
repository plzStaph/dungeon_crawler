from pygame.locals import *
from pygame.event import Event

from mixins.managed import Managed
from mixins.container import Container

from entities.text import Text
from entities.doors import (
    IronSingleDoor, IronDoubleDoor,
    GoldenSingleDoor, GoldenDoubleDoor
)
from entities.hatches import IronHatch, GoldenHatch

from entities.enemies.flaming_skulls import (
    NormalFlamingSkull, EliteFlamingSkull
)
from entities.enemies.skeletons import (
    NormalSwordSkeleton, EliteSwordSkeleton,
    NormalScytheSkeleton, EliteScytheSkeleton
)
from entities.enemies.vampires import (
    NormalVampire, EliteVampire
)

from entities.items import Coin, IronKey, GoldKey
from entities.potions import (
    SmallHealthPotion, BigHealthPotion,
    SmallManaPotion, BigManaPotion
)

from entities.prompts import (
    PC_Prompt, PS_Prompt, XBOX_Prompt
)

class LevelScreen(Managed, Container):
    """Level Screen class."""

    def __init__(self) -> None:
        Managed.__init__(self)
        Container.__init__(self)
        self.entities = [
            Text("lorem_ipsum", 32).with_position(100, 50),
            IronSingleDoor("closed").with_position(0, 3),
            IronSingleDoor("open_up").with_position(1, 3),
            IronSingleDoor("open_down").with_position(2, 3),
            IronDoubleDoor("closed").with_position(3, 3),
            IronDoubleDoor("open_up").with_position(5, 3),
            IronDoubleDoor("open_down").with_position(7, 3),
            IronHatch("closed").with_position(9, 3),
            IronHatch("open").with_position(10, 3),
            GoldenSingleDoor("closed").with_position(0, 5),
            GoldenSingleDoor("open_up").with_position(1, 5),
            GoldenSingleDoor("open_down").with_position(2, 5),
            GoldenDoubleDoor("closed").with_position(3, 5),
            GoldenDoubleDoor("open_up").with_position(5, 5),
            GoldenDoubleDoor("open_down").with_position(7, 5),
            GoldenHatch("closed").with_position(9, 5),
            GoldenHatch("open").with_position(10, 5),
            NormalFlamingSkull("idle").with_position(0, 7),
            NormalSwordSkeleton("idle").with_position(1, 7),
            NormalScytheSkeleton("idle").with_position(2, 7),
            NormalVampire("idle").with_position(3, 7),
            EliteFlamingSkull("idle").with_position(0, 9),
            EliteSwordSkeleton("idle").with_position(1, 9),
            EliteScytheSkeleton("idle").with_position(2, 9),
            EliteVampire("idle").with_position(3, 9),
            Coin().with_position(0, 11),
            IronKey().with_position(1, 11),
            GoldKey().with_position(2, 11),
            SmallHealthPotion().with_position(3, 11),
            BigHealthPotion().with_position(4, 11),
            SmallManaPotion().with_position(5, 11),
            BigManaPotion().with_position(6, 11),
            PC_Prompt("a").with_position(7, 11),
            PS_Prompt("x").with_position(8, 11),
            XBOX_Prompt("x").with_position(9, 11)
        ]
        self.controllable = self.entities[18]

    def on_event(self, event: Event) -> None:
        """Catch events for the Level Screen."""
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.manager.changeScreen("start")
            elif event.key == K_a:
                self.controllable.x -= 1
                self.controllable.x_flipped = True
            elif event.key == K_d:
                self.controllable.x += 1
                self.controllable.x_flipped = False
            elif event.key == K_w:
                self.controllable.y -= 1
            elif event.key == K_s:
                self.controllable.y += 1
        Container.on_event(self, event)