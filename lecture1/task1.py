from math import sqrt, cos, radians

b = float(input())
c = float(input())
alfa = float(input())

if b <= 0 or c <= 0 or alfa <= 0:
    print("error")
else:  
    a = sqrt(b**2 + c**2 - 2*b*c*cos(radians(alfa)))   

    print(round(a, 4))
