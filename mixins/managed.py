class Managed:
    """Managed class. Keeps a reference to a manager instance."""

    def __init__(self):
        self.manager = None

    def with_manager(self, manager: object) -> object:
        """Set manager and return self."""
        self.manager = manager
        return self