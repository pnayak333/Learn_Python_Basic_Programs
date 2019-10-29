#Program to display sum of natural numbers usinf Recursion

def Sum_Rcr(n):
    if n == 0:
        return 0
    elif n ==1 :
        return 1
    else:
        return n + Sum_Rcr(n-1)

#for n in range(1,5):
print("Sum of N Numbers:", Sum_Rcr(5))