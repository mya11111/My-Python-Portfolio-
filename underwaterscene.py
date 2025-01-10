#Liam White
#init
import turtle
import random
a = turtle.Turtle()
turtle.colormode(255)

#functions
def drawFish(size,color,x,y):
    a.setheading(0)
    a.color(color)
    a.penup()
    a.goto(x,y)
    a.pendown()
    a.dot(size)
    a.fd(size/3)
    a.lt(30)
    a.begin_fill()
    for i in range(3):
        a.fd(size/1.1)
        a.rt(120)
    a.end_fill()
def seaFloor():
    a.penup()
    a.goto(-800,-100)
    a.pendown()
    a.setheading(0)
    a.color(168,136,62)
    a.begin_fill()
    for i in range(4):
        a.fd(1600)
        a.rt(90)
    a.end_fill()


#myaweiss

#initalization
import turtle
mya = turtle.Turtle()
import random

#functions
def drawElement(size,color,x,y):
  mya.penup()
  mya.goto(x,y)
  mya.pendown()
  mya.color(color)
  mya.pensize(25)
  for i in range (2):
    mya.forward(size)
    mya.left(20)
    mya.forward(size)
    mya.right(160)
    mya.forward(size)
    mya.left(20)
    mya.forward(size)
    mya.right(160)
  for i in range(2):
    mya.forward(size)

def draw_all_element():
  for i in range(3):
    drawElement(random.randint(20,60),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.randint(-300,300),random.randint(-50,350))


#jamari

#intialization
import turtle
import random
turtle.colormode(255)
ari=turtle.Turtle()
#Functions
def seaweed (size,color,x,y):
    ari.color(color)
    ari.pensize(5)
    ari.setheading(90)
    ari.setheading(360)
    ari.penup()
    ari.goto(x,y)
    ari.pendown()
    for i in range(3):
        ari.circle(size,180)
        ari.circle(-size,180)
        ari.forward(10)



#All Functions
def oceanScene():
    a.speed(100) #Speeds up drawing
    a.dot(5000,"blue") #Blue sea background
    seaFloor() #Brown sea floor
    drawFish(50,(255,185,23),100,0) #Default orange fish
    for i in range(5): #5 random size and shape fish
        drawFish(random.randint(20,50),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.randint(-400,400),random.randint(-70,400))
    draw_all_element() #starfish
    for i in range (4): #seaweed
        seaweed(random.randint(10,30),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.randint(-300,300),random.randint(-100,-100))

#All Main
oceanScene() #final scene
