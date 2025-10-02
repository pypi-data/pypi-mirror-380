# PyAnsiWrap 🎨
A simple, zero-dependency Python class for adding color and style to your terminal text.

Ansiwrap provides a clean, fluent API to make your command-line applications more readable and visually appealing. It works on any terminal that supports ANSI escape codes (like most Linux, macOS, and modern Windows terminals).

# Key Features
1. Zero Dependencies: Pure Python, no external packages needed.
2. Simple API: An intuitive, easy-to-learn set of static methods.
3. Flexible Styling: Supports foreground/background colors, bold, underline, reverse, and more.
4. Case-Insensitive: Color names can be red, RED, or Red.
5. Global Control: Easily enable or disable all styling with a single command.
6. Pipe-Aware: Automatically disables color when output is redirected to a file.

# Installation
Install Ansiwrap directly from pip:
```Bash
pip install pyansiwrap
```

# Quick Start
Ansiwrap is designed to be straightforward. You can style a specific piece of text or apply a style to a whole block.

## Styling a single string
This is the most common use case. The style is automatically applied and reset.
```Python
from pyansiwrap import Ansiwrap

# --- Foreground Colors ---
print("Status:", Ansiwrap.fg("green", "SUCCESS", bold=True))
print("Error:", Ansiwrap.fg("red", "File not found."))

# --- Background Colors ---
print(Ansiwrap.bg("yellow", Ansiwrap.fg("black", " WARNING ")))

# --- Other Styles ---
print("Task:", Ansiwrap.strikethrough("Review documents"), "(Complete)")
print("Selection:", Ansiwrap.reverse(" Menu Item 1 "))
```

## Styling a block of text
Use the ```start_*``` methods to begin a style and ```reset()``` to end it.
```Python
from pyansiwrap import Ansiwrap

# Combine start codes by adding them together
print(Ansiwrap.start_fg("cyan") + Ansiwrap.start_underline(), end="")

print("System Log")
print("----------")
print("All systems are operating normally.")

# Return to the default terminal style
print(Ansiwrap.reset(), "Log finished.")
```
# API Reference
All methods are static and can be called directly on the ```Ansiwrap``` class.

## Wrapper methods
These methods style a specific ```text``` string and automatically append a reset code.

- ```Ansiwrap.fg(color_name, text, bold=False)```: Styles foreground color.
- ```Ansiwrap.bg(color_name, text)```: Styles background color.
- ```Ansiwrap.underline(text)```
- ```Ansiwrap.reverse(text)```
- ```Ansiwrap.conceal(text)```
- ```Ansiwrap.strikethrough(text)```

## Starter methods
These methods return only the opening ANSI code to start a persistent style.

- ```Ansiwrap.start_fg(color_name, bold=False)```
- ```Ansiwrap.start_bg(color_name)```
- ```Ansiwrap.start_underline()```
- ```Ansiwrap.start_reverse()```
- ```Ansiwrap.start_conceal()```
- ```Ansiwrap.start_strikethrough()```

## Global controls
- ```Ansiwrap.enable()```: Globally enables all styling.
- ```Ansiwrap.disable()```: Globally disables all styling.
- ```Ansiwrap.reset()```: Returns the code to reset all active styles.

# Cross platform support
Ansiwrap works out-of-the-box on modern terminals. For compatibility with the legacy Windows ```cmd.exe```, you can use it alongside the ```colorama``` library.

Initialize ```colorama``` at the start of your script to get the best of both worlds: ```colorama```'s robust Windows support and ```Ansiwrap```'s clean API.

```Python
import colorama
from pyansiwrap import Ansiwrap

# Let colorama handle Windows compatibility
colorama.init()

# Now use Ansiwrap's API as usual
print(Ansiwrap.fg("magenta", "This will work everywhere!"))
```