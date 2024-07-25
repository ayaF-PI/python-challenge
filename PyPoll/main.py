import os 
import csv

# Define the path to the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Print the path to verify
print(f"CSV Path: {csvpath}")

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = {"name": "", "votes": 0}

# Print initial values to verify
print(f"Initial values:\nTotal Votes: {total_votes}\nCandidates: {candidate_votes}\nWinner: {winner}")

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row

    # Verify the header
    print(f"Header: {header}")

    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Update the vote count for each candidate
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentages and determine the winner
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

results += (
    "-------------------------\n"
    f"Winner: {winner['name']}\n"
    "-------------------------\n"
)

print(results)

# Write the results to a text file
output_path = os.path.join('analysis', 'results.txt')
with open(output_path, 'w') as textfile:
    textfile.write(results)

# Verify the results were written to the file
print(f"Results written to {output_path}")



