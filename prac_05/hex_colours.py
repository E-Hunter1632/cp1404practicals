"""Hex colour dictionary"""

COLOUR_TO_HEX = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff",
                 "alizarincrimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
                 "amethyst": "#9966cc", "antiquewhite": "#faebd7", "apricot": "#fbceb1",
                 "aqua": "#00ffff"}

colour = str(input("Enter a colour to receive the hex equivalent: ")).lower()
while colour != "":
    try:
        print(COLOUR_TO_HEX[colour])
        colour = str(input("Enter a colour to receive the hex equivalent: ")).lower
    except KeyError:
        print("Colour not in dictionary. Enter a different colour.")
        colour = str(input("Enter a colour to receive the hex equivalent: ")).lower()
