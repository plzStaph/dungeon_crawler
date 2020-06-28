from pygame import Surface, display
from pygame.event import Event

from screens.start import StartScreen
from screens.sandbox import SandboxScreen
from screens.level import LevelScreen

from utils.localization import LOCALIZATION
from utils.config import CONFIG
from utils.colors import LIGHT

class ScreenManager:
    "Screen Manager class."

    def __init__(self):
        self.__display_surf = None
        self.__screens = {}
        self.__active = ""

    def activeScreen(self):
        return self.__screens.get(self.__active)

    def changeScreen(self, screen: str) -> None:
        self.__active = screen
        self.activeScreen().on_init()

    def on_init(self) -> None:
        display.set_caption(LOCALIZATION.game_title)
        
        self.__display_surf = display.set_mode(
            CONFIG.get_screen_size(),
            CONFIG.get_screen_flags()
        )
        self.__screens = {
            "start"   : StartScreen().with_manager(self),
            "sandbox" : SandboxScreen().with_manager(self),
            "level"   : LevelScreen().with_manager(self)
        }
        self.__active = "start"
        self.activeScreen().on_init()

    def on_event(self, event: Event) -> None:
        self.activeScreen().on_event(event)

    def on_update(self) -> None:
        self.activeScreen().on_update()

    def on_render(self) -> None:
        self.__display_surf.fill(LIGHT)
        self.activeScreen().on_render(self.__display_surf)
        display.update()

    def on_quit(self) -> None:
        self.activeScreen().on_quit()

SCREEN_MANAGER = ScreenManager()