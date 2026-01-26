# AR3

from Model import scoring
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
        score = scoring(*line)
        print(f"This is input number {lines_count+1}.")
        print(f"Compared to input number {lines_count}, the risk has deviated by {round(score-last_score, 2)}.")
        last_score = score
        lines_count += 1
def scoring_evaluate(score):
    if score == -1:
        print("invalid arguments.")
    else:
        print(f"the final score is {score}.")
        print("The model detected ", end="")
        if score <= 25:
            print("high risk, action needed.")
        elif score <= 45:
            print("medium risk.")
        else:
            print("low risk.")

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

def month_impact(m):
    if m in months[5:9]:
        return "slightly decreased"
    elif m in months[2:5]:
        return "greatly decreased"
    else:
        return "stayed the same"

