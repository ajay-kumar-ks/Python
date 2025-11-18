strn = input("enter a string odd length greater than 7 : ")
strLen = len(strn)
if strLen > 6 and strLen % 2 :
    mid = strLen // 2
    print('mid 3 char = >',strn[mid-1]+strn[mid]+strn[mid+1])
else :
    print('invalide string format')