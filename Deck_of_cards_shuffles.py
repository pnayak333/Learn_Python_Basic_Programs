#Program to shuffle Deck cards
#Program to display month and year
import itertools,random
import calendar

yy= 2019
mm = 6
print(calendar.month(yy,mm))

deck = list(itertools.product(range(1,14),["Shade","Dimond","Squre","Love","abx"]))

random.shuffle(deck)

for i in range(5):
    print(deck[i][0],"of",deck[i][1])

