COLORS = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF",
    "BLUEVIOLET": "#8A2BE2"
}
while True:
    print("ALICEBLUE, ANTIQUE, AQUA, AZURE, BEIGE, BISQUE, BALCK, BLANCHEDALMOND, BLUE, BLUEVIOLET")
    color_name = input("Enter a color name: ").strip().upper()
    if not color_name:
        break
    if color_name in COLORS:
        print(f"The hexadecimal code for {color_name} is {COLORS[color_name]}")
    else:
        print(f"Invalid color name: {color_name}")
