import math

def quadratic_equation(a, b, c):
    d=b*b-4*a*c
    if(d<0):
        return None
    elif(d==0):
        return  -b/(2*a)
    else:
        return (-b-math.sqrt(d))/(2*a),(-b+math.sqrt(d))/(2*a)

print (quadratic_equation(2, 3, 0))
print (quadratic_equation(1, -6, 5))