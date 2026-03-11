import sys


def ft_sum(values: dict.values) -> int:
    total: int = 0
    for v in values:
        total += v
    return total


def ft_max(dct: dict) -> str:
    best_key: str | None = None
    for key in dct:
        if best_key is None or dct[key] > dct[best_key]:
            best_key = key
    return best_key


def ft_min(dct: dict) -> str:
    best_key: str | None = None
    for key in dct:
        if best_key is None or dct[key] < dct[best_key]:
            best_key = key
    return best_key


def ft_split(s: str, sep: str) -> list:
    parts: list = []
    current: str = ""
    for char in s:
        if char == sep:
            parts.append(current)
            current = ""
        else:
            current += char
    parts.append(current)
    return parts


def ft_int(s: str) -> int:
    digits: dict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }

    result: int = 0
    negative: bool = False

    it: str = s
    if len(s) > 0 and s[0] == '-':
        negative = True
        it = s[1:]

    for c in it:
        if c not in digits:
            raise ValueError(f"invalid literal: {s}")
        result = result * 10 + digits[c]

    if negative:
        result = -result

    return result


if __name__ == "__main__":
    inventory: dict = dict()

    if len(sys.argv) < 2:
        print("No inventory provided.")
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
        sys.exit()

    for arg in sys.argv[1:]:
        try:
            parts: list = ft_split(arg, ":")
            if len(parts) != 2:
                print(
                    f"Invalid format '{arg}' skipped. Expected item:quantity"
                    )
                continue
            item: str = parts[0]
            if item == "":
                print(
                    f"Invalid format '{arg}' skipped. "
                    "Item name cannot be empty.")
                continue
            quantity: int = ft_int(parts[1])
            if quantity < 0:
                print(f"Invalid quantity for '{item}' "
                      "skipped. Quantity must be positive.")
                continue
            inventory.update({item: quantity})
        except ValueError:
            print(
                f"Invalid quantity in '{arg}' skipped. "
                "Quantity must be an integer.")
            continue

    if len(inventory) == 0:
        print("No valid inventory items to process.")
        sys.exit()

    print("=== Inventory System Analysis ===")
    total_items: int = ft_sum(inventory.values())
    unique_types: int = len(inventory.keys())
    print("Total items in inventory:", total_items)
    print("Unique item types:", unique_types)
    print()

    print("=== Current Inventory ===")
    temp_inv: dict = dict()
    for k, v in inventory.items():
        temp_inv.update({k: v})

    while len(temp_inv) > 0:
        highest_qty: int = -1
        best_item: str = ""

        for item, qty in temp_inv.items():
            if qty > highest_qty:
                highest_qty = qty
                best_item = item

        try:
            percentage: float = (highest_qty / total_items) * 100
            unit_word: str = "units" if highest_qty > 1 else "unit"
            print(
                f"{best_item}: {highest_qty} {unit_word} ({percentage:.1f}%)"
                )
        except ZeroDivisionError:
            print(f"{best_item}: {highest_qty} unit (0.0%)")

        new_temp: dict = dict()
        for item, qty in temp_inv.items():
            if item != best_item:
                new_temp.update({item: qty})

        temp_inv = new_temp
    print()

    print("=== Inventory Statistics ===")
    most_item: str = ft_max(inventory)
    least_item: str = ft_min(inventory)
    most_qty: int = inventory.get(most_item)
    least_qty: int = inventory.get(least_item)
    most_unit: str = "units" if most_qty > 1 else "unit"
    least_unit: str = "units" if least_qty > 1 else "unit"
    print(f"Most abundant: {most_item} ({most_qty} {most_unit})")
    print(f"Least abundant: {least_item} ({least_qty} {least_unit})")
    print()

    abundant: dict = dict()
    moderate: dict = dict()
    scarce: dict = dict()

    for item, qty in inventory.items():
        if qty >= 10:
            abundant.update({item: qty})
        elif qty >= 4:
            moderate.update({item: qty})
        else:
            scarce.update({item: qty})

    print("=== Item Categories ===")
    if len(abundant) > 0:
        print("Abundant:", abundant)
    if len(moderate) > 0:
        print("Moderate:", moderate)
    if len(scarce) > 0:
        print("Scarce:", scarce)
    print()

    print("=== Management Suggestions ===")
    restock: list = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock += [item]
    if len(restock) > 0:
        print("Restock needed:", end=" ")
        print(*restock, sep=", ")
    else:
        print("All items sufficiently stocked.")
    print()

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", end=" ")
    print(*inventory.keys(), sep=", ")
    print("Dictionary values:", end=" ")
    print(*inventory.values(), sep=", ")
    print(
        "Sample lookup - 'sword' in inventory:",
        inventory.get("sword") is not None
            )
