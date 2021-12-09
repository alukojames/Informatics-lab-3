# Isu number = 336205
# eyes = O nose = 1 mouth = 2
#:<O

import turtle as turtle
import re

def check_for_emoticons(filename):
    file = open(filename)
    readfile = file.read()
    pattern = re.compile(r'[:][<][O]')
    occurrence = re.findall(pattern, readfile)
    print(len(occurrence))

for i in range(1,6):
    name_of_checked_file = 'text' + str(i) + '.txt'
    (check_for_emoticons(name_of_checked_file))
#######################################################################################################

turtle.title("Smiley")
turtle.pensize(10)
turtle.pencolor("black")
turtle.penup()
turtle.goto(20, -280)
turtle.pendown()
turtle.speed(1)
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(260)
turtle.end_fill()

#eyes
turtle.color("black")
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.dot(20)
turtle.penup()
turtle.goto(-100, -80)
turtle.pendown()
turtle.dot(20)

#nose
turtle.penup()
turtle.goto(-50, -20)
turtle.pendown()
turtle.right(10)
turtle.forward(100)
turtle.penup()
turtle.goto(-50, -20)
turtle.pendown()
turtle.left(30)
turtle.forward(100)


#mouth
turtle.penup()
turtle.pencolor("black")
turtle.goto(170,-70)
turtle.pendown()
turtle.circle(60)
turtle.end_fill()
turtle.hideturtle()

turtle.exitonclick()








