import pandas as pd
import math

nbadata = pd.read_csv('nbaprojectdata.csv') # loads data from saved csv

nbadata = nbadata['0'] # eliminates unneeded extra index

counts = nbadata.value_counts() # shows how many of each type are in data set

datalist = nbadata.tolist() #converts to a list for filtering purposes

for i in datalist: # gets rid of counts that are less than 20 (less than 5% of total)
	if datalist.count(i) < 20:
		while datalist.count(i) > 0:
			datalist.remove(i) 

filterlist = ['NBA', 'USA', 'West', 'Charlotte Hornets', '[LAL] Nick Young'] #these tags don't represent current teams

datalist2 = set(datalist)
datalist2 = list(datalist2) # list of all team tags in dataset without duplicates

for i in datalist2: # matches tags in data set with team tags in the filter set, if they match then the filter tag is removed from the data set
	for tag in filterlist:
		if i == tag:
			while datalist.count(i) > 0:
				datalist.remove(i)
		
		else:
			pass
		
		

print len(datalist)

datalist = pd.Series(datalist) #turn into a series object

counts = datalist.value_counts() # returns number of fans for each team

datalist = list(datalist) # back to list object

datalist2 = list(set(datalist)) # list of filtered team tags without duplicates

wins = pd.read_csv('wins2.csv') # win totals for each team

teams = list(wins['Unnamed: 1'])
records = list(wins['Unnamed: 2'])
del(records[0])
del(teams[0])
records2 = []
teams2 = [] #this whole sequence preps the data to turn it into a dictionary

for i in records:
	new = i.split('-')
	a = float(new[0])
	b = float(new[1])
	percentage = float((a/(a+b)))
	records2.append(percentage)

for i in teams:
	new = i.split(' ')
	teams2.append(new[-1])

records2.append(0)
teams2.append('Supersonics')
teams2[6] = 'Trail Blazers'
teams2[15] = 'Hornets' #data is ready for final step of turning into a dictionary

predic = zip(teams2, records2)
teamrecords = dict(predic)


teamrecords # dictionary


population = { 'New York' : 19500000.0, 'Oklahoma City':1296565.0, 'Atlanta': 4457831.0, 
            'Washington D.C.': 5860342.0, 'Orlando' : 2267846.0, 'Denver': 2697000.0,
			'Cleveland': 2068283.0, 'Salt Lake City' : 1140483.0, 'Minneapolis': 3459146.0,
			'Los Angeles':16400000.0, 'Chicago': 9522434.0, 'Miami':5564635.0, 'Portland': 2314554.0,
			'San Francisco': 4516276.0, 'Boston': 4590000.0, 'Charlotte': 2335358.0, 'Philadelphia':
			6034678.0, 'Dallas': 6810000.0, 'New Orleans': 1240977.0, 'Indianapolis': 1756241.0,
			'Houston' : 6313158.0, 'Milwaukee': 1566981.0, 'Seattle': 3610105.0, 'Toronto' : 5583064.0,
			'San Antonio': 2234023.0, 'Phoenix': 4398762.0, 'Memphis':1316100.0, 'Detroit': 4292060.0,
			'Sacramento': 2600000.0}
			
teamcities = {'Knicks':'New York', 'Thunder':'Oklahoma City', 'Hawks' : 'Atlanta',
            'Wizards' : 'Washington D.C.', 'Magic' : 'Orlando', 'Nuggets' : 'Denver',
			'Cavaliers' : 'Cleveland','Jazz' : 'Salt Lake City', 'Timberwolves' : 'Minneapolis',
			'Lakers' : 'Los Angeles', 'Bulls' :'Chicago', 'Heat' : 'Miami', 'Trail Blazers' : 'Portland',
			'Warriors' :'San Francisco', 'Celtics': 'Boston', 'Hornets' : 'Charlotte', '76ers' : 'Philadelphia',
			'Mavericks' : 'Dallas', 'Pelicans' : 'New Orleans', 'Pacers' : 'Indianapolis',
			'Rockets':'Houston','Bucks' : 'Milwaukee', 'Supersonics' : 'Seattle', 'Raptors' : 'Toronto',
			'Spurs' : 'San Antonio','Suns' : 'Phoenix','Grizzlies' : 'Memphis','Pistons' : 'Detroit',
			'Kings' : 'Sacramento', 'Clippers' : 'Los Angeles', 'Nets' : 'New York'}

poplist = []
tagtotals = []
ratios = []
winpercentages = []
citypopulationpro = []
fanpro = []
			
for i in datalist2: # prepares data to be turned into a DataFrame
	usapop = 313900000
	pop = population[teamcities[i]]
	sup =float(counts[i])
	poplist.append(pop)
	tagtotals.append(sup)
	ratios.append((sup/pop))
	winpercentages.append(teamrecords[i])
	citypopulationpro.append((pop/usapop))
	fanpro.append(counts[i]/4591.0)

	

finallist = zip(datalist2, tagtotals, fanpro, poplist, ratios, winpercentages, citypopulationpro) # prepares data to be turned into a DataFrame

df = pd.DataFrame(finallist, columns = ['Team', 'Fans', '% of Fans', 'City Population', 'Fan Population Ratio', 'Win%',
                                         'CityPop/CountryPop',]) # Data Frame creation
df = df.set_index('Team') # Setting Index 

print df # Ready for analysis
	