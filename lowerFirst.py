strn = input("enter a string : ")
str1 = ''
str2 = ''
for k in strn:
    if k.islower():
        str1 += k
    else :
        str2 += k
print("new => ",str1+str2)