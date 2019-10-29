arr = [1, 2, 3, 4, 5, ]
inner = input('Hello ')
print('Hi' + inner)
ln = len(arr)
sum = 0
sqr = 0.0
qub = 0.0
num = 25
num_sqrt = num ** 0.5
print(num_sqrt)
print("Length of the array:", ln)
print('')
for i in arr:
    if i > 3:
        print("break:", i)
        continue
    sum = sum + i
    qub = i * i * i
    sqr = i * i
    print("Value : I * I * I", i, "Qube:", qub)
    print(" I * I:", i , "*", i , "Squres:", sqr)
    print("Value:", i, "Sum:", sum)
