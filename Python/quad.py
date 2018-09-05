from math import *

from os import system

print("Epic Quadratic Solver")

print("Enter The Coefficient For ax^2+bx+c=0")

def descriminant(a,b,c):
        return ((b**2)-(2*a*c))

def sol(a,b,c):
    
    sol = [round((-b-sqrt(descriminant(a,b,c))/(2*a))), round((-b+sqrt(descriminant(a,b,c))/(2*a)))]
    return sol

while True:

    a = float(input("a = "))

    b = float(input("b = "))

    c = float(input("c = "))

    if descriminant(a,b,c) < 0:
        print("No Real Roots")

    else:
        theResult = sol(a,b,c)
        for stuff in theResult:
            print("hey, here's a root: ",stuff)
        #print(sol(a,b,c))

