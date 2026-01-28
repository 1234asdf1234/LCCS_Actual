import AR1 as Model

test1 = ["jan", 2, -2.5, 34, 26.2, 92, 84.3] # negative windspeed
test2 = ["jul", 8.2, 6.7, 51, 26.2, 94.3, 86.2] # normal
test3 = ["jan", 0, 0, 0, 0, 0, 0] # boundary
test4 = ["jul", -8.2, 6.7, 51, 26.2, 94.3, 86.2] # negative temperature

Model.scoring(*test1)
Model.scoring(*test2)
Model.scoring(*test3)
Model.scoring(*test4)