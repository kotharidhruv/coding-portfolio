import turtle as trtl

painter = trtl.Turtle()

def makeSquare(size): #Draws a square with a given size
    for _ in range(4):
        painter.forward(size)
        painter.right(90)

def drawBackground(): #Draws the blue sky background
    painter.penup()
    painter.goto(-475, -500)
    painter.setheading(90)
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor("#00BFFF")
    makeSquare(1000)
    painter.end_fill()

drawBackground()

def drawGrass(): #Draws the grass that the house and the people are standing on
    painter.penup()
    painter.goto(-475,-100)
    painter.setheading(0)
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor("green")
    painter.forward(1000)
    painter.right(90)
    painter.forward(400)
    painter.right(90)
    painter.forward(1000)
    painter.right(90)
    painter.forward(400)
    painter.end_fill()

drawGrass()

painter.penup()
painter.goto(0,0)
painter.setheading(0)
painter.pendown()

def makePerson(scale): #Draws a person with a given scale
    painter.begin_fill()
    painter.fillcolor("#c68642")
    painter.circle(scale*25)
    painter.end_fill()
    painter.left(90)
    painter.penup()
    painter.forward(scale*50)
    painter.pendown()
    painter.forward(scale*75)
    painter.left(45)
    painter.forward(scale*60)
    painter.back(scale*60)
    painter.right(90)
    painter.forward(scale*60)
    painter.back(scale*60)
    painter.right(135)
    painter.forward(scale*(75/2))
    painter.left(90)
    painter.forward(scale*30)
    painter.back(scale*30)
    painter.right(180)
    painter.forward(scale*30)
    painter.penup()

def makeEyes(x,y): #Draws eyes at given coordinates
    painter.goto(0,0)
    painter.right(90)
    painter.forward(50)
    painter.goto(x,y)
    painter.back(7)
    painter.right(90)
    painter.forward(3)
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor("white")
    painter.circle(3)
    painter.end_fill()
    painter.penup()
    painter.left(90)
    painter.forward(3)
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor("black")
    painter.circle(1)
    painter.penup()
    painter.back(3)
    painter.right(90)
    painter.back(10)
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor("white")
    painter.circle(3)
    painter.end_fill()
    painter.penup()
    painter.left(90)
    painter.forward(3)
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor("black")
    painter.circle(1)
    painter.penup()
    painter.forward(7)
    painter.right(90)
    painter.pendown()
    painter.forward(10)
    painter.penup()
    painter.goto(0,0)

def makeHair(scale, x, y): #Worked along with AI to write this function which draws hair at the given coordinates at a given scale
    painter.penup()
    painter.goto(x - scale * 25, y + scale * 25)
    painter.pendown()
    painter.pensize(2)
    painter.pencolor("black")
    
    for i in range(10):
        painter.penup()
        painter.goto(x - scale * 25 + i * scale * 5, y + scale * 30)
        painter.pendown()
        painter.goto(x - scale * 25 + i * scale * 5, y + scale * 10)
    
    for side in [-1, 1]:
        for _ in range(10):
            painter.penup()
            painter.goto(x + side * scale * 25, y + scale * 30 - _ * scale * 5)
            painter.pendown()
            painter.goto(x + side * scale * 25 + side * scale * 10, y - scale * 50)

    


#The house structure under the roof is drawn using the following code:
painter.begin_fill()
painter.fillcolor("#bd952a")

makeSquare(100)

painter.end_fill()

#The roof is drawn using the following code:
painter.begin_fill()
painter.fillcolor("red")

painter.left(45)
painter.forward(75)
painter.right(90)
painter.forward(75)

painter.end_fill()


painter.penup()
painter.goto(25, -50)

#Draws the door of the house
painter.pendown()
painter.begin_fill()
painter.fillcolor("brown")
painter.right(45)
painter.forward(50)
painter.left(90)
painter.forward(40)
painter.left(90)
painter.forward(50)
painter.end_fill()

painter.penup()
painter.forward(15)
painter.pendown()

#Draws the windows of the house
painter.begin_fill()
painter.fillcolor("lightblue")
makeSquare(20)
painter.end_fill()

painter.penup()
painter.left(90)
painter.forward(35)

painter.pendown()
painter.begin_fill()
painter.fillcolor("lightblue")
makeSquare(20)
painter.end_fill()

#Makes the first person (AKA the father)
makePerson(0.5)
makeEyes(25,-50)

painter.goto(75,-35)

#Draws the second person (AKA the mother)
makePerson(0.5)
makeEyes(75,-50)
makeHair(0.5, 75, -45) 

painter.penup()
painter.goto(125,-65)
painter.pendown()
painter.pensize(1)

#Draws the third person (AKA the child)
makePerson(0.4)
makeEyes(125,-80)
makeHair(0.4, 125, -75)



painter.penup()
painter.goto(175, 48)

#Draws the sun
painter.pendown()
painter.begin_fill()
painter.fillcolor("yellow")
painter.circle(15)
painter.end_fill()

for i in range(0, 360, 30): #Used AI to generate this code in which the sun rays are drawn and coming out of the circle.
    painter.penup()
    painter.goto(175, 30)
    painter.setheading(i)
    painter.forward(15)
    painter.pendown()
    painter.forward(25)

#Draws the horse
def draw_horse(x, y, scale=1):
    def draw_body():
        painter.penup()
        painter.goto(x - 100 * scale, y - 50 * scale)
        painter.pendown()
        painter.begin_fill()
        painter.fillcolor("#633E13")
        painter.setheading(0)
        painter.forward(150 * scale)
        painter.left(90)
        painter.forward(50 * scale)
        painter.left(90)
        painter.forward(150 * scale)
        painter.left(90)
        painter.forward(50 * scale)
        painter.end_fill()

    def draw_head():
        painter.penup()
        painter.goto(x + 50 * scale, y)
        painter.pendown()
        painter.begin_fill()
        painter.fillcolor("#633E13")
        painter.setheading(45)
        painter.forward(40 * scale)
        painter.right(45)
        painter.forward(30 * scale)
        painter.right(45)
        painter.forward(40 * scale)
        painter.right(135)
        painter.forward(40 * scale)
        painter.end_fill()

    def draw_legs():
        painter.penup()
        painter.goto(x - 90 * scale, y - 50 * scale)
        painter.pendown()
        for _ in range(2):
            painter.setheading(270)
            painter.forward(40 * scale)
            painter.backward(40 * scale)
            painter.penup()
            painter.forward(30 * scale)
            painter.pendown()

        painter.penup()
        painter.goto(x + 30 * scale, y - 50 * scale)
        painter.pendown()
        for _ in range(2):
            painter.setheading(270)
            painter.forward(40 * scale)
            painter.backward(40 * scale)
            painter.penup()
            painter.forward(30 * scale)
            painter.pendown()

    def draw_tail():
        painter.penup()
        painter.goto(x - 100 * scale, y)
        painter.setheading(180)
        painter.pendown()
        painter.forward(30 * scale)
        painter.left(45)
        painter.forward(30 * scale)
        painter.backward(30 * scale)
        painter.right(90)
        painter.forward(30 * scale)
        painter.backward(30 * scale)

    def draw_mane():
        painter.penup()
        painter.goto(x - 50 * scale, y)
        painter.setheading(90)
        painter.pendown()
        for _ in range(5):
            painter.forward(15 * scale)
            painter.backward(15 * scale)
            painter.penup()
            painter.forward(10 * scale)
            painter.pendown()

    def draw_eyes():
        painter.penup()
        painter.goto(x + 65 * scale, y + 15 * scale)
        painter.pendown()
        painter.dot(10 * scale, "black")

        painter.penup()
        painter.goto(x + 85 * scale, y + 15 * scale)
        painter.pendown()
        painter.dot(10 * scale, "black")
    
    #Puts all the parts of the horse together
    draw_body()
    draw_head()
    draw_legs()
    draw_tail()
    draw_eyes()


painter.penup()
painter.goto(500, -100)
draw_horse(250,-75,scale=0.5)



wn = trtl.Screen()
wn.mainloop()
