from game import *


def start():
    game = Game()
    game.read_saves()
    game.character_selection()
    game.print_storyline()
    input()
    while True:
        game.action_selection()


if __name__ == "__main__":
    start()
