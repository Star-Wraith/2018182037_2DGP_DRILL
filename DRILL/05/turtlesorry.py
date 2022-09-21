import turtle

def turle_UP():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turle_DOWN():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()



def turle_LEFT():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()


    

def turle_RIGHT():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()



def restart():
    turtle.reset()
    turtle.stamp()


turtle.shape('turtle')
turtle.stamp()
turtle.onkey(turle_UP,'w')
turtle.onkey(turle_DOWN,'s')
turtle.onkey(turle_LEFT,'a')
turtle.onkey(turle_RIGHT,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
turtle.exitonclick()

