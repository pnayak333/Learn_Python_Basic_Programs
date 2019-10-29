# Prime Number - num > 1 and factor should be the same number

num = int(input("Enter the Number: "))

if num > 1:
    # the number should be > 1
    for i in range(2,num):
        if num % i == 0:
            print("The number is not a Prime")
            print(i, "times", num // i, "is", num)
            break
        else:
            print("Prime Number", num)
            break
else:
    print("Ooops Wrong number")