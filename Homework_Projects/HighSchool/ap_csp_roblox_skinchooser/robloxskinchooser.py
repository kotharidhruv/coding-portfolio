import turtle as trtl

t = trtl.Turtle()
t.speed(0)

#list of the accepted colors
accepted_colors = ["red","orange","yellow","green","blue","purple","black","white"]

class Character():
    def __init__(self, width, height, head_color, body_color, arm_color, leg_color):
        self.width = width
        self.height = height
        self.head_color = head_color
        self.body_color = body_color
        self.arm_color = arm_color
        self.leg_color = leg_color

    def draw_rectangle(self, x, y, width, height, color):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        for i in range(2):
            t.forward(width)
            t.right(90)
            t.forward(height)
            t.right(90)
        t.end_fill()

    def draw_head(self):
        self.draw_rectangle(-25, 50, 50, 50, self.head_color)

    def draw_face(self):
        #Drawing the eyes
        t.penup()
        t.goto(-13, 30)
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        t.circle(2)
        t.end_fill()
        t.penup()
        t.goto(6, 30)
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        t.circle(2)
        t.end_fill()

        #Drawing the mouth
        t.penup()
        t.goto(8,15)
        t.pendown()
        t.setheading(-90)
        for deg in range(180):
            t.forward(0.2)
            t.right(1)

        t.setheading(0)


    def draw_body(self):
        self.draw_rectangle(-50, 0, 100, 100, self.body_color)

    def draw_arms(self):
        self.draw_rectangle(-89, 0, 40, 75, self.arm_color)
        self.draw_rectangle(50, 0, 40, 75, self.arm_color)

    def draw_legs(self):
        self.draw_rectangle(-47.5, -100, 50, 75, self.leg_color)
        self.draw_rectangle(3.5, -100, 50, 75, self.leg_color)

    def draw_character(self):
        self.draw_head()
        self.draw_face()
        self.draw_body()
        self.draw_arms()
        self.draw_legs()

head_color = input("Enter the head color: ")
body_color = input("Enter the body color: ")
arm_color = input("Enter the arm color: ")
leg_color = input("Enter the leg color: ")

#Checking if the colors the user inputted are valid
if head_color not in accepted_colors or body_color not in accepted_colors or arm_color not in accepted_colors or leg_color not in accepted_colors:
    print("Never heard of this color, try again.")
else:
    character = Character(100, 150, head_color, body_color, arm_color, leg_color)
    character.draw_character()

# Hide the turtle
t.hideturtle()

# Keep the window open
trtl.done()