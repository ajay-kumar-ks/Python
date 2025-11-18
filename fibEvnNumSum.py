a = 0
b = 1
sum = 0;
num = int(input("enter fibinacci limit : "))
print(a,end = " ") 
for i in range(num):
    print(b,end = " ")
    a,b = b,a+b
    if not b % 2 :
        sum += b;

print("\n sum of even number in fibinacci ",sum)
