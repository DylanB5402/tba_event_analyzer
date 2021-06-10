import requests
import auth_token
import json
from team import Team
from match_data import MatchData

def get_data(data : str):
    # tba auth token is in an auth_token.py file, which has been gitignored
    header = { 'X-TBA-Auth-Key' : auth_token.token}
    tba_url = "https://www.thebluealliance.com/api/v3"
    response = requests.get(tba_url + data, headers=header)
    tba_data = json.loads(response.content)
    return tba_data

class EventAnaylzer():

    def __init__(self, event_key : str):
        self.event_key = event_key        
        self.teams = {}
        self.raw_teams = []
        self.matches = []

    def gather_teams(self):
        self.raw_teams = get_data("/event/" + self.event_key + "/teams")
        for team in self.raw_teams:
            self.teams.update({team["key"] : Team(team["team_number"])})

    def gather_matches(self):
        self.matches = get_data("/event/" + self.event_key + "/matches")
        for match in self.matches:
            if (match["comp_level"] == "qm"):
                match_data = MatchData(match)
                for team in (match_data.red_teams + match_data.blue_teams):
                    self.teams[team].add_match(match_data)
