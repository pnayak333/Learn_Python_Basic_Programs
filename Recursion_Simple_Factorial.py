#Program on Recursion - Factorial

def Factorail(num):
    if num == 0:
        return 0
    elif num == 1:
        return  1
    else:
        return num * Factorail(num -1)

num = int(input("Enter The Numer:"))
if num < 0:
    raise TypeError("Ooops! -ve Entry")
else:
    print(Factorail(num))

