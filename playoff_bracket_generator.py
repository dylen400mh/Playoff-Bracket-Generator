def get_number_of_teams():
    while True:
        number_of_teams = input("Enter the number of teams in the league: ")
        if not number_of_teams.isdigit():
            print("Input must be a valid integer. Please try again.")
            continue
        number_of_teams = int(number_of_teams)
        if number_of_teams >= 2:
            break
        print("The minimum number of teams is 2. Please try again.")
    return number_of_teams


def get_names_of_teams(number_of_teams):
    names_of_teams = []

    for team in range(number_of_teams):
        while True:
            team_name = input(
                f"Enter the name for team #{len(names_of_teams) + 1}: ")
            if len(team_name.split(" ")) > 2:
                print("Team names cannot have more than two words. Please try again.")
            elif len(team_name) < 2:
                print("Team names must have at least two characters. Please try again.")
            else:
                names_of_teams.append(team_name)
                break
    return names_of_teams


def get_number_of_games_played(number_of_teams):
    while True:
        number_of_games_played = input(
            "Enter the number of games played by each team: ")
        if not number_of_games_played.isdigit():
            print("Input must be a valid integer. Please try again.")
            continue
        number_of_games_played = int(number_of_games_played)
        if number_of_games_played >= number_of_teams - 1:
            break
        print("Invalid number of games. Each team plays each other at least once in the regular season. Please try again.")
    return number_of_games_played


def get_number_of_wins(names_of_teams, number_of_games_played):
    number_of_wins = []

    for team in names_of_teams:
        while True:
            wins = input(f"Enter the number of wins Team {team} had: ")
            if not wins.isdigit():
                print("Input must be a valid integer. Please try again.")
                continue
            wins = int(wins)
            if wins < 0:
                print("The minimum number of wins is 0. Please try again.")
            elif wins > number_of_games_played:
                print(
                    f"The maximum number of wins is {number_of_games_played}. Please try again.")
            else:
                number_of_wins.append([team, wins])
                break
    return number_of_wins


number_of_teams = get_number_of_teams()
names_of_teams = get_names_of_teams(number_of_teams)
number_of_games_played = get_number_of_games_played(number_of_teams)
number_of_wins = get_number_of_wins(names_of_teams, number_of_games_played)

sorted_teams = sorted(number_of_wins, key=lambda x: x[1])

print("Generating the games to be played in the first round of the tournament...")

if number_of_teams % 2 != 0:
    bye = sorted_teams[-1][0]
    sorted_teams.pop()
    print(f"Bye: {bye}")

for match in range(number_of_teams//2):
    home_team = sorted_teams[0][0]
    away_team = sorted_teams[-1][0]
    sorted_teams.remove(sorted_teams[0])
    sorted_teams.pop()
    print(f"Home: {home_team} VS Away: {away_team}")
