class Player:
    def __init__(self, name="", age=0, position="", team=""):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Forward",
        "team": "Philadelphia 76ers"
    },
    {
        "name": "",
        "age": 16,
        "position": "P",
        "team": "en"
    }
]
players_list = [Player(**player_info) for player_info in players]
