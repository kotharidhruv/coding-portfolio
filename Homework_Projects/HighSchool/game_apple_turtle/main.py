#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()
writer = trtl.Turtle()

writer.hideturtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_fall():
  apple.penup()
  writer.clear()
  while apple.ycor() > -200:
    apple.goto(apple.xcor(), apple.ycor()-1)
    wn.update()

def draw_a():
  writer.goto(apple.xcor()-18, apple.ycor()-35)
  writer.write("A", font=("Arial", 40, "bold"))


#-----function calls-----
draw_apple(apple)
draw_a()
wn.onkeypress(apple_fall,"a")


wn.listen()

wn.mainloop()