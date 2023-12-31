"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention - DONE
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    # if state_code in CODE_TO_NAME:
    #     print(state_code, "is", CODE_TO_NAME[state_code])
    # else:
    #     print("Invalid short state")
    # state_code = input("Enter short state: ").upper()
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
        state_code = input("Enter short state: ").upper()
    except KeyError:
        print("Invalid short state")
        state_code = input("Enter short state: ").upper()

for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name:15}")
