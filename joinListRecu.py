def addList(lst):
    if len(lst) == 1:
        return str(lst[0])
    
    return str(lst[0]) + "-" + addList(lst[1:])


listVal = [1,2,3,4,5,6,7,8]
result = addList(listVal)
print(result)
