
"""
CP1404/CP5632 Practical
hex colours in a dictionary
"""

CODE_TO_NAME={"Absolute Zero": "#0048ba","Acid Green" : "#b0bf1a", "Alice Blue":"#f0f8ff","Baby Pink" : "#f4c2c2","Barn Red" : "#7c0a02","Beaver" : "#9f8170", "Bitter Lime" : "#bfff00","Blond" : "#faf0be","buff" : "#f0dc82","Camel" : "#c19a6b"}

colour_name=input("Enter Colour Name :").title()
print(CODE_TO_NAME[colour_name])

while colour_name!="":
    if colour_name in CODE_TO_NAME:
        print(f"Colour code of {colour_name} is {CODE_TO_NAME[colour_name]}")
    else:
        print("Invalid colour")
    colour_name = input("Enter Colour Name :").title()





