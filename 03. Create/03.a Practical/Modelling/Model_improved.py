'''
The improved version of model, considering months.
'''

from Model import scoring
import csv

# first row in the dataset
month = "" # to be inputted in demonstration
temp = 8.2
wind = 6.7
rh = 51 # relative humidity
dmc = 26.2 # duff
dc = 94.3 # drought
ffmc = 86.2 # flammable litter


# list of months
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

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
        for i in range(1, len(line)):
            line[i] = float(line[i])
        score = scoring(*line)
        print(f"This is input number {lines_count+1}.")
        print(f"Compare the input number {lines_count}, the risk has deviated by {round(score-last_score, 2)}.")
        last_score = score
        lines_count += 1

'''
if __name__ == "__main__":
    date = datetime.datetime.now() # get current date
    month = months[date.month-1] # get corresponding month value
    scoring(month, temp, wind, rh, dmc, dc, ffmc) 
    '''

# read a file