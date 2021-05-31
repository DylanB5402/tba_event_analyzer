import requests
import auth_token
import json
from team import Team

def get_data(data : str):
    # tba auth token is in an auth_token.py file, which has been gitignored
    header = { 'X-TBA-Auth-Key' : auth_token.token}
    tba_url = "https://www.thebluealliance.com/api/v3"
    response = requests.get(tba_url + data, headers=header)
    tba_data = json.loads(response.content)
    # data = data.replace("/", "_")
    # try:
    #     output_file = open(data + ".json", "w")
    #     print("file DNE   ")
    # except:
    #     output_file = open(data + ".json", "x")
    # json.dump(tba_data, output_file )
    return tba_data

class EventAnaylzer():

    def __init__(self, event_key : str):
        self.event_key = event_key        
        self.teams = {}
        self.raw_teams = []
        self.matches = []

    def analyze_teams(self):
        self.raw_teams = get_data("/event/" + self.event_key + "/teams")
        for team in self.raw_teams:
            # self.teams.append(Team(team["team_number"]))
            self.teams.update({team["key"] : Team(team["team_number"])})
            # print(team["team_number"])

    def analyze_matches(self):
        self.matches = get_data("/event/" + self.event_key + "/matches")
        # for match in self.matches:
        #     if (match["comp_level"] == "qm"):
        #         pass
        match = self.matches[0]
        print(match)
                


ev = EventAnaylzer("2020cala")
ev.analyze_teams()
ev.analyze_matches()



