
class Team():

    def __init__(self, number : int):
        self.team_number = number
        self.matches = []
        self.team_key = "frc" + str(number)
    
    def add_match(self, match):
        self.matches.append(match)
    