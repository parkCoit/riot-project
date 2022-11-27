

from riotwatcher import LolWatcher
import pandas as pd


api_key = ""
watcher = LolWatcher(api_key)
my_region = "kr"

me = watcher.summoner.by_name(my_region, 'hideonbush')
print(me)
a = pd.DataFrame(me, index=[0])
puuid = me['puuid']
matchid = watcher.match.matchlist_by_puuid(my_region, puuid)



[print(i) for i in matchid]

b = watcher.match.timeline_by_match(my_region, matchid[0])

print(b)




