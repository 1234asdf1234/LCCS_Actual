'''
The improved version of model, considering months.
'''


# first row in the dataset
month = "jul"
temp = 8.2
wind = 6.7
rh = 51 # relative humidity
dmc = 26.2 # duff
dc = 94.3 # drought
ffmc = 86.2 # flammable litter


# list of months
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


def scoring(month, temp, wind, rh, dmc, dc, ffmc):
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
    elif score >= 4:
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
    print(score)
    # evaluating
    # changed in AR3 due to distribution
    if score <= 25:
        print("high risk, action needed")
    elif score <= 45:
        print("medium risk")
    else:
        print("low risk")

    return score