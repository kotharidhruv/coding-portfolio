Original image:
![image](https://github.com/kotharidhruv/reacreationOfHouse/blob/9ab482a4d56dc4f3a644f0371371a94817b1ca6c/IMG_4278.HEIC)

# Functions used

## makeSquare
Takes the a given size and uses a for loop to keep on going forward based on the scale and right 90 degrees 4 times.

## drawBackground
Painter goes to the corner of screen and uses makeSquare function to build a 1000x1000 sqaure background.

## drawGrass
Painter travels to the bottom left corner of the screen and draws a 1000x400 green rectangle.

## makePerson 
Takes the scale and goes through a series of moves relative to the scale and turns to create a stickman shape with human colors.

## makeEyes
Take the coordinates of where the eyes should be and draws the eyes at that coordinate.

## makeHair
Takes the scale and coordinates to draw hair using a series of for loops to make the painter go up and down as if it were scribbling to resemble hair.

## draw_horse
Contains a series of functions which are called together to build a basic drawing of a horse/mustang

## draw_head
Draws a head of a horse using painter movements to create a trapezoid. Called in the draw_horse function.

## draw_legs
Draws two front legs and two back legs. Called in the draw_horse function.

## draw_eyes
Draws two eyes at the head of the horse. Called in the draw_horse function.

