from random import random
from utils.config import CONFIG

class Health:
    """Health class."""

    maxHealth = 0
    dot_resist = 100

    def __init__(self):
        self.vulnerable = True
        self.currentHealth = self.maxHealth
        self.dot = 0
        self.__dot_tick = 0
        self.__dot_max_ticks = 0

    def with_health(self, health: int) -> object:
        """Overwrite current health and return self."""
        self.currentHealth = health
        return self

    def apply_dot(self, damage: int, ticks: int) -> bool:
        """Set damage on tick and return if it was successfully applied."""
        
        if int(random()*100) > self.dot_resist:
            self.dot = damage
            self.__dot_tick = 0
            self.__dot_max_ticks = ticks * CONFIG.fps
            return True
        return False

    def apply_damage(self, damage: int) -> int:
        """Damage health if entity is vulnerable and return damage received."""
        received_damage = 0
        if self.vulnerable:
            if self.currentHealth > damage: received_damage = damage
            else: received_damage = self.currentHealth
        self.currentHealth -= received_damage
        return received_damage

    def alive(self) -> bool:
        """Return alive status."""
        return self.currentHealth > 0

    def on_update(self) -> None:
        """Checks for and calls damage on tick upon update."""
        if self.__dot_tick == self.__dot_max_ticks:
            self.dot = 0
        elif self.dot > 0:
            if self.__dot_tick % CONFIG.fps == 0:
                self.apply_damage(self.dot)
            self.__dot_tick += 1