import re

with open("text2.txt") as file:
    for line in file:
        if re.search(r'\bs\w*e\b', line, re.IGNORECASE):
            print(line, end="")
