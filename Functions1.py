#Create a polygon function that accepts a turtle, sides, and distance.
#function file

def coolSquared2(t,d,c1,c2):#makes square with 4 maltese crosses
    for times in range(4):
        coolSquared(t,d,c1,c2)
        t.forward(d*2)
        t.right(90)

def jump(t,x,y):#moves the pen to x, y coordinates on the page 
    t.penup()
    t.goto(x,y)
    t.pendown()
  
def rightcurve(t):#makes a right curve
    
    for n in range(20):
        t.begin_fill()
        t.circle(n)
        t.forward(n)
        t.left(n)
        t.end_fill()

def leftcurve(t):#makes a left curve
    
    for n in range(20):
        t.begin_fill()
        t.circle(n)
        t.forward(n)
        t.right(n)
        t.end_fill()
    
    
def ballons(t,r):#makes 4 little light blue-dark blue circles looks like baloons
    for c in ['light blue','blue','light blue','blue']:
        t.begin_fill()
        t.color(c)
        t.circle(r)
        t.right(90)
        t.end_fill()

def star(t,d,c):#makes one 8 sided star
    t.begin_fill()
    t.color(c)
    for times in range(8):
        t.forward(d)
        t.left(135)

    t.end_fill()

def stars(t,c):#makes a circle of 8 sided stars
    for times in range(8):
        star(t,times *10 + 8,c)
        t.penup()
        t.right(20)
        t.forward(80)
        t.pendown()


def funky(t,d,c1,c2):#makes a triangle with 2 colors
    t.color(c1)
    polygon(t,3,d)
    t.color(c2)
    polygon(t,3,d/2)
        

def box(t,d,c,ds):#makes a rectangle
    t.begin_fill()
    for times in range(2):
        t.color(c)
        t.forward(d)
        t.right(90)
        t.forward(ds)
        t.right(90)

    t.end_fill()


def my_draw_function(bob):
    bob.forward(100)#try different values for forward
    bob.left(255)#try different angles - larger angles tighter the turns

def penmovement_right(bob):
    bob.penup()
    bob.right(40)#try different angles to move the designs around the screen
    bob.forward(200)
    bob.pendown()

def penmovement_left(bob):#moves the pen left 200
	bob.penup()
	bob.left(270)
	bob.forward(200)
	bob.pendown()
    
def purple_star(bob):
    bob.color("purple")#use different colors for the pen
    for x in range(36):#try different values for the interations
         my_draw_function()
         
def sun(bob):# draws a circle with 36 triangle that look like a sun
    sides = 3
    angle = 360/sides
    distance = 90
    angle2 = 10
    bob.color('orange')
    bob.pensize(10)
    for times in range(36):
        for x in range(3):
            bob.forward(distance)
            bob.left(angle)
 
        bob.forward(distance)
        bob.right(angle2)   


def eye(bob): #draw eye, 18 sided polygon used as an eye
    bob.color("blue")         # makes the pen blue
    for x in range(18):       # for loop to repeat the next comands 18 times
        bob.forward(140)      # go forward 140
        bob.left(100)         # go left 100 degrees

def move_left(bob):
    bob.penup()               # picks the pen up
    bob.right(80)             # turns right 80 degrees
    bob.forward(300)          # moves forward 300
    bob.pendown()             #puts pen down


def eyes(bob): #draws 2 eyes
    eye(bob) 
    move_left(bob)
    eye(bob)     
