from score_breakdown import ScoreBreakdown

class MatchData():

    def __init__(self, data_json):
        self.data = data_json
        self.red_teams = []
        self.blue_teams = []
        self.match_key = self.data["key"]
        self.process_data()
        pass

    def process_data(self):
        self.red_teams = self.data["alliances"]["red"]["team_keys"]
        self.blue_teams = self.data["alliances"]["blue"]["team_keys"]
        self.red_score_breakdown = ScoreBreakdown(self.data["score_breakdown"]["red"])
        self.blue_score_breakdown = ScoreBreakdown(self.data["score_breakdown"]["blue"])
        
        

