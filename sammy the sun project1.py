#Sammy the sun project 1 
import turtle             # allows this program to use the turtle library
import Functions1         # allows this program to use my function file
turtle.bgcolor("yellow")  # makes the background orange
bob = turtle.Turtle()     # creates a turtle named bob
bob.speed(0)              # speed is 0
bob.pensize(3)            # thickness of the line is 3

# moves left and up from center 
bob.penup()               # picks the pen up
bob.right(190)            # turns right 190 degrees
bob.forward(250)          # goes foward 250
bob.right(90)             # makes a right 90 degree turn
bob.forward(100)          # goes forward 100
bob.pendown()             # put the pen back down to start to draw

Functions1.eyes(bob)       # makes two 18 sided polygon eyes
   
for x in range(2):        #for loop to move right twice the distance
    Functions1.penmovement_right(bob)#moves pen right
    
#makes 12 sided star to start the mouth
bob.color("red")          # makes the pen red
for x in range(12):       # for loop to repeat the next commands 12 times
    bob.forward(150)      # goes forward 150
    bob.left(150)         # goes left 150 degrees
Functions1.penmovement_right(bob) # goes right 40, then goes forward 200

#makes a smile made out of 8 sided stars  
Functions1.stars(bob,"red") # draws eight 8 sided stars

#draws the nose
Functions1.penmovement_right(bob)#moves the pen to where the nose should be
Functions1.ballons(bob,20)  # draws 4 ballons that look like a nose
bob.penup()                 # picks the pen up
bob.right(60)               # turns right 60 degrees
bob.forward(700)            # goes forward 700
bob.right(130)              # turns right 130 degrees
bob.forward(300)            # goes forward 300

bob.pendown()               # puts the pen down
Functions1.sun(bob)         # drwas a 36 triangular sun to make the face


turtle.done()               # stops the program

