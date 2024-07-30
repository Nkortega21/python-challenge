#Module 3 Poll_main.py
import os
import csv
#setup counter for total votes, dictionary to count votes for each candidate, and a list to store lines for output
vote_total = 0
vote_count = {}
export_list = []
#define file path for importing data
poll_main = os.path.join("Resources","election_data.csv")
with open(poll_main) as csvfile: #open the csv file
     csvreader = csv.reader(csvfile, delimiter=',') #read csv file
     csv_header = next(csvreader) #skip header row
     for row in csvreader:
         vote_total += 1 #increase total number of votes by 1
         candidate = row[2].strip() #get candidates name
         if candidate in vote_count:
             vote_count[candidate] += 1 #if a candidate is in the dictionary increase the number of votes by 1
         else:
             vote_count[candidate] = 1 #if there is a new candidate add them to the dictionary and establish their count as 1

export_list.append("Election Results") #Header for export list
export_list.append("---------------------")
export_list.append(f"Total Votes: {vote_total}") #Total votes for export list
export_list.append("---------------------")
for candidate, count in vote_count.items(): #for each candidate in the dictionary calculate the percentage of votes recieved and amount of votes recieved then add it to the export list
    percentage = round((count / vote_total) * 100, 3)
    export_list.append(f"{candidate}: {percentage:}% ({count})")

win = max(vote_count, key=vote_count.get) #determine the winner and add to export list
export_list.append("---------------------")
export_list.append(f"Winner: {win}")
export_list.append("---------------------")

for line in export_list:
	print(line)

#define file path for exporting data
output_file = os.path.join("analysis","election_results.txt")
with open(output_file, 'w') as file:
    for line in export_list:
        file.write(line + "\n") #export to file path and separate onto different lines
		