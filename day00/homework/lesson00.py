from turtle import *


#we want to paint a house

#step:1 drawing a square

speed(20)

color("green")
width(5)
forward(230)
left(90)

forward(230)
left(90)

forward(230)
left(90)

forward(230)
left(90)
#end of square

#step2: drawing a door

forward(90)
left(90)

color("yellow")
begin_fill()
forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()

#end of door

penup()
goto(230, 230)
pendown()

#step3: drawing  a roof
color("red")
begin_fill()
right(140)
forward(180)
left(100)
forward(180)
end_fill()

#end of roof

#step4: drawing a window

penup()
goto(20, 150)
pendown()
color("blue")

right(140)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(25)

right(90)
forward(50)

left(90)
forward(25)

left(90)
forward(25)

left(90)
forward(50)

penup()
goto(210, 150)
pendown()

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(25)

right(90)
forward(50)

right(90)
forward(25)

right(90)
forward(25)

right(90)
forward(50)

#end of drawing a window



exitonclick()