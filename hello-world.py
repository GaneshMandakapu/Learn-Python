import turtle 
import sys

print("Hello World")

myturtle = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor("light green")

myturtle.pencolor("blue")
myturtle.pensize(2)
myturtle.penup()
myturtle.goto(-50,50)
myturtle.pendown()

for i in range(4):
	myturtle.forward(100)
	myturtle.right(90)

i = input("please enter to exit")
