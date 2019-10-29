#Program - Count number of vowels

vow = 'aeiou'

mystr = "This is my Home"

mystr = mystr.casefold()

count = {}.fromkeys(vow,0)
#count = 0
for char in mystr:
    if char in vow:
        count[char] +=  1
        #count += 1
print(count)