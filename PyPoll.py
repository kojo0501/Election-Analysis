print("test print")

# Add our dependencies.
import csv
import os

# vote counter
total_votes = 0

# List of candidates
candidate_options = []

# Dictionary connecting candidates w/ vote totals.
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Open the election results and read the file
    headers = next(file_reader)


    #Print each row in the CSV file
    for row in file_reader:
        #print(row)
        # vote count
        total_votes += 1

        # Copy the candidate name from each row into a variable.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Set vote counter to zero
            candidate_votes[candidate_name] = 0

        # Tracking candidate vote counts
        candidate_votes[candidate_name] += 1

# print the total votes

print(total_votes)

# Print the candidate list.
print(candidate_options)
print(candidate_votes)


# Percentage of votes for each candidate
# Going through the list
for candidate_name in candidate_votes:
    # Making a variable for candidate votes
    votes = candidate_votes[candidate_name]
    # Doing the math
    vote_percentage = float(votes) / float(total_votes) * 100
    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")

    # Evaluating to see if they're the winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # As it goes through, it will reassign the highest total to these variables
        winning_count = votes
        winning_percentage = vote_percentage
        # And reassign the winning candidate
        winning_candidate = candidate_name

# print out the winning candidate name, vote count, and percentage
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)