#Program - Palindrome of a String
#Reversing a String without using builtin Function

#----------------------------------------------------
mystr = "GeeGeeG"
mystr = mystr.casefold()
print(mystr)
revstr = reversed(mystr)
#print(revstr)
if list(mystr) == list(revstr):
    print("Palnindrome")
else:
    print("Not Palindrome")
#------------------------------------------------------
newstr = []
n = len(mystr)
n = n-1
print(n)
while n >= 0:
    newstr.append(mystr[n])
    n = n -1
#for n in newstr:
print(newstr)
