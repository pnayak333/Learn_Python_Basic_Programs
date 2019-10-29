# PRogram - LIst

lst = [1,2,3,4,5,-2,6,10,1]
flag = False
print(lst)
for i in range(len(lst)):
    first = lst[i]
    #for j in range(1,len(lst)):
    if first  == 2:
        flag = True
        break
    else:
        flag - False
        break
if flag == True:
    print("Found", first)
else:
    print("Not")


