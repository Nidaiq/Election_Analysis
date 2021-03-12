# The data we need to retrieve.
import csv
import os
# Assign variable to the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to the path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Inititalize a total vote counter
total_votes = 0

# Candidate Options
candidate_options =[]

# Declare candidate_vote dictionary
candidate_votes = {}

# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:

  # To do: read and analyze the data here
  # Read the file with reader function
  file_reader = csv.reader(election_data)
  
  # Read header row
  headers = next(file_reader)

  #Print each row in the csv file
  for row in file_reader:
    #2.Add to the total vote count
    total_votes += 1
    
    # Find candidate name in each row as it is thrid colum 
    candidate_name = row[2]

    # If candidate name is not present add to list
    if candidate_name not in candidate_options:

      # Add candidate name to the list
      candidate_options.append(candidate_name)
      
      # Begin tracking candidate votes
      candidate_votes[candidate_name] = 0

    # Begin candidate vote count
    candidate_votes[candidate_name]+= 1

# Print the total votes
print(candidate_votes)

#3. The percentage of votes each candidate won by looping through the count
# % votes per candidate = (candidate_votes/ total_votes)*100
for candidate_name in candidate_votes:
  # Retrive votes of the candidates
  votes = candidate_votes[candidate_name]
  # calculate percentage of votes
  vote_percentage = float (votes) / float (total_votes) *100
  
  # The total number of voles each candidate won
  # Print statement
  print(f' {candidate_name} recieved {round(vote_percentage,1)}  % of the vote')


  # Print out each candidate's name, vote count and percentage  
  print(f"{candidate_name}: {vote_percentage:.1f} %, ({votes:,})\n")

# votes to terminal
  if (votes > winning_count) and (vote_percentage > winning_percentage):
    # if true winning_count = votes and winning_percentage = vote_percentage 
    winning_count = votes
    winning_percentage = vote_percentage
    # set winning_candidate = candidant_ name
    winning_candidate = candidate_name
    # For statement
for candidate in candidate_votes:
  # The winner of the election based on popular vote
  winning_candidate_summary = (
    f"--------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Votes: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"--------------------\n"
    )
print(winning_candidate_summary)