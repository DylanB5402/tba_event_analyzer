import requests
import auth
import json
from team import Team

def get_data(data : str):
    header = { 'X-TBA-Auth-Key' : auth.token}
    tba_url = "https://www.thebluealliance.com/api/v3"
    response = requests.get(tba_url + data, headers=header)
    tba_data = json.loads(response.content)
    data = data.replace("/", "_")
    try:
        output_file = open(data + ".json", "w")
    except:
        output_file = open(data + ".json", "x")
    # print(type())
    json.dump(response.content, output_file )
    return tba_data

class EventAnaylzer():

    def __init__(self, event_key : str):
        self.event_key = event_key        
        self.teams = []
        self.raw_teams = []
        self.matches = []

    def load_date(self):
        # self.raw_teams = get_data("/event/" + self.event_key + "/teams")
        pass

    def analyze_teams(self):
        self.raw_teams = get_data("/event/" + self.event_key + "/teams")
        for team in self.raw_teams:
            # print(team["team_number"])
            self.teams.append(Team(team["team_number"]))
        # print(type(self.raw_teams))

    def analyze_matches(self):
        self.matches = get_data("/event/" + self.event_key + "/matches")
        for match in self.matches:
            if (match["comp_level"] == "qm"):
                # print(match["match_number"])
                print(match)
        print(type(self.matches))
                

# print(get_data("/event/2020cala"))
# data_point = get_data("/event/2020cala/matches/keys")
# print(data_point)
# for x in data_point:    
    # print(x)

ev = EventAnaylzer("2020cala")
ev.analyze_matches()
# ev.analyze_teams()


