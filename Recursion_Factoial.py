#Program to display Recursion using factorial.
f = 1
dict = {}
def R_fact(n):
    if n in dict:
        return dict[n]
    if n < 0:
        value =  -1
    elif n < 2:
        value =  1
    else:
        value =  n * R_fact(n-1)
    dict[n] = value
    return value
def Iter_fact(m):
    if m < 0:
        return -1

    else:
        f = 1
        for i in range(1, m+1):
            f = f * i
        return f
print(R_fact(5))
print(Iter_fact(6))