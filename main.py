import pygame
from pygame import QUIT

from utils.config import CONFIG
from utils.localization import LOCALIZATION
from utils.font import FONT

from screens import SCREEN_MANAGER

class Game:
    "Game class."

    def __init__(self) -> None:
        self.__running = False
        self.__clock = None

    def on_init(self) -> None:
        "Safely initializes pygame modules and game dependencies."

        pygame.init()
        self.__clock = pygame.time.Clock()

        CONFIG.on_init()
        LOCALIZATION.on_init()
        FONT.on_init()
        SCREEN_MANAGER.on_init()

        self.__running = True

    def on_event(self) -> None:
        "Handles events at game level."

        for event in pygame.event.get():
            if event.type == QUIT:
                self.__running = False
            else:
                SCREEN_MANAGER.on_event(event)

    def on_update(self) -> None:
        "Handles updates at game level."

        SCREEN_MANAGER.on_update()

    def on_render(self) -> None:
        "Handles rendering at game level."

        SCREEN_MANAGER.on_render()

    def on_quit(self) -> None:
        "Handles quitting at game level."

        SCREEN_MANAGER.on_quit()
        pygame.quit()

    def _run(self) -> None:
        "Initializes the game, executes the loop and closes the game."

        self.on_init()
        while self.__running:
            self.on_event()
            self.on_update()
            self.on_render()
            self.__clock.tick(CONFIG.fps)
        self.on_quit()

if __name__ == "__main__":
    Game()._run()