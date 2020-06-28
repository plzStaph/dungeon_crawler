from mixins.health import Health
from utils.config import CONFIG

class Attack:
    """Attack class."""

    damage = 0
    cooldown = 0
    dot = 0
    dot_ticks = 0

    def __init__(self):
        self.__cooldown_tick = 0

    def with_attack(self, damage: int) -> object:
        """Overwrite current damage and return self."""
        self.damage = damage
        return self

    def with_cooldown(self, cooldown: int) -> object:
        """Overwrite current cooldown and return self."""
        self.cooldown = cooldown
        return self

    def with_dot(self, damage: int, ticks: int) -> object:
        """Overwrite current dot and dot_ticks. Return self."""
        self.dot = damage
        self.dot_ticks = ticks
        return self

    def attack(self, target: Health) -> None:
        """Attack target and apply dot if applicable."""
        if self.__cooldown_tick == 0:
            target.apply_damage(self.damage)
            if self.dot > 0: target.apply_dot(self.dot, self.dot_ticks)

    def on_update(self) -> None:
        """Checks if attack has completed cooldown upon update."""
        if self.__cooldown_tick == self.cooldown:
            self.__cooldown_tick = 0
        else:
            self.__cooldown_tick += 1