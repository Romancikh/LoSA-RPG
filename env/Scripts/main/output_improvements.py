from colorama import Fore, init
init()


def black(output: str) -> str:
    return Fore.BLACK + output + Fore.RESET


def red(output: str) -> str:
    return Fore.RED + output + Fore.RESET


def green(output: str) -> str:
    return Fore.GREEN + output + Fore.RESET


def yellow(output: str) -> str:
    return Fore.YELLOW + output + Fore.RESET


def blue(output: str) -> str:
    return Fore.BLUE + output + Fore.RESET


def magenta(output: str) -> str:
    return Fore.MAGENTA + output + Fore.RESET


def cyan(output: str) -> str:
    return Fore.CYAN + output + Fore.RESET


def white(output: str) -> str:
    return Fore.WHITE + output + Fore.RESET


def clear():
    from os import system
    system("cls")


def print_outline(clean_up: bool = False):
    def outer(func):
        def wrapper(*args, **kwargs):
            if clean_up:
                clear()
            print("="*30)
            result = func(*args)
            print("="*30)
            return result
        return wrapper
    return outer
