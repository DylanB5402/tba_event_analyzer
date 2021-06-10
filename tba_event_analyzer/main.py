import requests
import auth_token
import json

import event_analyzer
from team import Team
from match_data import MatchData
from event_analyzer import EventAnaylzer


                
ev = EventAnaylzer("2020cala")
ev.gather_teams()
ev.gather_matches()
# print(ev.teams["frc687"].matches, len(ev.teams["frc687"].matches))
for (x) in ev.teams.keys():
    print(x, len(ev.teams[x].matches))
# print(len(ev.teams.keys()))
# print(len(ev.teams))

# md = MatchData(event_analyzer.get_data("/match/2020cala_qm1"))
# print(md.data)
# print(json.dumps(md.data, indent=2))


