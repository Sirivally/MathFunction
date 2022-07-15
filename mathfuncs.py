import math
def square(s):
    area=s*s
    perimeter=4*s
    diagonal=s*math.sqrt(2)
    print("Area: ",area)
    print("Perimeter: ",perimeter)
    print("Diagonal: ",diagonal)
def rectangle(l,b):
    area=l*b
    perimeter=2*(l+b)
    diagonal=math.sqrt(l*l+b*b)
    print("Area: ",area)
    print("Perimeter: ",perimeter)
    print("Diagonal: ",diagonal)
def triangle(a,b,c,h):
    area=b*h/2
    perimeter=a+b+c
    print("Area: ",area)
    print("Perimeter: ",perimeter)
def circle(r):
    area=math.pi*r*r
    circumference=2*math.pi*r
    print("Area: ",area)
    print("circumference: ",circumference)
def semicircle(r):
    area=math.pi*r*r/2
    circumference=(math.pi+2)*r
    print("Area: ",area)
    print("circumference: ",circumference)
def rhombus(s,d1,d2):
    area=d1*d2/2
    perimeter=4*s
    print("Area: ",area)
    print("Perimeter: ",perimeter)
def cube(s):
    lateralsurfaceArea=4*s*s
    totalsurfaceArea=6*s*s
    volume=s*s*s
    print("Lateral surface area: ",lateralsurfaceArea)
    print("Total surface area: ",totalsurfaceArea)
    print("volume: ",volume)
def cuboid(l,b,h):
    lateralsurfaceArea=2*h*(l+b)
    totalsurfaceArea=2*(l*b+b*h+b*l)
    volume=l*b*h
    print("Lateral surface area: ",lateralsurfaceArea)
    print("Total surface area: ",totalsurfaceArea)
    print("volume: ",volume)
def sphere(r):
    lateralsurfaceArea=4*math.pi*r*r
    totalsurfaceArea=4*math.pi*r*r
    volume=(4/3)*math.pi*r*r
    print("Lateral surface area: ",lateralsurfaceArea)
    print("Total surface area: ",totalsurfaceArea)
    print("volume: ",volume)
def cylinder(r,h):
    lateralsurfaceArea=2*math.pi*r*h
    totalsurfaceArea=2*math.pi*r*(r+h)
    volume=math.pi*r*r*h
    print("Lateral surface area: ",lateralsurfaceArea)
    print("Total surface area: ",totalsurfaceArea)
    print("volume: ",volume)
def cone(r,h,l):
    lateralsurfaceArea=math.pi*r*l
    totalsurfaceArea=math.pi*r*(l+r)
    volume=(1/3)*math.pi*r*r*h
    print("Lateral surface area: ",lateralsurfaceArea)
    print("Total surface area: ",totalsurfaceArea)
    print("volume: ",volume)