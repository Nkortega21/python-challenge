#Module 3 Poll_main.py

import os
import csv

totalvotes = 0
vote_counts = {}
output_text = []

csv_election_data = os.path.join("UCI DA Class Folder","python-challenge","PyPoll","Resources","election_data.csv")
with open(csv_election_data) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     for row in csvreader:
         totalvotes += 1
         candidate = row[2].strip()
         if candidate in vote_counts:
             vote_counts[candidate] += 1
         else:
             vote_counts[candidate] = 1

output_text.append("Election Results")
output_text.append("---------------------")
output_text.append(f"Total Votes: {totalvotes}")
output_text.append("---------------------")
for candidate, count in vote_counts.items():
    percentage = round((count / totalvotes) * 100, 3)
    output_text.append(f"{candidate}: {percentage:}% ({count})")

win = max(vote_counts, key=vote_counts.get)
output_text.append("---------------------")
output_text.append(f"Winner: {win}")
output_text.append("---------------------")

output_file = os.path.join("UCI DA Class Folder","python-challenge","PyPoll","Resources","election_results.txt")
with open(output_file, 'w') as file:
    for line in output_text:
        file.write(line + "\n")
		