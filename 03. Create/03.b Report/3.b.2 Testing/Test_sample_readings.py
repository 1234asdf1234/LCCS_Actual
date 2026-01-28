from sample_readings import sample_generate
import csv

test1 = [8, 37, 100, 95]     # standard case
test2 = [8, 50, 300, 100]    # edge case
test3 = [8, 5, 8, 10]        # boundary case
test4 = [8, 0, 0, 0]         # invalid case
test5 = [5000, 37, 100, 95]  # stress case

def validate(expected_lines):
    actual_lines = 0
    with open("/Users/beriaru/Documents/LCCS_Actual/03. Create/03.a Practical/Modelling/sample_readings.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        # in the invalid case, there is nothing in the file
        try:
            next(reader) # ignore the heading
        except StopIteration: # header not read
            return False
        # make sure the first three columns match the requirements
        for row in reader:
            # 1 for temperature, 2 for wind and 3 for rh
            for i in range(1, 4):
                row[i] = float(row[i])
            # the windspeed is divided by 10 in the definition
            if row[1] < 5 or row[2] < (5 / 10) or row[3] < 10:
                print(row[1], row[2], row[3])
                return False
            actual_lines += 1
    # the number of lines should match
    if actual_lines == expected_lines:
        return True
    return False

sample_generate(*test1)
print(validate(8))

sample_generate(*test2)
print(validate(8))

sample_generate(*test3)
print(validate(8))

sample_generate(*test4)
print(validate(8))

sample_generate(*test5)
print(validate(5000))