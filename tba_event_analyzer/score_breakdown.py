
class ScoreBreakdown():

    def __init__(self, breakdown_json):
        self.breakdown = breakdown_json
        self.total_points = self.breakdown["totalPoints"]
        self.teleop_points = self.breakdown["teleopPoints"]
        self.teleop_cell_points = self.breakdown["teleopCellPoints"]
        self.endgame_points = self.breakdown["endgamePoints"]
        