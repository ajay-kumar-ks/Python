import re

with open("text.txt") as file:
    text = file.read()
    numbers = re.findall(r'\b[6-9]\d{9}\b', text)
    print(numbers)
