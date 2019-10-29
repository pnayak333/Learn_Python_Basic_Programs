#Program to display Anonymous power of values

num = int(input("Value: " ))

res = list(map(lambda x:  2 ** x, range(num)))
op = list(map(lambda x : x ** 2, range(num)))

for i in range(num):
    print("2 to the Power of", i , "is:=", res[i])
    print(i, " to the power ", i,"is=",op[i])