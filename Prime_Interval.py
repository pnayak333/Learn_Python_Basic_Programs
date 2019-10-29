#Program to priny Prime numbers from 500 to 600
lower = 1
upper = 50

for num in range(lower,upper):

    if num > 1:

        for i in range(2,num):
            #print(i,num)
            if num % i == 0:
                #print("Not Prime:","Index:",i,num)
                break

        else:
            print(num)