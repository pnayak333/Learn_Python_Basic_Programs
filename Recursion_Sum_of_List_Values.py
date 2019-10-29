#Sum the entire list using Recursion
#Sum the different list inside the another list
#-----------------------------------------------------
lst = [4,5,6,7,8]
def Sum_List(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + Sum_List(lst[1:])

print("Sum of Values of List :",Sum_List(lst))
#----------------------------------------------------------
#you can use extend method in the else case so that each elemnt added supperatly in the end of the list - lst.extend(n) - else case
lst = [[2,3],[3],4,5,[[1]],[1,2,4]]

def Sum_List1(lst):
    tot = 0
    for n in lst:
        if type(n) != list:
            tot = tot + n
        else:
            tot = tot + Sum_List1(n)
    return tot
print("Sum of Values of List1 :",Sum_List1(lst))