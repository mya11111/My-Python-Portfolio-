#init
import turtle
import random
ari=turtle.Turtle()
turtle.colormode(255)
#functions
def building (size,color,x,y):
   ari.color(color)
   ari.penup()
   ari.goto(x,y)
   ari.pendown()
   ari.setheading(0)
   ari.pensize(5)
   for i in range(4):
           ari.forward(size)
           ari.left(90)
   ari.forward(size+size/2)
   ari.left(90)
   ari.forward(size)
   ari.left(90)
   ari.forward(size/2)
def water ():
    ari.speed(1000)
    ari.penup()
    ari.color(57,230,230)
    ari.begin_fill()
    ari.goto(-500,-300)
    ari.pendown()
    ari.setheading(0)
    for i in range(4):
        ari.forward(1000)
        ari.right(90)
    ari.end_fill()
def drawCloud(x,y,size):
    ari.penup()
    ari.goto(x,y)
    ari.pendown()
    ari.color("white")
    ari.begin_fill()
    for i in range(6):
        ari.circle(size)
        ari.right(60)
    ari.setheading(0)
    ari.fd(size+size)
    for i in range(6):
        ari.circle(size)
        ari.right(60)
    ari.end_fill()

#Main
ari.speed(100)
ari.dot(5000,107,255,250)
water()
for i in range(10):
   drawCloud(random.randint(-300,300),random.randint(100,250),random.randint(10,15))
for i in range(25):
    building(random.randint(10,100),(random.randint(0,0),random.randint(230,255),random.randint(230,255)),random.randint(-300,300),random.randint(-300,-300))


#heading
#8/30/24
#myaweiss

#initalization
import turtle
mya = turtle.Turtle()
import random
turtle.colormode(255)

#functions
def drawT():
  mya.width(2)
  mya.color("black")
  mya.penup()
  mya.goto(250,-250)
  mya.pendown()
  mya.right(30)
  mya.forward(30)
  mya.left(30)
  mya.forward(30)
  mya.left(90)
  mya.forward(100)
  mya.right(90)
  mya.forward(50)
  mya.left(90)
  mya.forward(60)
  mya.left(90)
  mya.forward(105)
  mya.forward(50)
  mya.left(90)
  mya.forward(60)
  mya.left(90)
  mya.forward(50)
  mya.right(90)
  mya.forward(90)

def drawT_outline():
  mya.width(15)
  mya.color("white")
  for i in range(2):
    mya.right(90)
    mya.forward(10)
  mya.forward(70)
  mya.left(90)
  mya.forward(50)
  for i in range(2):
    mya.right(90)
    mya.forward(80)
  mya.forward(15)
  for i in range(2):
    mya.forward(80)
    mya.right(90)
  mya.forward(50)
  mya.left(90)
  mya.forward(100)
  mya.right(90)
  mya.forward(40)
  mya.right(30)
  mya.forward(40)
  mya.penup()
 
def drawShadow():
  mya.penup()
  mya.goto(140+190,-15-250)
  mya.pendown()
  mya.width(18)
  mya.color(0, 153, 153)
  mya.right(180)
  mya.forward(80)
  mya.right(90)
  mya.forward(50)
  mya.left(90)
  mya.forward(90)
  mya.penup()
  mya.goto(35+190,60-250)
  mya.pendown()
  mya.left(90)
  mya.forward(40)
 
def drawShadow_outline():
  mya.width(3)
  mya.color("black")
  mya.forward(5)
  mya.right(90)
  mya.forward(100)
  mya.right(90)
  mya.forward(210)
  mya.right(90)
  mya.forward(105)
  mya.right(90)
  mya.forward(55)
  mya.left(90)
  mya.forward(80)
  mya.right(90)
  mya.forward(100)
  mya.right(90)
  mya.forward(75)
  mya.left(90)
  mya.forward(55)
  mya.right(90)
  mya.forward(20)
  mya.right(90)
  mya.forward(55)
  mya.right(90)
  mya.forward(40)
  mya.penup()
  mya.goto(130+190,-25-250)
  mya.pendown()
  mya.left(180)
  mya.forward(100)
  mya.right(90)
  mya.forward(50)
  mya.left(90)
  mya.forward(85)
  mya.penup()
  mya.goto(200+190,55-250)
  mya.pendown()
  mya.left(50)
  mya.forward(28)
  mya.penup()
  mya.goto(145+190,55-250)
  mya.pendown()
  mya.right(10)
  mya.forward(25)
  mya.penup()
  mya.goto(95+190,-25-250)
 
def grass():
  mya.pendown()
  mya.color(0, 230, 0)
  mya.forward(40)
  mya.left(80)
  mya.forward(30)
  mya.left(70)
  mya.forward(20)
  mya.left(90)
  mya.forward(50)

def drawHouse():
  mya.speed(1000)
  drawT()
  mya.begin_fill()
  drawT_outline()
  mya.color(102, 255, 255)
  mya.end_fill()
  mya.right(150)
  drawT()
  drawShadow()
  drawShadow_outline()
  mya.begin_fill()
  grass()
  mya.end_fill()

#main
mya.speed(1000)
drawHouse()

#init - Liam White

import turtle
import random

a = turtle.Turtle()
turtle.colormode(255)

#functions
def smallRock(): #Used in mainRock(), creates small purple rocks at bottom
    a.begin_fill()
    a.rt(30)
    a.fd(50)
    a.lt(30)
    a.fd(20)
    a.lt(60)
    a.fd(50)
    a.end_fill()
def sideRock(): #Creates purple rock on side
    a.penup()
    a.goto(random.randint(-400,-300),-400) #random coords
    a.setheading(90)
    a.pendown()
    a.color(244,109,175) #color
    a.begin_fill()
    length = random.randint(30,60) #variable for side length
    a.rt(30)
    a.fd(length) #side length (left)
    a.rt(60)
    a.fd(random.randint(10,30)) #top length
    a.rt(60)
    a.fd(length) #side length (right)
    a.end_fill()
def mainRock(tree): #Creates island, tree parameter decides # of trees
    for i in range(tree): #tree = integer
        a.penup()
        a.color("brown")
        a.goto(random.randint(200,300),random.randint(-265,-260))
        a.pendown()
        a.pensize(2)
        a.setheading(random.randint(85,95))
        a.fd(25)
        a.dot(11,130,random.randint(240,255),random.randint(100,140)) 
    brownRock1()
    grassTop()
    brownRock2()
    blackLine1() 
    blackLine2()
    blackLine3()
    blackLine4()
    smallRocks()
    rockOutline()
    rockPath()
def brownRock1(): #Starts brown rock
    a.color(243,127,125) #brown
    a.penup()
    a.goto(200,-400) #start coords
    a.begin_fill()
    a.setheading(80) #point cursor up
    a.pendown()
    a.fd(55) #straight line on left
    a.lt(70)
    a.circle(-50,90) #curve on left
    a.rt(20)
def grassTop(): #Draws grass hills
    a.color(140,251,102) #green
    a.pensize(15) #make pen wider
    a.bk(5)
    a.circle(-100,70) #first grass curve
    a.penup()
    a.bk(20)
    a.pendown()
    a.lt(50)
    a.circle(-60,70) #second grass curve
def brownRock2(): #Finishes brown rock
    a.pensize(1) #make pen normal
    a.color(243,127,125) #brown
    a.fd(20) #zigzag on right
    a.rt(50) #zigzag on right
    a.fd(50) #zigzag on right
    a.lt(90) #zigzag on right
    a.fd(20) #zigzag on right
    a.rt(90) #zigzag on right
    a.fd(50) #zigzag on right
    a.end_fill()
def blackLine1(): #First crack
    a.color("black")
    a.penup()
    a.goto(250,-400)
    a.setheading(90)
    a.pendown()
    a.lt(10)
    a.fd(30)
    a.lt(70)
    a.fd(5)
    a.rt(65)
    a.fd(10)
    a.rt(10)
    a.fd(20)
    a.lt(20)
    a.fd(30)
    a.rt(20)
    a.fd(30)
    a.rt(3)
    a.fd(10)
    a.penup()
def blackLine2(): #Second crack
    a.color("black")
    a.penup()
    a.goto(270,-400)
    a.setheading(90)
    a.pendown()
    a.fd(20)
    a.lt(10)
    a.fd(30)
    a.fd(10)
    a.rt(30)
    a.fd(5)
    a.lt(30)
    a.fd(25)
    a.lt(10)
    a.fd(5)
    a.rt(10)
    a.fd(41)
    a.penup()
def blackLine3(): #Third crack
    a.goto(290,-400)
    a.setheading(90)
    a.pendown()
    a.rt(20)
    a.fd(50)
    a.lt(30)
    a.fd(20)
    a.rt(5)
    a.fd(25)
    a.rt(3)
    a.fd(31)
    a.penup()
def blackLine4(): #Last crack
    a.goto(330,-400)
    a.setheading(90)
    a.pendown()
    a.rt(5)
    a.fd(50)
    a.lt(5)
    a.fd(10)
    a.lt(20)
    a.fd(15)
    a.rt(25)
    a.fd(53)
    a.penup()
def rockOutline(): #Black Outline
    a.color("black")
    a.pensize(2)
    a.penup()
    a.goto(200,-400) #start coords
    a.setheading(80) #point cursor up
    a.pendown()
    a.fd(55) #straight line on left
    a.lt(70)
    a.circle(-50,77) #curve on left
    a.rt(20)
    a.penup()
    a.goto(352,-281)
    a.pendown()
    a.rt(104)
    a.fd(20) #zigzag on right
    a.rt(50) #zigzag on right
    a.fd(50) #zigzag on right
    a.lt(90) #zigzag on right
    a.fd(20) #zigzag on right
    a.rt(90) #zigzag on right
    a.fd(50) #zigzag on right
    a.penup()
def rockPath(): #Path
    a.goto(355,-285) #start of path
    a.setheading(320) #change direction of turtle
    a.pendown()
    a.color(249,200,127) #light brown
    a.pensize(5) #increase path width
    a.bk(40)
    a.rt(50)
    a.bk(5)
    a.fd(5)
    a.lt(50)
    a.fd(50)
    a.rt(80)
    a.fd(50)
    a.lt(102)
    a.fd(38)
def smallRocks(): #Purple rocks
    a.color(244,109,175) #purple
    a.setheading(180)
    a.goto(340,-400)
    a.pendown()
    smallRock() #purple rock
    a.color(240,100,170) #dark purple
    a.setheading(180)
    a.goto(300,-410)
    smallRock() #dark purple rock
    a.penup()
def finalRocks(tree): #Whole scene drawn by Liam
    sideRock()
    mainRock(tree) #Extends tree parameter to main - integer
#main

finalRocks(5)
