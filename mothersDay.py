#heading
#teddybear
#myaweiss
#liamwhite

#initalization
import turtle
mya = turtle.Turtle() #Mya
a = turtle.Turtle() #Liam
pen = turtle.Turtle() #Mya

#functions
def bodyOutline(): #this function makes the black outline of the body
  mya.penup()
  mya.goto(0,0)
  mya.pendown()
  mya.pencolor("black")
  mya.left(180)
  mya.circle(75)
def body(): #this function makes the brown circle body
  mya.penup()
  mya.goto(0,-150)
  mya.circle(75)
  mya.color("#debea0")
def frontLeftPaw(): #this function makes the brown left circular paw
  mya.penup()
  mya.goto(-60,-20)
  mya.circle(30)
  mya.color("#f2e5d9")
def frontLeftPawOutline(): #this function makes the black outline of the left circular paw
  mya.penup()
  mya.goto(-60,-20)
  mya.pendown()
  mya.pencolor("black")
  mya.circle(30)
def chest(): #this function lets me move the turtle across the chest to the right paw invisibly
  mya.penup()
  mya.goto(60,-20)
def frontRightPaw(): #this function makes the right brown circular paw and its black outline
  mya.pendown()
  mya.circle(30)
  mya.color("#f2e5d9")
def waist(): #this function moves the turtle down the waist to the bottom right paw invisibly
  mya.penup()
  mya.goto(30,-130)
def bottomRightPaw(): #this function makes the brown ovalular bottom right paw
  mya.pendown()
  mya.pencolor("#f2e5d9")
  mya.left(45)
  mya.circle(30,180)
  mya.forward(25)
  mya.circle(30,180)
  mya.forward(25)
def bottomRightPawOutline(): #this function makes the ovalular bottom right paws black outline
  mya.pencolor("black")
  mya.circle(30,180)
  mya.forward(25)
  mya.circle(30,180)
  mya.forward(25)
def bottom(): #this function moves the turtle invisibly along the body to the bottom left paw
  mya.penup()
  mya.right(45)
  mya.forward(60)
def bottomLeftPaw(): #this function makes the brown ovalular bottom left paw
  mya.pencolor("#f2e5d9")
  mya.right(45)
  mya.forward(25)
  mya.circle(30,180)
  mya.forward(25)
  mya.circle(30,180)
def bottomLeftPawOutline(): #this function makes the ovalular bottom left paws black outline
  mya.pendown()
  mya.pencolor("black")
  mya.forward(25)
  mya.circle(30,180)
  mya.forward(25)
  mya.circle(30,180)

def teddyHead(): #This makes the base of the head (the brown circle)
    #Head
    a.color("#debea0")
    a.begin_fill()
    a.penup()
    a.goto(0,-10)
    a.pendown()
    a.circle(75)
    a.end_fill()
    #Black Outline
    a.color("Black")
    a.circle(75)
def teddyEyes(): #This makes the eyes
    a.color("Black")
    a.penup()
    #Left Eye
    a.goto(-30,70)
    a.pendown()
    a.begin_fill()
    a.circle(10)
    a.end_fill()
    a.penup()
    #Right Eye
    a.goto(30,70)
    a.pendown()
    a.begin_fill()
    a.circle(10)
    a.end_fill()
def teddyNose(): #This makes the nose (black circle, tan circle, mouth)
    #Light Brown Circle
    a.penup()
    a.goto(0,0)
    a.pendown()
    a.color("#f2e5d9")
    a.begin_fill()
    a.circle(35)
    a.end_fill()
    a.penup()
    #Black Nose
    a.goto(0,25)
    a.pendown()
    a.color("Black")
    a.begin_fill()
    a.circle(18)
    a.end_fill()
    #Mouth
    a.penup()
    a.goto(0,15)
    a.pendown()
    a.right(30)
    a.circle(15,100)
    a.penup()
    a.goto(0,15)
    a.pendown()
    a.left(150)
    a.circle(-15,100)
    a.penup()
    a.goto(0,0)
def teddyEars(): #This makes the ears (brown and tan circles)
    a.color("#debea0")
    #Left Ear
    a.begin_fill()
    a.penup()
    a.goto(-50,90)
    a.pendown()
    a.circle(35)
    a.end_fill()
    #Right Ear
    a.begin_fill()
    a.penup()
    a.goto(50,90)
    a.pendown()
    a.circle(35)
    a.end_fill()
    #Left Ear Outline
    a.color("Black")
    a.penup()
    a.goto(-50,90)
    a.pendown()
    a.circle(35)
    #Right Ear Outline
    a.color("Black")
    a.penup()
    a.goto(50,90)
    a.pendown()
    a.circle(35)
    #Left Ear Inner
    a.color("#f2e5d9")
    a.begin_fill()
    a.penup()
    a.goto(-45,95)
    a.pendown()
    a.circle(25)
    a.end_fill()
    #Right Ear Inner
    a.color("#f2e5d9")
    a.begin_fill()
    a.penup()
    a.goto(45,95)
    a.pendown()
    a.circle(25)
    a.end_fill()
def drawStar(): #Draws a star (use goto before)
    a.pendown()
    a.color("#ffce42")
    a.begin_fill()
    for i in range(6):
        a.fd(10)
        a.rt(120)
        a.fd(10)
        a.lt(60)
    a.end_fill()

def curve():
  for i in range(200):
    pen.right(1)
    pen.forward(1)

def heart():

    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def txt():
    
    pen.up()
    pen.setpos(-90, -100)
    pen.down()
    pen.color('black')

    pen.write("Happy Mothers Day", font=("Verdana", 12, "bold"))


def drawScene():
    mya.speed(3)
    mya.begin_fill()
    body()
    mya.end_fill()
    bodyOutline()
    mya.begin_fill()
    frontLeftPaw()
    mya.end_fill()
    frontLeftPawOutline()
    chest()
    mya.begin_fill()
    frontRightPaw()
    mya.end_fill()
    waist()
    mya.begin_fill()
    bottomRightPaw()
    mya.end_fill()
    bottomRightPawOutline()
    bottom()
    mya.begin_fill()
    bottomLeftPaw()
    mya.end_fill()
    bottomLeftPawOutline()
    a.speed(3)
    teddyEars()
    teddyHead()
    teddyEyes()
    teddyNose()
    a.penup()
    a.goto(100,100)
    drawStar()
    a.penup()
    a.goto(-120,10)
    drawStar()
    a.penup()
    a.goto(-20,180)
    drawStar()
    pen.penup()
    pen.goto(0,-200)
    pen.pendown()
    heart()
    txt()
    pen.penup()
    pen.goto(0,0)


#Main

drawScene()
