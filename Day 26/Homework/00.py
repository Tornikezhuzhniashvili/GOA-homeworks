from turtle import *
speed(30)
      
def triangle(a):
    if a % 2 == 0:
        color("red")
    else:
        color("black")
    
    begin_fill()
    forward(200)
    left(120)
    forward(100)
    forward(100)
    end_fill()
    penup()
    left(30)
    left(90)
    forward(200)
    left(30)
    forward(200)
    left(90)



for i in range(120):
    triangle()



exitonclick()