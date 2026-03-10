import sys

if __name__ == "__main__":
    inventory = dict()

    if len(sys.argv) < 2:
        print("No inventory provided.")
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
        sys.exit()

    for arg in sys.argv[1:]:
        try:
            parts = arg.split(":")
            if len(parts) != 2:
                print(
                    f"Invalid format '{arg}' skipped. Expected item:quantity"
                    )
                continue
            item = parts[0]
            if item == "":
                print(
                    f"Invalid format '{arg}' skipped. "
                    "Item name cannot be empty.")
                continue
            quantity = int(parts[1])
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
    total_items = sum(inventory.values())
    unique_types = len(inventory.keys())
    print("Total items in inventory:", total_items)
    print("Unique item types:", unique_types)
    print()

    sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)

    print("=== Current Inventory ===")
    for item, qty in sorted_items:
        percentage = round((qty / total_items) * 100, 1)
        unit_word = "units" if qty > 1 else "unit"
        print(f"{item}: {qty} {unit_word} ({percentage}%)")
    print()

    print("=== Inventory Statistics ===")
    most_item = max(inventory.keys(), key=lambda x: inventory.get(x))
    least_item = min(inventory.keys(), key=lambda x: inventory.get(x))
    most_qty = inventory.get(most_item)
    least_qty = inventory.get(least_item)
    most_unit = "units" if most_qty > 1 else "unit"
    least_unit = "units" if least_qty > 1 else "unit"
    print(f"Most abundant: {most_item} ({most_qty} {most_unit})")
    print(f"Least abundant: {least_item} ({least_qty} {least_unit})")
    print()

    abundant = dict()
    moderate = dict()
    scarce = dict()

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
    restock = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)
    if len(restock) > 0:
        print("Restock needed:", ", ".join(restock))
    else:
        print("All items sufficiently stocked.")
    print()

    print("=== Dictionary Properties Demo ===")
    keys_list = ", ".join(inventory.keys())
    values_list = ", ".join(str(v) for v in inventory.values())
    print("Dictionary keys:", keys_list)
    print("Dictionary values:", values_list)
    print(
        "Sample lookup - 'sword' in inventory:",
        inventory.get("sword") is not None
            )
