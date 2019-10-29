#Program - Remove Punctuations

punct = '''@#$%^&!<>;"':'''

mystr = "Myname!is@#Prash>:Nayakzzz;'"
newstr = ""

for ch in mystr:
    if ch not in punct:
        newstr = newstr + ch
print(newstr)