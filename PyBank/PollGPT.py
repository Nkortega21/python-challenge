import os
import csv

totalvotes = 0
vote_counts = {}

csv_election_data = os.path.join('..', 'Resources', 'election_data.csv')
with open(csv_election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        totalvotes += 1
        candidate = row[2].strip()  # Using .strip() to remove any leading/trailing whitespace

        # Update vote counts in the dictionary
        if candidate in vote_counts:
            vote_counts[candidate] += 1
        else:
            vote_counts[candidate] = 1

    # Convert dictionary keys (candidate names) to a list
    candidate_list = list(vote_counts.keys())
    print(f"Total Votes: {totalvotes}")
    print(f"Candidates: {candidate_list}")

    # Calculate and print the percentage of total votes for each candidate
    for candidate, count in vote_counts.items():
        percentage = (count / totalvotes) * 100
        print(f"{candidate}: {count} votes, {percentage:.2f}%")

    # Determine the winner by finding the candidate with the maximum votes
    winner = max(vote_counts, key=vote_counts.get)
    print(f"The winner is: {winner} with {vote_counts[winner]} votes")