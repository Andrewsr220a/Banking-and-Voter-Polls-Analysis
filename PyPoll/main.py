import os
import csv
import math


election_data = os.path.join('Resources', 'election_data.csv')

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(type(election_data))
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Total Number of votes
    candidate_name = list()
    voter_count = dict()
    total_votes = 0

    for i in csvreader:
        Voter, County, Candidate = i
        candidate_name.append(Candidate)
        total_votes += 1

        if Candidate not in voter_count:
            voter_count[Candidate] = 1

        else:
            voter_count[Candidate] += 1

print(max(voter_count, key=lambda k: voter_count[k]))


Khan_percentage = (voter_count["Khan"] / total_votes) * 100
Correy_percentage = (voter_count["Correy"] / total_votes) * 100
Li_percentage = (voter_count["Li"] / total_votes) * 100
OTooley_percentage = (voter_count["O'Tooley"] / total_votes) * 100


print("Election Results")
print("-------------------------")
print("Total Votes:" + str(total_votes))
print("-------------------------")
print("Total Votes Per Candidate:" + str(voter_count))

print("Khan:" + str(Khan_percentage)+"%")
print("Correy:" + str(Correy_percentage)+"%")
print("Li:" + str(Li_percentage)+"%")
print("O'Tooley:" + str(OTooley_percentage)+"%")
