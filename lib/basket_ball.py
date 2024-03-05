def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },

        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

class Player:
    def __init__(self, name, number, position, points_per_game, rebounds_per_game, assists_per_game, steals_per_game, blocks_per_game, career_points, age, height_inches, shoe_brand):
        self.name = name
        self.number = number
        self.position = position
        self.points_per_game = points_per_game
        self.rebounds_per_game = rebounds_per_game
        self.assists_per_game = assists_per_game
        self.steals_per_game = steals_per_game
        self.blocks_per_game = blocks_per_game
        self.career_points = career_points
        self.age = age
        self.height_inches = height_inches
        self.shoe_brand = shoe_brand


players = [
    Player("Jarrett Allen", 31, "Center", 16.1, 10.8, 1.6, 0.8, 1.3, 3945, 24, 82, "Nike"),
    Player("Darius Garland", 10, "Point Guard", 21.7, 3.3, 8.6, 1.3, 0.1, 3142, 22, 73, "Nike"),
    Player("Evan Mobley", 4, "Center", 15.0, 8.3, 2.5, 0.8, 1.7, 1034, 21, 83, "Adidas"),
    Player("Kevin Love", 0, "Power Forward", 13.6, 7.2, 2.2, 0.4, 0.2, 14305, 34, 80, "Nike"),
    Player("Isaac Okoro", 35, "Small Forward", 8.8, 3.0, 1.8, 0.8, 0.3, 1234, 21, 77, "Nike"),
    Player("Ricky Rubio", 99, "Point Guard", 13.1, 4.1, 6.6, 1.4, 0.2, 7399, 31, 74, "Adidas"),
    Player("Bradley Beal", 3, "Shooting Guard", 23.2, 4.7, 6.6, 0.9, 0.4, 14231, 29, 76, "Nike"),
    Player("Kyle Kuzma", 33, "Power Forward", 17.1, 8.5, 3.5, 0.6, 0.9, 5336, 27, 81, "Puma"),
    Player("Kentavious Caldwell-Pope", 1, "Shooting Guard", 13.2, 3.4, 1.9, 1.1, 0.3, 7911, 29, 77, "Nike"),
    Player("Davis Bertans", 42, "Power Forward", 5.6, 2.1, 0.6, 0.3, 0.3, 3165, 29, 82, "Nike"),
    Player("Kristaps Porzingis", 6, "Power Forward", 22.1, 8.8, 2.9, 0.7, 1.5, 6371, 27, 87, "Adidas"),
    Player("Rui Hachimura", 8, "Power Forward", 11.3, 3.8, 1.1, 0.5, 0.2, 1913, 24, 80, "Jordan"),
]

def num_points_per_game(player_name):
    for player in players:
        if player.name == player_name:
            return player.points_per_game
    return None

def player_age(player_name):
    for player in players:
        if player.name == player_name:
            return player.age
    return None

def team_colors(team_name):
    if team_name == "Cleveland Cavaliers":
        return ["Wine", "Gold"]
    elif team_name == "Washington Wizards":
        return ["Red", "White", "Navy Blue"]
    return None

def team_names():
    return ["Cleveland Cavaliers", "Washington Wizards"]

def player_numbers(team_name):
    if team_name == "Cleveland Cavaliers":
        return [player.number for player in players if player.name in ["Jarrett Allen", "Darius Garland", "Evan Mobley", "Kevin Love", "Isaac Okoro", "Ricky Rubio"]]
    elif team_name == "Washington Wizards":
        return [player.number for player in players if player.name in ["Bradley Beal", "Kyle Kuzma", "Kentavious Caldwell-Pope", "Davis Bertans", "Kristaps Porzingis", "Rui Hachimura"]]
    return None

def player_stats(player_name):
    for player in players:
        if player.name == player_name:
            return {
                "name": player.name,
                "number": player.number,
                "position": player.position,
                "points_per_game": player.points_per_game,
                "rebounds_per_game": player.rebounds_per_game,
                "assists_per_game": player.assists_per_game,
                "steals_per_game": player.steals_per_game,
                "blocks_per_game": player.blocks_per_game,
                "career_points": player.career_points,
                "age": player.age,
                "height_inches": player.height_inches,
                "shoe_brand": player.shoe_brand,
            }
    return None


def average_rebounds_by_shoe_brand():
    shoe_brand_rebounds = {}
    shoe_brand_count = {}

    for player in players:
        shoe_brand = player.shoe_brand
        rebounds = player.rebounds_per_game

        if shoe_brand in shoe_brand_rebounds:
            shoe_brand_rebounds[shoe_brand] += rebounds
            shoe_brand_count[shoe_brand] += 1
        else:
            shoe_brand_rebounds[shoe_brand] = rebounds
            shoe_brand_count[shoe_brand] = 1

    for brand, rebounds in shoe_brand_rebounds.items():
        count = shoe_brand_count[brand]
        average_rebounds = rebounds / count
        print(f"{brand}: {average_rebounds:.2f}")
