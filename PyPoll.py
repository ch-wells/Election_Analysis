# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candiadte won
# 4. The total number of votes each candidate won
# 5. The winner of th election based on popular vote

# Add our dependencies
import csv
import os 

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable for the file to save and path
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the elections results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes> winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winnning Vote Count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
