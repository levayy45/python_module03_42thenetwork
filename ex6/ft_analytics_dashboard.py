if __name__ == "__main__":
    players_data = [
        {
            "name": "alice",
            "score": 2300,
            "region": "north",
            "active": True,
            "achievements": [
                "first_kill", "level_10", "boss_slayer",
                "speed_demon", "perfectionist"
            ],
        },
        {
            "name": "bob",
            "score": 1800,
            "region": "east",
            "active": True,
            "achievements": ["first_kill", "level_10", "collector"],
        },
        {
            "name": "charlie",
            "score": 2150,
            "region": "central",
            "active": True,
            "achievements": [
                "level_10", "treasure_hunter", "boss_slayer",
                "speed_demon", "perfectionist", "collector", "champion"
            ],
        },
        {
            "name": "diana",
            "score": 2000,
            "region": "north",
            "active": False,
            "achievements": [
                "first_kill", "level_10", "boss_slayer",
                "veteran", "guardian", "tactician", "warrior"
            ],
        },
    ]

    print("=== Game Analytics Dashboard ===")
    print()

    print("=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players_data if p["score"] >= 2000]
    print("High scorers (>2000):", high_scorers)

    scores_doubled = [p["score"] * 2 for p in players_data]
    print("Scores doubled:", scores_doubled)

    active_players = [p["name"] for p in players_data if p["active"]]
    print("Active players:", active_players)
    print()

    print("=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["score"] for p in players_data[:3]}
    print("Player scores:", player_scores)

    score_categories = {
        "high": len([p for p in players_data if p["score"] >= 2000]),
        "medium": len([
            p for p in players_data if 1700 <= p["score"] < 2100
        ]),
        "low": len([p for p in players_data if p["score"] < 1900]),
    }
    print("Score categories:", score_categories)

    achievement_counts = {
        p["name"]: len(p["achievements"])
        for p in players_data
        if p["active"]
    }
    print("Achievement counts:", achievement_counts)
    print()

    print("=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players_data}
    print("Unique players:", unique_players)

    ach_counts = {}
    for p in players_data:
        for ach in p["achievements"]:
            if ach not in ach_counts:
                ach_counts[ach] = 0
            ach_counts[ach] += 1

    unique_achievements = {ach for ach in ach_counts if ach_counts[ach] >= 3}
    print("Unique achievements:", unique_achievements)

    active_regions = {p["region"] for p in players_data if p["active"]}
    print("Active regions:", active_regions)
    print()

    print("=== Combined Analysis ===")

    all_scores = [p["score"] for p in players_data]
    total_players = len(players_data)
    total_unique_achievements = len(ach_counts)
    average_score = sum(all_scores) / len(all_scores) if all_scores else 0

    def get_score(player):
        return player["score"]
    
    top = max(players_data, key=get_score) if players_data else None

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", average_score)
    if top:
        top_ach = len(top["achievements"])
        print(
            f"Top performer: {top['name']} "
            f"({top['score']} points, {top_ach} achievements)"
        )
