# Model rules:
'''
1. if 
'''

# first row in the dataset
month = "jul"
temp = 8.2
wind = 6.7
rh = 51 # relative humidity
dmc = 26.2 # duff
dc = 94.3 # drought
ffmc = 86.2 # flammable litter


def scoring(month, temp, wind, rh, dmc, dc, ffmc):
    # risk score
    score = 100 # this will be changed later according to month factor

    ''' 
    we ignore the month factor in this iteration
    it will be included in the improved version to meet AR3
    also, to make changes easier to interpret
    we deduct points from an initial score when risk factors
    which meet the requirements
    '''

    '''
    if month == "mar" or month in months[5:10]: # march, june-october
        score += 5
    elif month not in ["jan", "nov"]: # months with least risk
        score += 1

    '''

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
    if score <= 45:
        print("high risk, action needed")
    elif score <= 60:
        print("medium risk")
    else:
        print("low risk")

    return score

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
    scoring(month, temp, wind, rh, dmc, dc, ffmc)