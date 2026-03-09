import csv
import random

headers = ['month', 'temp', 'wind', 'rh', 'dmc', 'dc', 'ffmc']

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

def sample_generate(lines, temp_upper=35, wind_upper=58, rh_upper=90):
    with open("/Users/beriaru/Documents/LCCS_Actual/03. Create/03.a Practical/Modelling/sample_readings.csv", "w") as csvfile:
        if temp_upper < 5 or wind_upper < 8 or rh_upper < 10:
            # upper limits lower than minimum
            print("Requirements: temp_upper >= 5 and wind_upper >= 8 and rh_upper >= 10")
            return None # terminate early
        db = csv.writer(csvfile)
        db.writerow(headers)
        for i in range(lines): # eight rows
            month = months[random.randint(0, 11)]
            temp = random.randint(5, temp_upper)
            wind = random.randint(8, wind_upper) / 10
            rh = random.randint(10, rh_upper)
            # the limit of following factors could not be changed
            # to ensure simplicity
            dmc = random.randint(20, 80)
            dc = random.randint(80, 400)
            ffmc = random.randint(70, 90)
            db.writerow([month, temp, wind, rh, dmc, dc, ffmc])
            csvfile.flush()



if __name__ == "__main__":
    sample_generate(8, 30, 10, 70)


