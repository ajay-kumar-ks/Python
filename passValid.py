import re

def check_for_case_mix(text):
    has_lower = any(c.islower() for c in text)
    has_upper = any(c.isupper() for c in text)
    return has_lower and has_upper

def check_for_num(text):
    return bool(re.search(r'\d', text))

def check_for_special_char(text):
    pattern = r"[$@#&%]"
    return bool(re.search(pattern, text))

strn = input("Enter a string: ")
flg = 1
if len(strn) < 6 or len(strn) > 16:
    print("Password should be min 6 and max 16 characters")
    flg = 0

if not check_for_case_mix(strn):
    print("Password must have capital and small letters")
    flg = 0

if not check_for_num(strn):
    print("Password must have numbers")
    flg = 0

if not check_for_special_char(strn):
    print("Password must have special characters")
    flg = 0
if flg:
    print("good password")
