val = int(input('enter the size of the pyramid : '))

for i in range(val):
    for m in range(val-i):
        print(" ",end=' ')
    for k in range(i+1):
        print("*  ",end=" ")
    print('')