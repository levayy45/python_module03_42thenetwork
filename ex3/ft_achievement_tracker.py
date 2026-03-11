if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()

    alice = set(["first_kill", "first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(
        ["level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist"]
        )

    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)
    print()

    print("=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print("All unique achievements:", all_achievements)
    print("Total unique achievements:", len(all_achievements))
    print()

    common_all = alice.intersection(bob).intersection(charlie)
    print("Common to all players:", common_all)

    rare = set()
    for achievement in all_achievements:
        count = 0
        if achievement in alice:
            count = count + 1
        if achievement in bob:
            count = count + 1
        if achievement in charlie:
            count = count + 1
        if count == 1:
            rare = rare.union(set([achievement]))
    print("Rare achievements (1 player):", rare)
    print()

    alice_bob_common = alice.intersection(bob)
    alice_only = alice.difference(bob)
    bob_only = bob.difference(alice)

    print("Alice vs Bob common:", alice_bob_common)
    print("Alice unique:", alice_only)
    print("Bob unique:", bob_only)
