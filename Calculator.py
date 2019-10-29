#Program to display all options of calculator

num1 = int(input("Number First Number: "))
num2 = int(input("Number Second Number: "))

num = input("Enter the Operator [+,-,*,/]: ")

#ad = list(map(lambda x : x + y, add(a,b,)))
#su = list(map(lambda x: x - y, sub(a,b)))
#di = list(map(lambda x : x / y, div(a,b)))
#mu = list(map(lambda x : x * y, mul(a,b)))

def ad(x,y):
    return x + y
def su(x,y):
    return x - y
def mu(x,y):
    return x * y
def di(x,y):
    return x / y

if num == '+':
    print("The value", ad(num1, num2))
elif num == '-':
    print("The value", su(num1, num2))
elif num == '*':
    print("The value", mu(num1, num2))
elif num == '/':
    print("The value", di(num1, num2))
else:
    print("Invalid option")
#def cal(num):
#    switcher = {
#        1 : print("The value",ad(num1,num2)),
#        2 : print("The value",su(num1,num2)),
#        3 : print("The value",di(num1,num2)),
#        4 : print("The value",mu(num1,num2))
 #   }
#    return switcher.get(num,"Invalid Oprion")
