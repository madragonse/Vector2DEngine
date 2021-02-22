from physics import Physics
from vector2D import Vector2D
from matrixOp import Matrix_op
from shape2D import Shape2D
from testClass import TestClass
import collision2D
import turtle
import keyboard
from line2D import Line2D

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600



def render(pen:turtle.Turtle, line):
    pen.penup()
    pen.goto(line[0][0], line[0][1])
    pen.pendown()
    pen.width(2)
    pen.goto(line[1][0], line[1][1])
    pen.penup()

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

wn = turtle.Screen()
wn.setup(width = SCREEN_WIDTH + 20, height = SCREEN_HEIGHT + 20)
wn.title("Collision detection test")
wn.bgcolor("black")
wn.tracer(0)

collision_tool = collision2D.Collision()

l1 = Line2D([[-10,-15], [10*6,15*6]]) 
l2 = Line2D([[-40, -40], [40,40]])

s1 = Shape2D([1, 1])
s2 = Shape2D([0, 0])

s1.addLine(l1)
s2.addLine(l2)

vector_test = Vector2D([3,4])
phis_test = Physics([0, 0])
phis_test.set_speed(vector_test)
print(phis_test.get_speed())

while True:

    # Clear the screen  
    pen.clear()

    # if keyboard.is_pressed('w'):
    #     s1.move([0, 0.1])
    # if keyboard.is_pressed('s'):
    #     s1.move([0, -0.1])
    # if keyboard.is_pressed('a'):
    #     s1.move([-0.1,0])
    # if keyboard.is_pressed('d'):
    #     s1.move([0.1,0])
    # if keyboard.is_pressed('q'):
    #     s1.rotate(0.1)
    # if keyboard.is_pressed('e'):
    #     s1.rotate(-0.1)  
    # 
    # s1.set_speed([0,0])
    # if keyboard.is_pressed('w'):
    #     s1.add_speed(Vector2D([0, 30]))
    # if keyboard.is_pressed('s'):
    #     s1.add_speed(Vector2D([0, -30]))
    # if keyboard.is_pressed('a'):
    #     s1.add_speed(Vector2D([-30,0]))
    # if keyboard.is_pressed('d'):
    #     s1.add_speed(Vector2D([30,0]))
    
    # if keyboard.is_pressed('w'):
    #     s1.add_acceleration(Vector2D([0, 0.001]))
    # elif keyboard.is_pressed('s'):
    #     s1.add_acceleration(Vector2D([0, -0.001]))
    # else:
    #     s1.decelarate_by(Vector2D([0, 1]))

    # if keyboard.is_pressed('a'):
    #     s1.add_acceleration(Vector2D([-0.001,0]))
    # elif keyboard.is_pressed('d'):
    #     s1.add_acceleration(Vector2D([0.001,0]))
    # else:
    #     s1.decelarate_by(Vector2D([1, 0]))

    s1.set_acceleration([0,0])
    if keyboard.is_pressed('w'):
        s1.add_acceleration(Vector2D([0, 1]))
    if keyboard.is_pressed('s'):
        s1.add_acceleration(Vector2D([0, -1]))
    if keyboard.is_pressed('a'):
        s1.add_acceleration(Vector2D([-1,0]))
    if keyboard.is_pressed('d'):
        s1.add_acceleration(Vector2D([1,0]))

    if keyboard.is_pressed('q'):
        s1.rotate(0.1)
    if keyboard.is_pressed('e'):
        s1.rotate(-0.1) 
    
    s1.calculate(0.015)
    print(s1.get_acceleration())
    #print(s1.get_acceleration())
    res = collision_tool.shapesCollision(s1, s2)
    if  (res == False): 
        pen.color("White")
    else:
        pen.color("Blue")

    linesToDraw = s1.getLinesToDraw()
    for line in linesToDraw:
        render(pen, line) 
    linesToDraw = s2.getLinesToDraw()
    for line in linesToDraw:
        render(pen, line) 


    wn.update()




