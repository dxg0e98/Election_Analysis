# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_results:
    file_reader = csv.reader(election_results)

# print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
    # add to the total vote count
        total_votes += 1

print(total_votes)

    