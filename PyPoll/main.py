import os
import csv

# File path
election_csv = os.path.join('Resources','election_data.csv')

# Function for candidate data
def can_list(candidate,votes):
    can_data = [candidate,votes,round((votes/ballot_count*100),3)]
    return(f'{can_data[0]}: {can_data[2]}% ({can_data[1]})')

# Open file to read
with open(election_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

# Initialize variables
    ballot_count = 0
    candidates = {}
    winner_count = 0

# Iterate through rows
    for row in csvreader:

        #Count total ballots
        ballot_count += 1

        #Add new candidate to dictionary and update candidate's vote count
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

    hash = '--------------------'
    lines = ['Election Results',hash,(f'Total Votes: {ballot_count}'),hash]
    
# Iterate through candidate dictionary with function and determine winner
    for k,v in candidates.items():
        if v > winner_count:
            winner_count = v
            winner = (f'Winner: {k}')
        lines.append(can_list(k,v))
    lines.append(hash)
    lines.append(winner)
    lines.append(hash)

# Print to terminal
    for line in lines:
        print(line)

# Write to file
results_path = os.path.join('Analysis','analysis.txt')
with open (results_path,'w') as f:
    for line in lines:
        f.write(f'{line}\n')