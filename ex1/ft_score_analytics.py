import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    my_list = []
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            my_list.append(score)
        except ValueError:
            print(
                f"Invalid score '{arg}' skipped. Please provide integer"
                "values only."
            )
    if my_list:
        print("Scores processed:", my_list)
        print(f"Total players: {len(my_list)}")
        print(f"Total score: {sum(my_list)}")
        print(f"Average score: {sum(my_list) / len(my_list):.1f}")
        print(f"High score: {max(my_list)}")
        print(f"Low score: {min(my_list)}")
        print(f"Score range: {max(my_list) - min(my_list)}")
    else:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py"
            "<score1> <score2> ..."
        )
