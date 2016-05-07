import turtle
import random
wn = turtle.Screen()
name = "Ian"
wn.bgcolor("lightblue")
snappy = turtle.Turtle()
snappy.speed(20)
x = 0
bigDistance = 190

snappy.pendown() 
while x < 18: 
    snappy.forward(bigDistance)     
    snappy.right(60)
    snappy.forward(bigDistance)
    snappy.right(60)
    snappy.forward(bigDistance)
    snappy.right(60)
    snappy.forward(200)
    snappy.right(60)
    snappy.forward(200)
    snappy.right(60)
    snappy.forward(200)
    snappy.right(60)

    snappy.right(20) 
    x = x+1 # adds 1 to the value of x,
wn.exitonclick()
