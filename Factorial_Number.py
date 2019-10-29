# program for calculating the factorial number.
num = int(input("Enter the number :" ))
t = int(input("Enter the number :" ))

fact = 1
if num < 0:
    print("Ooops -ve number does'nt have factorial")
elif num == 0:
    print("Fact is 1")
else:
    for i in range(1 , num+1):
        fact = fact * i
    print(fact)

for i in range(1, 10+1):
    print(t, "*", i, "=", t*i)