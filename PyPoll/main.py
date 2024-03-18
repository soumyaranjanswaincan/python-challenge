import os
import csv

#census_csv = os.path.join("..", "Resources", "election_data.csv")
poll_csv = "C:\\Soumya\\Data Analytics\\Module 3 - Challenge\\python-challenge\\PyPoll\\Resources\\election_data.csv"

total_votes = 0

# declare empty dictionary
candidates = {}

# declare empty list
sorted_list = []

with open(poll_csv) as csvfile:
    
    #hold content in a variable and specify delimiter
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    csv_header = next(csvreader)

    for row in csvreader:

        total_votes = total_votes + 1

        candidate_name = row[2]

        if candidate_name in candidates:
            # increment vote count
            candidates[candidate_name] = candidates[candidate_name] + 1
        else:
            # add new candidate with 1 vote
            candidates[candidate_name] = 1

# Print output to terminal
print("Election Results\n")
print("-----------------------------------------------\n")
print ("Total votes: " + str(total_votes)+"\n")
print("-----------------------------------------------\n")

for name, votes in candidates.items():
    print(f'{name}  :  {round((votes/total_votes*100),3)} % ({votes})\n')
print("-----------------------------------------------\n")

for name, votes in candidates.items():
    sorted_list.append([name,votes])

max_votes = sorted_list[0][1]

for item in sorted_list:
    if item[1] > max_votes:
        max_votes = item[1]
        winner = item[0]

print("Winner: " + winner+ "\n")
print("-----------------------------------------------\n")
