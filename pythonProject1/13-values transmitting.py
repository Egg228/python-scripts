import math

PI = math.pi

def radius():
    n = float(input("Diametr of celindre: "))
    n /= 2
    return n

def height():
    n = float(input("High of celindre: "))
    return n

def volume():
    r =radius()
    h =height()
    s =PI*r**2
    v =s*h
    return v

print("V of celindre = ",volume())