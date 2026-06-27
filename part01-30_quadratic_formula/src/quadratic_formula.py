# Write your solution here

from math import sqrt
a=int(input("Value of a: "))
b=int(input("Value of b: "))
c=int(input("Value of c: "))

x1=(-b + sqrt((b**2) - (4*a*c)))/(2*a)
x2=(-b - sqrt((b**2) - (4*a*c)))/(2*a)
print(f"The roots are {x1} and {x2}")