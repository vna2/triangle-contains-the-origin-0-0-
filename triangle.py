def ComputeArea(x1, y1, x2, y2, x3, y3): 
	return abs((x1 * (y2 - y3) + x2 * (y3 - y1) 
				+ x3 * (y1 - y2)) / 2.0) 

from math import sqrt

x1 = float(input("Input value x1: "))
y1 = float(input("Input value y1: "))
x2 = float(input("Input value x2: "))
y2 = float(input("Input value y2: "))
x3 = float(input("Input value x3: "))
y3 = float(input("Input value y3: "))

if ((x2-x1)*(y3-y1) - (y2-y1)*(x3-x1) == 0):
    print('The points dont form a triangle')
else:
    print('The points form a triangle')
    triangleArea = ComputeArea(x1,y1,x2,y2,x3,y3)
    area1 = ComputeArea(0.0,0.0,x2,y2,x3,y3)
    area2 = ComputeArea(x1,y1,0.0,0.0,x3,y3)
    area3 = ComputeArea(x1,y1,x2,y2,0.0,0.0)

    if (triangleArea == (area1+area2+area3)):
        print('The point (0,0) is inside the triangle!')
    else:
        print('The point(0,0) is not inside the triangle!')

