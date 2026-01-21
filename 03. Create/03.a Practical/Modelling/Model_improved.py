'''
The improved version of model, considering months.
'''

import datetime

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
months_capital = ['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December'
]

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
        scoring_evaluate(-1)
    # risk score
    score = 100 # this will be changed later according to month factor

    ''' 
    most rules are inherited from AR1, while adding these:
    - if jun-sep, score = 80 (big impact)
    - if mar-may or oct or dec, score = 90 (medium impact)
    - otherwise score = 100 (no changes)
    '''
    
    impact = month_impact(month)
    if impact == "slightly decreased":
        score = 90
    elif impact == "greatly decreased":
        score = 80
    

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
    scoring_evaluate(score)
    return score

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


def month_impact(m):
    if m in months[5:9]:
        return "slightly decreased"
    elif m in months[2:5]:
        return "greatly decreased"
    else:
        return "stayed the same"

if __name__ == "__main__":
    date = datetime.datetime.now() # get current date
    month = months[date.month-1] # get corresponding month value
    month_capital = months_capital[date.month-1]
    print(f"It is now {month_capital}.")
    print(f"Due to that, the initial score threshold has \
{month_impact(month)}.")
    scoring(month, temp, wind, rh, dmc, dc, ffmc) 