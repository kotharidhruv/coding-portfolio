import turtle as trtl
import random as rand

t = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()

wn = trtl.Screen()

spot_color = "blue"
spot_size = 2
spot_shape = "circle"
score = 0
timer = 30
counter_interval = 1000
timer_up = False
first_click = False

colors = ["red", "orange", "yellow", "green", "purple", "pink", "brown", "white", "gray"]
sizes = [0.5, 1, 1.5, 2, 2.5, 0.7, 0.8]

wn.bgcolor("black")

t.color(spot_color)
t.shape(spot_shape)
t.shapesize(spot_size)

score_writer.penup()
score_writer.color("white")
score_writer.goto(-370,270)

counter.penup()
counter.color("white")
counter.goto(0,270)

font_setup = ("Arial", 20, "normal")

def change_position():
    new_xpos = rand.randint(-400,400)
    new_ypos = rand.randint(-300,300)
    t.penup()
    t.goto(new_xpos,new_ypos)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def change_color():
    new_color = rand.choice(colors)
    t.color(new_color)
    t.stamp()

def change_size():
    new_size = rand.choice(sizes)
    t.shapesize(new_size)
    t.stamp()

def spot_clicked(x,y):
    global first_click
    if first_click == False:
        wn.ontimer(countdown, counter_interval)
        first_click = True
    if timer_up == False:
        change_position()
        update_score()
        change_color()
        change_size()
        t.color(spot_color)
    else:
        t.hideturtle()

def start():
   t.onclick(spot_clicked)

start()

wn.mainloop()