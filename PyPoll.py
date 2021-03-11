# The data we need to retrieve.
import csv
import os
# Assign variable to the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to the path
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

  # To do: read and analyze the data here
  # Read the file with reader function
  file_reader = csv.reader(election_data)
  # Read and print the header row
  headers = next(file_reader)
  print(headers)

# To do performance analysis
  
#1.The total number of votes cast
#2. A complete list of candidates who recieved votes
#3. The percentage of votes each candidate won
#4. The total number of voles each candidate won
#5. The winner of the election based on popular vote