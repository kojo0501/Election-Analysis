#print("test print")

# Add our dependencies.
import csv
import os

# vote counter
total_votes = 0

# Lists of candidates and counties
candidate_options = []
county_list = []

# Dictionaries connecting candidates and counties w/ vote totals.
candidate_votes = {}
county_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
biggest_county = ""

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Go past the header
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        #print(row)
        # vote count
        total_votes += 1

        # Copy the candidate from each row into a variable.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Set vote counter to zero
            candidate_votes[candidate_name] = 0

        # Tracking candidate vote counts
        candidate_votes[candidate_name] += 1

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    next(election_data)

    for row in file_reader:
        
        # Copy the county from each row into a variable
        county_name = row[1]

        # Add county name if not listed
        if county_name not in county_list:
            county_list.append(county_name)

            # Set vote counter to zero
            county_votes[county_name] = 0
        
        # Tracking county vote counts
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (f"\nElection Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n")
    print(election_results, end="")
    # Save the final vote count in the text file.
    txt_file.write(election_results)

    # print the total votes

    #print(total_votes)

    # Print the candidate list.
    #print(candidate_options)
    #print(candidate_votes)

    # little bit of text formatting
    county_text = f"\nCounty Votes:\n"
    print(county_text)
    txt_file.write(county_text)

    for county_name in county_votes:
        # making a variable to hold county votes
        votes = county_votes[county_name]
        # mathing
        vote_percentage = float(votes)/float(total_votes) * 100
        
        # capture county results for printing
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes})\n")

        # printing county results
        print(county_results)
        txt_file.write(county_results)

        # evaluating the county w/ the largest vote total
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # As it goes through, it will reassign the highest total to these variables
            winning_count = votes
            winning_percentage = vote_percentage
            biggest_county = county_name
        
        # biggest county summary
        biggest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {biggest_county}\n"
        f"-------------------------\n")    
    print(biggest_county_summary)

    # Save it to the text file
    txt_file.write(biggest_county_summary)

    winning_count = 0
    winning_percentage = 0


    # Percentage of votes for each candidate
    # Going through the list
    for candidate_name in candidate_votes:
        # Making a variable for candidate votes
        votes = candidate_votes[candidate_name]
        # Doing the math
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #capture candidate results for printing
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")

        #print candidate results
        print(candidate_results)
        txt_file.write(candidate_results)

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

    # Save it to the text file
    txt_file.write(winning_candidate_summary)

