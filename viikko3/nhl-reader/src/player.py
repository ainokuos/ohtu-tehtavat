class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20}{self.team} {self.goals} + {self.assists} = {self.points}"
