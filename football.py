from tabulate import tabulate

def generate_fixtures_table(teams):
    num_teams = len(teams)
    fixtures_table = []

    # Create two copies of team list first and second legs
    first_leg = teams[:]
    second_leg = teams[:]

    # Schedule matches for each team against all other teams, both at home and away
    for _ in range(num_teams - 1):
        for i in range(num_teams // 2):
            home_team = first_leg[i]
            away_team = first_leg[num_teams - i - 1]

            # Skip scheduling the match if home team and away team are the same
            if home_team != away_team:
                fixture = [home_team, 'Home', 'vs', away_team, 'Away', 'Stadium', '1']
                fixtures_table.append(fixture)

            home_team = second_leg[num_teams - i - 1]
            away_team = second_leg[i]

            # Skip scheduling the match if home team and away team are the same
            if home_team != away_team:
                fixture = [home_team, 'Home', 'vs', away_team, 'Away', 'Stadium', '2']
                fixtures_table.append(fixture)

        # Rotate teams for the next round
        first_leg.insert(1, second_leg.pop())
        second_leg.insert(0, first_leg.pop(1))

    return fixtures_table

# List of teams participating in the tournament
teams = [
    'Cklein Stars',
    'Wolves FC',
    'Dolphins FC',
    'Sea Horses FC',
    'Sharks United',
    'Lake Basin FC',
    'Thika United',
    'Mavuno Comrades FC',
    'Nakuru FC',
    'Ostrich Associates'
]

# Generate the fixtures table
fixtures_table = generate_fixtures_table(teams)

# Print the fixtures table using the tabulate library for better formatting
headers = ['Home', 'City', 'vs', 'Away', 'City', 'Stadium', 'Leg']
print(tabulate(fixtures_table, headers=headers))
