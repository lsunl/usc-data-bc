import os
import csv

cereal_csv = os.path.join("../Downloads", "cereal.csv")

with open(cereal_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)


    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")



    for row in csvreader:
        fiber = float(row[7])
        if fiber > 5:
            print(row[0])
