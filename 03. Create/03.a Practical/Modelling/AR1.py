# AR1

import csv

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

# helper to check negative values
def anyneg(*args):
    for i in args:
        if i < 0:
            return True
    return False

# main scoring function
def scoring(month, temp, wind, rh, dmc, dc, ffmc):
    # terminate scoring if:
    # - numerical values (except temp) are negative
    # - month not valid
    if anyneg(wind, rh, dmc, dc, ffmc)\
    or (month not in months):
        print(-1)
        print("invalid parameter")
        return -1
    # risk score
    score = 100 # this will be changed later according to month factor

    ''' 
    most rules are inherited from AR1, while adding these:
    - if jun-sep, score = 80 (big impact)
    - if mar-may or oct or dec, score = 90 (medium impact)
    - otherwise score = 100 (no changes)
    '''
    if month in months[5:9]:
        score = 80
    elif month in months[2:5]:
        score = 90
    

    # temperature
    if temp > 30:
        score -= 30
    elif temp > 25:
        score -= 22
    elif temp > 15:
        score -= 10

    # humidity
    # low relevance thus lower scoring factors
    if rh <= 30:
        score -= 9
    elif rh <= 50:
        score -= 3

    # wind (small impact)
    if wind >= 6:
        score -= 8
    elif wind >= 4:
        score -= 4

    # drought (small impact)
    score -= dc * (1/125)

    # duff (small impact)
    score -= dmc * (1/50)

    # litter flammable (large impact)
    if ffmc >= 90:
        score -= 20
    elif ffmc >= 80:
        score -= 16

    score = round(score, 3)
    return score

# seperate the evaluation from scoring function
def scoring_evaluate(score):
    if score == -1:
        print("Invalid arguments.")
    else:
        print(f"The score is {score}.")
        print("The model detected ", end="")
        if score <= 25:
            print("high risk, action needed.")
        elif score <= 45:
            print("medium risk.")
        else:
            print("low risk.")


'''
use the temperature and rh column colleted from microbit
to simulate input.
notice this is recorded in a room
'''
# !!! notice to justify how the temp and rh is recorded in transcript
month = "jan"
temp = 29 # temperature
wind = 0.8 # wind, almost none
rh = 29 # relative humidity
dmc = 5 # duff
dc = 50 # drought
ffmc = 2 # flammable litter

if __name__ == "__main__":
    # score each row in output.csv
    with open("/Users/beriaru/Documents/LCCS_Actual/03. Create/03.a Practical/Modelling/output.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # ignore headings
        for row in reader:
            temp = float(row[0])
            rh = float(row[1])           
            print("Microbit data:")
            print("month\ttemp\twind\trh\tdmc\tdc\tffmc")
            print(f"{month}\t{temp}\t{wind}\t{rh}\t{dmc}\t{dc}\t{ffmc}")
            score = scoring(month, temp, wind, rh, dmc, dc, ffmc)
            scoring_evaluate(score)