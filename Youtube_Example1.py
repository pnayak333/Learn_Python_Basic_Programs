# lst1 = [2,5,6,7,9] , lst2 = [1,4,3,11,12] , total = 23

# using Bruteforce
lst1 = [2,5,6,7,9]
lst2 = [1,4,3,11,12]
total = 21
sum = 0
for first in lst1:
    for line in range(len(lst2)):
       #global sum
        sum = first + lst2[line]
        #print(sum)
        if total == sum:
            print("Found :",first,"+",lst2[line],"=",sum)
        else:
            print("Not found Sum :",first,"+",lst2[line],"=",sum)