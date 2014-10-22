import praw 
import pandas as pd
import numpy as np
import matplotlib as mpl

df = pd.read_csv('id_table.csv') # Grabs html pages from a csv file

idlist = list(df.values.flatten())  # Manipulates ids into a usable list


user_agent = ("nba comment scraper by /u/aguy")

r = praw.Reddit(user_agent) #opens connection with reddit api

authorlist = [] #list for user names
flairlist = [] #list for team allegiances

for i in idlist:
	submission = r.get_submission(submission_id = i) # navigates to wanted page
	comments = submission.comments #grabs comments from page

	submission.replace_more_comments(limit=None, threshold = 0) #makes sure all comments are grabbed

	all_comments = submission.comments 

	flatcomments = praw.helpers.flatten_tree(all_comments) #final comment list including replies


	for i in flatcomments: #adds user name + allegiance to list
		authorlist.append(i.author) 
		flairlist.append(i.author_flair_text)

com = zip(authorlist, flairlist) #creates two dimensional list with extracted pairs

commentsize = len(com) #checks how many comments there are in total

com = set(com) # deletes duplicates from users who comment more than once

com = list(com) #keeps data as a list

allegance = []

for i in com:
	a = i[1].encode('utf8', 'replace')
	allegance.append(a)

print com

print commentsize

data = pd.DataFrame(allegance)

print data

data.to_csv('nbaprojectdata.csv')

