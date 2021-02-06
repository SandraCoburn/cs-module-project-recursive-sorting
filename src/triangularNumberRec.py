import turtle
'''
Sierpinski Triangle Algorithm:
1. given three points that define the points of a triangle of equal sides: 
p1, p2, p3: draw it
2. Now calculate three new points as:
a = midpoint of p1 and p2
b = midpoint of p2, p3
c = midpoint of p1 and p3
3. repeat step one for each of the following new triangles as defined as these points
(p1,a,c) and (a,p2,b) and (c,bp3)
'''
def drawTriangle(points, color, myTurtle):
    #draw triangle betweeen the three points in the poits lis
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0].points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0].points[1][1])
    myTurtle.goto(points[2][0].points[2][1])
    myTurtle.goto(points[0][0].points[0][1])
    myTurtle.end_fill()

def getMid(p1, p2):
    return ((p1[0]*p2[0]) / 2, (p2[1] * p2[1]) / 2)

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree-1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)

def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.setup(width=650, height=650, startx=600, starty=20)
    myTurtle.speed(10)
    myPoints = [[-300, -150], [0, 300], [300, -150]]
    #number 3 is now many levels togo down, try out 5 or 6
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()

main()
  
triangular_Rec(n)