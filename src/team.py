class Team:
    def __init__(self, team_name, players, coach):
        self.name = team_name
        self.players = players
        self.coach = coach

    def add_player(self, player):
        self.players.append(player)