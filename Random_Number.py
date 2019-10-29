import random

print(random.randint(0 , 1000))
print(random.randrange(10,20,1))
kilometer = 50
miles = 50
mile = kilometer * 1.628
kilo = miles * 0.628

print("MileS:",mile , "Kilomtere", kilo)
cel = 32
farh = 75
far = (cel *1.8) +32
cels = (farh - 32) / 1.8

num = int(input("Enter the Number to Check +ve or -ve?: "))
if num > 0:
    print("+ve",num)
else:
    print("-ve",num)
num2 = int(input("Eneter the number to check Even or Odd: "))
if (num2 % 2 == 0):
    print("Number is Even", num2)
else:
    print("Number is Odd",num2)
print("Faren" , far, "Celsius",cels)