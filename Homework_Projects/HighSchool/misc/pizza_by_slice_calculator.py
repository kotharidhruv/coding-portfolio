pizzaCost=int(input("What is the price of your pizza?"))
size=int(input("What is the size of your pizza in inches?"))
count=int(input("How slices of pizza would you like?"))

for x in range(0,count):
    for j in range(0,x-1):
        print("🍕",end="")
    print("/r")

def areaFormula(s):
    pi=3.14
    r=size/2
    s = pi*r**2
    return(s)

def costPerArea(c):
    pizzaCost/areaFormula(size)
    return(c)


finalArea=str(int(areaFormula(size)))
finalCostPerArea=str(int(costPerArea(pizzaCost)))

print("The area of your pizza is approximately " + finalArea + " square inches, the cost per square inch of this pizza is about " + "$"+finalCostPerArea+" per square inch")

