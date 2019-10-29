#Program to find the factor of the number Eg: 8 -> 1*8,2*8,4*8
num = int(input("Enter the Number:"))
l = []
if num > 1 :
    for i in range(2,num):
        if(num % i ==0):
            l = i
            print(l)
else:
    print("oops Wrong Entery - Watch it")