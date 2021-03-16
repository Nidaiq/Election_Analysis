# Election Analysis

# Challenge Overview
Tom, who is a Colorado Board of Elections employee has given you the following tasks to complete audits of a recent local congressional election in Colorado.  The results will be used to tabulate and certify the US congressional race.

## Purpose
The purpose of this project is to write a python code to automate the process for the total votes, candidate results and county results of the election.  Breakdown of the criteria's required are as follows:

- **Calculate the total number of votes cast**

- **Candidate Results:**
1. Get a complete list of candidates who received votes
2. Calculate the total number of votes each candidate received
3. Calculate the percentage of votes each candidate won
4. Determine the winner of election based on popular vote

- **County Results:**
1. Complete list of counties that the voting took place in
2. Calculate the total number of votes receive in each county
3. Calculate the percentage of votes each candidate won
4. Determine the winner of election based on popular vote

# Resources
- Data Source: election_results.cvs
- Software: Python 3.7.6, Visual Studio Code 1.54.1

# Election Audit Results
The analysis of the election show that:
- There were 369,711 votes casted in the election

The candidates are:
-   Charles Casper Stockham
-   Diana DeGette
-   Raymon Anthony Doane

The counties involved are:
-	Jefferson
-	Denver
-	Arapahoe

## Candidate Results and Winner
The candidate’s results are as follows:
-   Charles Casper Stockham received 23.0 % of votes and 85,213 votes
-   Diana DeGette received 73.8 % of votes and 272,892 votes
-   Raymon Anthony Doane received 3.1 % of votes and 11,606 votes

The results show that Diana DeGette who won the election by a landslide and received 73.8 % of votes and 272,892 votes.

## County Results and Largest County Turnout
The county results are as follows:
-	Jefferson county received 10.5% and 38,855 votes out of the total votes
-	Denver county received 82.8% and 306,055 votes out of the total votes
-	Arapahoe county received 6.7% and 24,801 out of the total votes

The results show that the Denver county had he largest county turnout with 82.8% of the votes received in that county.

# Election Audit Summary
The script can be modified to work on a larger scale by adding *state_list* list and a *state_vote* dictionary.  The code can be modified to tally up the results for all the states in a similar manner that it has been done for counties and candidates.  Modifications can also be made to the script to have live output as results are counted in.  The script can also be reused by assigning the hard-coded variables currently in the script (for example the *election_results.csv* and *election_results.txt*) to variables.  This would allow the user to assign those variables to other files and reuse them for other tasks.  

The script created for this audit can be used for senatorial district and other local elections.  The script can also be later modified and incorporated to have a live output that could be telecasted over various networks.  The script can also be modified to use on a much smaller scale and make it fun for the students in schools for their student council elections.  The possibilities are endless.  
