#Program to find Heighest or Greatest comman Devisor
#Program for LCM

x = int(input("Enter Value1:"))
y = int(input("Enter Value2:"))
mul = x * y
def computeGCD(x,y):

    if x > y:
        lower = y
    else:
        lower = x
    for i in range(2,lower+1):
        if(x % i == 0) and (y % i == 0):
            hcr = i
    return hcr

z = computeGCD(x,y)
LCM = mul // z

print("GCD",z)
print("LCM",LCM)