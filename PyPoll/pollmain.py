import os
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

#total number of votes cast
#candidate list
#percentage of votes won by each candidate
#total number of votes each candidate won
#winner based on total/popular vote

#set dictionaries, large data set, use keys to complete analysis
candidate_vote_cast = {}
candidate_percent_vote = {}

#initialize variables
total_votes = 0
winner = ""

with open(poll_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csvreader)

	#iterate through rows
	for row in csvreader:

		#total number of votes cast, row count
		total_votes += 1

		#conditional to increment up by 1 for vote cast to each candidate
		if row[2] in candidate_vote_cast:
			candidate_vote_cast[row[2]] += 1
		else:
			candidate_vote_cast[row[2]] = 1

		#assign winner using the max function
		winner = max(candidate_vote_cast, key=candidate_vote_cast.get)

	for key in candidate_vote_cast.keys():
		#set list to hold cast votes in order to determine
		#perentage of vote cast to each candidate
		voter = []
		voter.append((candidate_vote_cast[key]/total_votes)*100)
		voter.append(candidate_vote_cast[key])
		candidate_percent_vote[key] = voter


#Print Election Result Summary
print("Election Result Summary")
print("---------------------------")
print(f"Total Votes: {total_votes}")
for key in candidate_percent_vote:
	print(f"{key}: {round(candidate_percent_vote[key][0],2)}% ({candidate_percent_vote[key][1]})")
print(f"Winner: {winner}")
print("---------------------------")

#Output Election Results to text
PyPoll = open("Election_Result_Summary.txt", "w+")
PyPoll.write("Election Result Summary")
PyPoll.write('\n' + "---------------------------")
PyPoll.write('\n' + f"Total Votes: {total_votes}")
for key in candidate_percent_vote:
	PyPoll.write('\n' + f"{key}: {round(candidate_percent_vote[key][0],2)}% ({candidate_percent_vote[key][1]})")
PyPoll.write('\n' + f"Winner: {winner}")
PyPoll.write('\n' + "---------------------------")
