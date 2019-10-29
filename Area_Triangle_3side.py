# program for calculating the three sides of area of Triangle
import math
a = int(input('Enter The First value '))
b = int(input('Enter The Second value '))
c = int(input('Enter The Third value '))

s = (a+b+c) / 2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(area)