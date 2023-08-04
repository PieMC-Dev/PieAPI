class Terminal:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    @staticmethod
    def color(text, color_code):
        return f"{color_code}{text}{Terminal.RESET}"

    @staticmethod
    def style(text, style_code):
        return f"{style_code}{text}{Terminal.RESET}"

    # Colors
    @staticmethod
    def black(text):
        return Terminal.color(text, Terminal.BLACK)

    @staticmethod
    def red(text):
        return Terminal.color(text, Terminal.RED)

    @staticmethod
    def green(text):
        return Terminal.color(text, Terminal.GREEN)

    @staticmethod
    def yellow(text):
        return Terminal.color(text, Terminal.YELLOW)

    @staticmethod
    def blue(text):
        return Terminal.color(text, Terminal.BLUE)

    @staticmethod
    def magenta(text):
        return Terminal.color(text, Terminal.MAGENTA)

    @staticmethod
    def cyan(text):
        return Terminal.color(text, Terminal.CYAN)

    @staticmethod
    def white(text):
        return Terminal.color(text, Terminal.WHITE)

    # Styles
    @staticmethod
    def bold(text):
        return Terminal.style(text, Terminal.BOLD)

    @staticmethod
    def underline(text):
        return Terminal.style(text, Terminal.UNDERLINE)
