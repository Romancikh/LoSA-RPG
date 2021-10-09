from colorama import Fore, init
init()


def red(output: str) -> str:
    return Fore.RED + output + Fore.RESET


def green(output: str) -> str:
    return Fore.GREEN + output + Fore.RESET


def yellow(output: str) -> str:
    return Fore.YELLOW + output + Fore.RESET


def blue(output: str) -> str:
    return Fore.BLUE + output + Fore.RESET
