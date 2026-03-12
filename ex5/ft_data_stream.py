import typing


def game_event_generator(count: int) -> typing.Generator:
    players = ["alice", "bob", "charlie", "diana", "eve"]
    actions = [
        "killed monster", "found treasure",
        "leveled up", "collected item", "defeated boss"
        ]

    for i in range(count):
        player_index = i % len(players)
        action_index = i % len(actions)
        level = (i % 20) + 1
        player = players[player_index]
        action = actions[action_index]
        yield (i + 1, player, level, action)


def fibonacci_generator() -> typing.Generator:
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> typing.Generator:
    num: int = 2
    while True:
        is_prime: bool = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num = num + 1


def take(n: int, gen: typing.Generator) -> list:
    result: list = []
    try:
        for _ in range(n):
            result += [next(gen)]
    except StopIteration:
        pass
    return result


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print()

    event_count: int = 1000
    print(f"Processing {event_count} game events...")
    print()

    stream: typing.Generator = game_event_generator(event_count)

    total_events: int = 0
    high_level_count: int = 0
    treasure_count: int = 0
    levelup_count: int = 0
    first_three: list = []

    for event_id, player, level, action in stream:
        total_events = total_events + 1

        if len(first_three) < 3:
            first_three += [(event_id, player, level, action)]

        if level >= 10:
            high_level_count = high_level_count + 1
        if action == "found treasure":
            treasure_count = treasure_count + 1
        if action == "leveled up":
            levelup_count = levelup_count + 1

    for event_id, player, level, action in first_three:
        print(f"Event {event_id}: Player {player} (level {level}) {action}")
    print("...")
    print()

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print()
    print("Memory usage: Constant (streaming)")
    print()

    print("=== Generator Demonstration ===")

    fib_gen: typing.Generator = fibonacci_generator()
    fib_values: list = take(10, fib_gen)
    print("Fibonacci sequence (first 10):", end=" ")
    print(*fib_values, sep=", ")

    prime_gen: typing.Generator = prime_generator()
    prime_values: list = take(5, prime_gen)
    print("Prime numbers (first 5):", end=" ")
    print(*prime_values, sep=", ")
