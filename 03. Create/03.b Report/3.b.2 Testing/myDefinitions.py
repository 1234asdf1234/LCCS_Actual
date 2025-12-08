import csv

'''Note:  These are the functions I AM TESTING'''

def clean_temperature(raw_line):
    '''Cleans a raw serial line from the micro:bit and converts it to an integer temperature'''
    
    temperature = raw_line[2:]                  # remove leading b' from "b' 24\\r\\n'"
    temperature = temperature.replace(' ', '')  # remove spaces
    temperature = temperature.replace("'", '')  # remove quotes
    temperature = temperature.replace('\\r\\n', '')  # remove carriage returns and newlines

    if int(temperature) < -10 or int(temperature) > 60:     ''' Using the int() function removes any leading zeros e.g. in my Edge Case Test for 009'''
        raise ValueError("Temperature out of valid range.")
    return int(temperature)

def write_temperature_to_csv(filename, temperature):
    '''Writes temperature and doubled value to a CSV file.'''
    
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([temperature, temperature * 2])
        csvfile.flush()

