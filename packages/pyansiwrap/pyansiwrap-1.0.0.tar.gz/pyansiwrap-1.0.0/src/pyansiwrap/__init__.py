import sys

class Ansiwrap:
    """
    A utility class for adding ANSI color and style codes to terminal text.
    Includes reverse, conceal, and other text styling functions.
    """
    
    RESET = "\u001b[0m"
    STYLES = {"bold": 1, "underline": 4, "reverse": 7, "strikethrough": 9}
    FG_COLORS = {"black": 30, "red": 31, "green": 32, "yellow": 33, "blue": 34, "magenta": 35, "cyan": 36, "white": 37}
    BG_COLORS = {"black": 40, "red": 41, "green": 42, "yellow": 43, "blue": 44, "magenta": 45, "cyan": 46, "white": 47}
    
    enabled = True

    @classmethod
    def enable(cls):
        """Globally enable color and style output."""
        cls.enabled = True

    @classmethod
    def disable(cls):
        """Globally disable color and style output."""
        cls.enabled = False

    @staticmethod
    def _generate_code(*codes: int) -> str:
        """Internal helper to generate the ANSI code string part."""
        if not Ansiwrap.enabled or not sys.stdout.isatty():
            return ""
        code_str = ";".join(map(str, codes))
        return f"\u001b[{code_str}m"

    @staticmethod
    def fg(color_name: str, text: str, bold: bool = False) -> str:
        """Applies a foreground color to a string and resets it."""
        color_name = color_name.lower()
        if color_name not in Ansiwrap.FG_COLORS: return text
        codes = [Ansiwrap.FG_COLORS[color_name]]
        if bold: codes.append(Ansiwrap.STYLES["bold"])
        start_code = Ansiwrap._generate_code(*codes)
        return f"{start_code}{text}{Ansiwrap.RESET}" if start_code else text

    @staticmethod
    def bg(color_name: str, text: str) -> str:
        """Applies a background color to a string and resets it."""
        color_name = color_name.lower()
        if color_name not in Ansiwrap.BG_COLORS: return text
        start_code = Ansiwrap._generate_code(Ansiwrap.BG_COLORS[color_name])
        return f"{start_code}{text}{Ansiwrap.RESET}" if start_code else text

    @staticmethod
    def underline(text: str) -> str:
        """Applies underline style to a string and resets it."""
        start_code = Ansiwrap._generate_code(Ansiwrap.STYLES["underline"])
        return f"{start_code}{text}{Ansiwrap.RESET}" if start_code else text

    @staticmethod
    def reverse(text: str) -> str:
        """Applies reverse video style to a string and resets it."""
        start_code = Ansiwrap._generate_code(Ansiwrap.STYLES["reverse"])
        return f"{start_code}{text}{Ansiwrap.RESET}" if start_code else text
    
    @staticmethod
    def strikethrough(text: str) -> str:
        """Applies strikethrough style to a string and resets it."""
        start_code = Ansiwrap._generate_code(Ansiwrap.STYLES["strikethrough"])
        return f"{start_code}{text}{Ansiwrap.RESET}" if start_code else text

    @staticmethod
    def start_fg(color_name: str, bold: bool = False) -> str:
        """Returns the start code for a foreground color."""
        color_name = color_name.lower()
        if color_name not in Ansiwrap.FG_COLORS: return ""
        codes = [Ansiwrap.FG_COLORS[color_name]]
        if bold: codes.append(Ansiwrap.STYLES["bold"])
        return Ansiwrap._generate_code(*codes)

    @staticmethod
    def start_bg(color_name: str) -> str:
        """Returns the start code for a background color."""
        color_name = color_name.lower()
        if color_name not in Ansiwrap.BG_COLORS: return ""
        return Ansiwrap._generate_code(Ansiwrap.BG_COLORS[color_name])
        
    @staticmethod
    def start_underline() -> str:
        """Returns the start code for underline style."""
        return Ansiwrap._generate_code(Ansiwrap.STYLES["underline"])

    @staticmethod
    def start_reverse() -> str:
        """Returns the start code for reverse video style."""
        return Ansiwrap._generate_code(Ansiwrap.STYLES["reverse"])
    
    @staticmethod
    def start_strikethrough() -> str:
        """Returns the start code for strikethrough style."""
        return Ansiwrap._generate_code(Ansiwrap.STYLES["strikethrough"])

    @staticmethod
    def reset() -> str:
        """Returns the code to reset all styles."""
        return Ansiwrap.RESET if Ansiwrap.enabled and sys.stdout.isatty() else ""