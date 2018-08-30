HEX_COLORS = {"aliceblue": "#fof8ff", "antiquewhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "	#f0ffff",
              "beige": "#f5f5dc", "bisque1": "#ffe4c4", "black": "#000000", "blanchedalmond": "	#ffebcd", "blue1":
                  "#0000ff"}

color_name = input("Enter Colour Name:").lower()

while color_name != "":
    if color_name in HEX_COLORS:
        print(color_name, "is", HEX_COLORS[color_name])
    else:
        print("Invalid Colour Name")
    color_name = input("Enter Colour Name:").lower()
