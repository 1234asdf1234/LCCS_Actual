import csv
import random

headers = ['month', 'temp', 'wind', 'rh', 'dmc', 'dc', 'ffmc']

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

with open("/Users/beriaru/Documents/LCCS_Actual/03. Create/03.a Practical/Modelling/sample_readings.csv", "w") as csvfile:
    db = csv.writer(csvfile)
    db.writerow(headers)
    for i in range(8): # eight rows
        month = months[i // 3]
        temp = random.randint(15, 30)
        wind = random.randint(8, 59) / 10
        rh = random.randint(25, 60)
        dmc = random.randint(20, 80)
        dc = random.randint(80, 400)
        ffmc = random.randint(70, 90)
        db.writerow([month, temp, wind, rh, dmc, dc, ffmc])
        csvfile.flush()



