# program to create calculator using lambda function
def add(x):
    return x + x
def sub(x):
    return x - x
def div(x):
    return x / x
def mul(x):
    return x * x
v = range(-20 , 10)

ch = list(filter(lambda x : x < 0 , v))
print(ch)

fun = [add , sub , div , mul]

for i in range(2 , 5):
    val = list(map(lambda x : x(i) , fun))
    print(val)
#print(fun(10))