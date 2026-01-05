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


# list of months
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

def scoring(month, temp, wind, rh, dmc, dc, ffmc):
    # risk score
    score = 0

    # rule about months
    if month == "mar" or month in months[5:10]: # march, june-october
        score += 5
    elif month not in ["jan", "nov"]: # months with least risk
        score += 1

    # temperature
    if temp > 30:
        score += 5
    elif temp > 25:
        score += 3
    elif temp > 15:
        score += 2

    # humidity
    # low relevance thus lower scoring factors
    if rh <= 30:
        score += 2
    elif rh <= 50:
        score += 1

    # wind (small impact)
    if wind >= 6:
        score += 2
    elif score >= 4:
        score += 1

    # drought (small impact)
    score += dc * (1/500)

    # duff (small impact)
    score += dmc * (1/200)

    # litter flammable (large impact)
    if ffmc >= 90:
        score += 4
    elif ffmc >= 80:
        score += 2

    score = round(score, 3)
    print(score)
    # evaluating
    if score >= 16:
        print("high risk, action needed")
    elif score >= 13:
        print("medium risk")
    else:
        print("low risk")

    return score