# a123_apple_random.py
import turtle as trtl
import random

#-----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
background_image = "background.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.bgpic(background_image)

apple = trtl.Turtle()
writer = trtl.Turtle()

writer.hideturtle()
apple.hideturtle()

# List of letters (home row: "asdfghjkl"; full alphabet: "abcdefghijklmnopqrstuvwxyz")
letters = list("asdfghjkl")  # Replace with list("abcdefghijklmnopqrstuvwxyz") for the full alphabet

current_letter = ""  # To track the currently displayed letter

#-----functions-----
# Given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
    active_apple.shape(apple_image)
    active_apple.showturtle()
    wn.update()

# Display the random letter on the apple
def display_letter(letter):
    writer.clear()
    writer.goto(apple.xcor() - 18, apple.ycor() - 35)
    writer.write(letter.upper(), font=("Arial", 40, "bold"))

# Drop the apple when the correct key is pressed
def apple_fall():
    apple.penup()
    writer.clear()
    while apple.ycor() > -200:
        apple.goto(apple.xcor(), apple.ycor() - 1)
        wn.update()
    reset_apple()

# Reset the apple to the top with a new letter
def reset_apple():
    global current_letter
    if letters:  # Check if letters are still available
        current_letter = letters.pop(random.randint(0, len(letters) - 1))
        apple.goto(random.randint(-200, 200), 150)
        draw_apple(apple)
        display_letter(current_letter)
    else:
        writer.goto(0, 0)
        writer.write("Game Over!", align="center", font=("Arial", 40, "bold"))

#-----event bindings-----
def bind_keys():
    for letter in letters:  # Bind each key directly
        wn.onkeypress(apple_fall, letter)

#-----main-----
reset_apple()  # Initialize the first apple
bind_keys()

wn.listen()
wn.mainloop()
