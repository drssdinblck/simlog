class Style:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    NOCOL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def in_blue(text: str) -> str:
    return in_color(Style.BLUE, text)


def in_cyan(text: str) -> str:
    return in_color(Style.CYAN, text)


def in_green(text: str) -> str:
    return in_color(Style.GREEN, text)


def in_orange(text: str) -> str:
    return in_color(Style.ORANGE, text)


def in_red(text: str) -> str:
    return in_color(Style.RED, text)


def in_color(color_escape: str, text: str) -> str:
    return f'{color_escape}{text}{Style.NOCOL}'
