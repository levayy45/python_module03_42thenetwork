import math

if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    position = tuple((10, 20, 5))
    print()
    print("Position created:", position)

    origin = (0, 0, 0)
    x1, y1, z1 = origin
    x2, y2, z2 = position
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between {origin} and {position}: {distance:.2f}")

    coord_string = "3,4,0"
    print()
    print(f'Parsing coordinates: "{coord_string}"')
    try:
        parts = coord_string.split(",")
        parsed = tuple((int(parts[0]), int(parts[1]), int(parts[2])))
        print("Parsed position:", parsed)
        px, py, pz = parsed
        ox, oy, oz = origin
        d = math.sqrt((px - ox) ** 2 + (py - oy) ** 2 + (pz - oz) ** 2)
        print(f"Distance between {origin} and {parsed}: {float(d)}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args},")

    invalid_string = "abc,def,ghi"
    print()
    print(f'Parsing invalid coordinates: "{invalid_string}"')
    try:
        parts = invalid_string.split(",")
        parsed_invalid = tuple((int(parts[0]), int(parts[1]), int(parts[2])))
        print("Parsed position:", parsed_invalid)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {ValueError.__name__}, Args: {e.args}")

    print()
    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    X, Y, Z = tuple((x, y, z))
    print(f"Coordinates: X={X}, Y={Y}, Z={Z}")
