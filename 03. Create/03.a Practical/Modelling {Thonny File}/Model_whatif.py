import Model # use model from AR1

# dummy data, peaceful condition
# calculate its score and compare to the other two
month = "may"
temp = 14
wind = 3.8
rh = 51 # relative humidity
dmc = 26.2 # duff
dc = 94.3 # drought
ffmc = 75 # flammable litter

score_original = Model.scoring(month, temp, wind, rh, dmc, dc, ffmc)
print(f"The original score is {score_original}")

# "what if severe drought occurs"
dc = 800
score_drought = Model.scoring(month, temp, wind, rh, dmc, dc, ffmc)
print(f"When drought occurs, score is {score_drought}")
print(f"Deviated by {round(score_drought-score_original, 3)}")

# "what if temperature rises drastically"
temp = 35
score_temp = Model.scoring(month, temp, wind, rh, dmc, dc, ffmc)
print(f"When temperature rises drastically, score is {score_temp}")
print(f"Deviated by {round(score_temp-score_original, 3)}")