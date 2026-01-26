# AR3

import AR1 as Model
import csv

print("The programs reads the sample readings and simulates adaptive analysis.")

# lines read
lines_count = 0

# last score calculated
last_score = 0

with open("sample_readings.csv", 'r') as file:
    csvFile = csv.reader(file)
    # discard the first line
    next(csvFile)
    for line in csvFile:
        for i in range(1, len(line)): # the first string is month, ignore
            line[i] = float(line[i])
        score = Model.scoring(*line)
        print(f"This is input number {lines_count+1}.")
        print(f"Compared to input number {lines_count}, the risk has deviated by {round(score-last_score, 2)}.")
        last_score = score
        lines_count += 1

