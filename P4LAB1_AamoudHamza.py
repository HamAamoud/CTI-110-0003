#Hamza Aamoud
#3/26/24
#P4LAB1
#Drawing triangles and squares using loops

import turtle
win = turtle.Screen
turtle.screensize(600,600)
win = turtle.bgcolor("black")
t = turtle.Turtle()

t.pensize(4)
t.pencolor("red")
t.fillcolor("blue")
t.begin_fill()
t.shape("turtle")

for num1 in range(4):
    t.forward(50)
    t.left(90)

t.penup()
t.goto(100,100)
t.pendown()
num2 = 0

while num2 <3:
    num2 +=1
    t.forward(50)
    t.right(120)

t.end_fill()
