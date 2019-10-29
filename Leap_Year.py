# program to check whether the Year Leap year or not
num = int(input("Enter The Year:" ))
if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print("Leap Year", num)
        else:
            print("Not a Leap Year", num)
    else:
        print("Leap year:",num)
else:
    print("Not a Leap year:",num)
