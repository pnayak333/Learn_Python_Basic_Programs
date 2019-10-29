#program to Divide 12 to all other number IN LIST
# Program for Anagram of a string
#Prigram for Palindrome of a string

from collections import Counter
lst = [12,24,2,45,67,34,66,99] # Devide % 12

pa = ["geeg","geek","paap","abcd","xxx"] # Palindrome

my_list = ["geeks", "geeg", "keegs", "practice", "aa"] # Anagram

str = "egske"

dd = list(filter(lambda x :(x % 12 == 0),lst))
xx = list(filter(lambda x :(x == "".join(reversed(x))) , pa))
ff = list(filter(lambda x :(Counter(str) == Counter(x)) , my_list))
print("Number devided by 12 are :" , dd)
print(xx)
print(ff)