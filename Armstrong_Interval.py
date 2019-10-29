# Program to Print Armstrong number with Intervals
lower = 100
upper = 20000

for num in range(lower,upper+1):
    sum = 0
    temp = num
    order = len(str(num))
    while temp > 0:
        d = temp % 10
        #print(temp,"% 10 =",d)
        sum = sum + (d ** order)
       # print("Sum:",sum)
        temp = temp // 10
        #print(p,"// 10 =", p)

    if num == sum:
        print("Amstrong Number:",num)



