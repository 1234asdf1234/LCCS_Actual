import myDefinitions as md
'''Before You Begin:  Always remember that the Expected Value is the one we KNOW FOR SURE to be Correct'''

# ==========================================
# TEST 1 — STANDARD CASE
# Overall Purpose:  To test the 'clean_temperature()' function in myDefinitions,
#         which is responsible for cleaning and converting raw serial data.
# Code Tested:   "b'24\\r\\n'" — checks if the function correctly cleans this input
#         and returns the integer value 24.
# Note:   It is using the 'clean_temperature' function in myDefinitions.py.
# ==========================================
print("TEST 1 — STANDARD CASE")

raw_line = "b'24\\r\\n'"
expected_temp = 24
actual_temp = md.clean_temperature(raw_line)

if expected_temp == actual_temp:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("Expected:", expected_temp)
print("Actual:", actual_temp)

# ==========================================
# TEST 2 — EDGE CASE
# Overall Purpose:  To continue testing the 'clean_temperature()' function in myDefinitions,
#        ensuring it handles unusual but still valid input formats correctly.
# Code Tested:   Variations such as "b' 24\\r\\n'", "b'009\\r\\n'", and "b' -1\\r\\n'"
#        — checks if the function removes spaces, leading zeros, or signs and still
#     returns the correct integer values.
# Note:   It is using the 'clean_temperature' function in myDefinitions.py
# ==========================================

print("\nTEST 2 — EDGE CASES")

edge_cases = [
    (24, "b'     24\\r\\n'"),     # extra spaces:    24 Expected   - Actual 24
    (9,  "b'009\\r\\n'"),     # leading zeros:   9 Expected - Actual  9 
    (-1, "b' -1\\r\\n'")      # small negative:   -1 Expected - Actual -1
]

for expected, raw_input in edge_cases:
    actual_temp = md.clean_temperature(raw_input)

    # PASS / FAIL check
    if expected == actual_temp:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    # Final output (expected → actual)
    print("Expected:", expected)
    print("Actual:  ", actual_temp)
    print()

# ==========================================
# TEST 3 — BOUNDARY CASE
# Overall Purpose:  To test the 'clean_temperature()' function in myDefinitions
#                   to confirm it correctly handles values around the valid range (-10°C to 60°C).
# Code Tested:   Three boundary inputs — one below ("b'-11\\r\\n'"), one at ("b'-10\\r\\n'"),
#                 and one above ("b'61\\r\\n'") the valid range — checking that valid data
#                 is accepted and out-of-range values raise an error.
# Note:   It is using the 'clean_temperature' function in myDefinitions.py.
# ==========================================

print("\nTEST 3 — BOUNDARY CASE")

boundary_values = [
    "b'-11\\r\\n'",    # Expected: ERROR
    "b'-10\\r\\n'",    # Expected: -10
    "b'61\\r\\n'"      # Expected: ERROR
]

for i in boundary_values: # 'i' is the raw input
    try:
        actual_temp = md.clean_temperature(i)

        if actual_temp == -10:  # -10 is my boundary {check myDefinitions}
            print("Result: PASS")
        else:
            print("Result: FAIL")

        print("Expected:", "-10")
        print("Actual:  ", actual_temp)
        print()

    except ValueError:
        print("Result: PASS")
        print("Expected:", "ERROR")
        print("Actual:  ", "ERROR")
        print()


# ==========================================
# TEST 4 — INVALID CASE
# Overall Purpose:  To test the 'clean_temperature()' function in myDefinitions
#           to ensure it correctly rejects invalid or non-numeric data.
# Code Tested:   Two invalid inputs — one with text ("b'abc\\r\\n'") and one empty ("b''")
#                 — each should raise a ValueError and not return a temperature.
# Note:   It is using the 'clean_temperature' function in myDefinitions.py.
# ==========================================
'''Note:  I've included TWO Tests Here'''

print("\nTEST 4 — INVALID CASE")

# Test 4.1: Invalid text: 'abc' is invalid - not a number
try:
    actual = md.clean_temperature("b'abc\\r\\n'") # 'abc' is invalid
    print("Expected: ERROR")
    print("Actual:  ", actual)
    print("Result: FAIL")
    
except ValueError:
    print("Expected: ERROR")
    print("Actual:  ERROR")
    print("Result: PASS")
print()

# Test 4.2: Empty input
try:
    actual = md.clean_temperature("b''")
    print("Expected: ERROR")
    print("Actual:  ", actual)
    print("Result: FAIL")
except ValueError:
    print("Expected: ERROR")
    print("Actual:  ERROR")
    print("Result: PASS")
print()

# ==========================================
# TEST 5 — STRESS CASE
# Overall Purpose:  To test the 'write_temperature_to_csv()' function in myDefinitions
#         to confirm it performs reliably when handling a large volume of data.
# Code Tested:   Writes 5000 valid temperature entries (value 23) to 'stress_output.csv'
#                 — checks that the file is created correctly and contains all entries.
# Note:   It is using the 'write_temperature_to_csv' function in myDefinitions.py.
# ==========================================

print("\nTEST 5 — STRESS CASE")

# Write 5000 entries
testfile = 'stress_output.csv'
with open(testfile, 'w') as f:
    pass  # clear file

for i in range(5000):
    md.write_temperature_to_csv(testfile, 23) # Writes Temperatue 23

# Expected vs Actual
expectedV = 5000   # The expected number of entries based on the 5000 loop iterations
actualV = 0 # counter {This value 'should' increase to 5000 if function in myDef. works}

# Opens, reads and counts the number of entries
with open(testfile, 'r') as file:
    for i in file:
        actualV = actualV + 1

if expectedV == actualV:
    print("Test Passed")
else:
    print("Test Failed")


print("Expected entries:", expectedV)
print("Actual entries:", actualV)
