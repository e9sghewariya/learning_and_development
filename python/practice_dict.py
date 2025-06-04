"""practice_dict.py"""
# This script creates a dictionary with number words as keys and their corresponding integers as values.
number_dict = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20
}

print("Keys:", number_dict.keys())
print("Values:", number_dict.values())

for key, value in number_dict.items():
    print(f"{key} + two : {value + 2}")
