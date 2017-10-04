from bs4 import BeautifulSoup
import os.path
import requests
import pandas as pd
import numpy as np
import lxml
import html5lib

# get output file name
output_file = input('Name of file to ouput to: ')

# get year
year = input('Year: ')

# get league name
league_name = input('League country: ')

cont = 'y'
rosters = []

# while still entering is yes
while (cont != 'n'):
	# team name
	team = input('Team name: ')

	# link to team
	url = input('Link to team: ')

	# scraping part
	df = pd.read_html(requests.get(url).text, encoding='ASCII')
	df = df[0]

	# fix column headers
	df.columns = df.iloc[0]
	df = df.iloc[1:]

	# cut 'Players no longer at this club'
	i = df.loc[df['Number'] == 'Players no longer at this club'].index[0]
	df = df.iloc[:i-1] 

	# delete NaNs from name
	df = df[pd.notnull(df['Name'])]

	# add cols w team name and year
	df['Current Club'] = team
	df['Year'] = year
	df['Country League'] = league_name	
	# append df to list of dfs
	rosters.append(df)

	# ask if user wants to keep going
	print(df)
	cont = input('More teams? (y/n) ')

# write to file
df = pd.concat(rosters)
path = os.path.join('/Users/abbyoneill/Desktop/data_mining_project/csv', output_file)
df.to_csv(path)
