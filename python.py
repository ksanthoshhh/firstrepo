import turtle 
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(11)
while(True):
    for i in range(6):
        for colors in ["red" , "yellow", "green","blue","magenta"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)