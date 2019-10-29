# program to print Armstrong number 3**3 + 7**3 + 1**3
num = int(input("Eneter the number value" ))

sum = 0
temp = num
while temp != 0:
    p = temp % 10
    print(temp,"% 10 =",p)
    sum = sum + (p ** 3)
    print("Sum:", sum)
    temp = temp // 10
    print("After Devide:",temp)
if num == sum:
    print("*******The number is Armstrong******")
else:
    print("*******Not an Armstrong Number********")
