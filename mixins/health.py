class Health:
    """Health class."""

    maxHealth = 0

    def __init__(self):
        self.currentHealth = self.maxHealth
        self.damage_on_tick = 0
        self.vulnerable = True

    def with_health(self, health: int) -> object:
        """Set current health and return self."""
        self.currentHealth = health
        return self

    def damage(self, damage: int) -> None:
        """Damage health if entity is vulnerable."""
        if self.vulnerable:
            self.currentHealth = max(
                self.currentHealth - damage, 0)

    def on_update(self) -> None:
        """Checks for and calls damage on tick upon update."""
        if self.damage_on_tick > 0:
            self.damage(self.damage_on_tick)