a = 0
b = 1
num = int(input("enter fibinacci limit : "))
print(a,end = " ") 
for i in range(num):
    print(b,end = " ")
    a,b = b,a+b
    
pos = int(input("\nenter fibinacci position : "))
a = 0
b = 1
for i in range(pos):
    a,b = b,a+b
print(b,end = "\n")
