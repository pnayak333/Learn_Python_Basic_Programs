#PRogram to give the options for Y or N and ask for fname and lname - Display

customers = []

while True:
    Opt = input("Enter the Option yes or no :")
    Opt = Opt[0].lower()
    if Opt == 'y':
        fname , lname = input("Enter the First and Last Name:").split()
        customers.append({'fname':fname,'lname':lname})
    else:
        print("Ooops! Wrong Entry")
        break
for n in customers:
    print(n['fname'],n['lname'])