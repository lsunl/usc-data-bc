# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV's
import csv

csvpath = os.path.join('..', 'Downloads', 'netflix_ratings.csv')

# # Method 1: Plain Reading of CSVs
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#    for row in csvreader:
    title = input("Which video are you looking for?")
        #print(f"{row[0]} is rated {row[1]} with a rating of {row[6]}")
    for row in csvreader:
        if row[0] == title:
            print(f"{row[0]} is rated {row[1]} with a rating of {row[6]}")
        #print(f"{title[0]} is rated {title[1]} with a rating of {title[6]}")
        #else:
        #    print("cannot be found")
    # Read each row of data after the header
    #for row in csvreader:
    #    print(row)
        #print(row[1])
