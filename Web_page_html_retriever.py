import requests
import pandas as pd


r = requests.get('http://www.reddit.com/r/nba/top/.json?t=month&limit=3')

stuff = r.json()

entries = stuff['data']['children']

post_ids = []

for i in entries:
	post_ids.append(str(i['data']['id']))
	
print post_ids

idtable = pd.DataFrame(post_ids, columns = ['Post IDs'])


idtable.to_csv('id_table.csv')

print idtable
