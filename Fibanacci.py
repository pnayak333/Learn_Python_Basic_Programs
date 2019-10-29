# program to print fibanacci series
num = int(input("Enter the Number:" ))
count = 0
n1 = 0
n2 = 1
if num <= 0:
    print("Oops enter +ve Number")
elif num == 1:
    print(n1)
else:

    while count < num:
        print(n1)
        n3 = n1 + n2

        #print(n3)
        n1 = n2
        n2 = n3
        count = count + 1
