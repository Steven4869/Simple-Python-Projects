#Area and perimeter calculator
print("Welcome to Area and perimeter calculator\n")
a=int(input("For circle Press 1\n For square press 2\n For rectangle Press 3\n"))
if(a==1):
    r=float(input("Please enter the radius of circle\n"))
    Area=3.14*r*r
    Perimeter=2*3.14*r
    print("Area of circle is",Area,"Perimeter is",Perimeter)
elif(a==2):
    b=float(input("Please enter the side of square\n"))
    Area=b*b
    Perimeter=4*b
    print("Area of square is",Area,"Perimeter is",Perimeter)
elif(a==3):
    c=float(input("Please enter the length of rectangle\n"))
    d=float(input("Please enter the breadth of rectangle\n"))
    Area=c*d
    Perimeter=4*(c+d)
    print("Area of rectangle is",Area,"Perimeter is",Perimeter)
else:
    print("Not the correct input")