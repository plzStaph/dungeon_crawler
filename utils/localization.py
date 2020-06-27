from utils.jsonHandler import loadFromJson
from utils.config import CONFIG

class Localization:
    """Localization class. Interacts with Localization.json file."""

    def on_init(self) -> None:
        """Load text from localization file."""
        loadFromJson(self, f'assets/localization/{CONFIG.localization}.json')

LOCALIZATION = Localization()