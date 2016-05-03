import turtle
joe = turtle.Turtle()
gary = turtle.Turtle()
lary = turtle.Turtle()
leeroy = turtle.Turtle()
james = turtle.Turtle()
jimbob = turtle.Turtle()
melisa = turtle.Turtle()
jimmy = turtle.Turtle()
erica = turtle.Turtle()

turtle.bgcolor('black')

leeroy.color('white')
leeroy.pensize(100)
leeroy.goto(400, 400)

jimbob.color('white')
jimbob.pensize(100)
jimbob.goto(0, 500)

jimmy.color('white')
jimmy.pensize(100)
jimmy.goto(0, -400)

erica.color('white')
erica.pensize(100)
erica.goto(500, 0)

melisa.color('white')
melisa.pensize(100)
melisa.goto(-500, 0)

james.color('white')
james.pensize(100)
james.goto(-400, -400)

lary.color('white')
lary.pensize(100)
lary.goto(-400, 400)

gary.color('white')
gary.pensize(100)
gary.goto(400, -400)

joe.goto(75,-115)
joe.color('purple','red')
joe.speed(0)
turtle.goto(125,-250)

turtle.color('red','yellow')
turtle.begin_fill()
joe.begin_fill()
turtle.speed(0)
while True:
    for num in range(1,32):
        turtle.backward(120)
        turtle.left(130)
        joe.backward(60)
        joe.left(130)
    # joe.penup()
    joe.circle(20,150)
    # joe.pendown()
    # turtle.penup()
    turtle.circle(20,150)
    # turtle.pendown()
    turtle.color('green', 'red')
    turtle.end_fill()
    joe.end_fill()

    for num in range(1,4):
        joe.color('yellow', 'red')
        joe.begin_fill()
        joe.forward(50)
        joe.left(170)
        joe.end_fill()
        turtle.color('pink','green')
        turtle.begin_fill()
        turtle.forward(100)
        turtle.left(170)
        turtle.end_fill()
        joe.end_fill()

        if num is 3:
            for num in range(3):
                joe.color('black', 'blue')
                joe.begin_fill()
                turtle.color('purple', 'red')
                turtle.begin_fill()
                turtle.forward(40)
                joe.forward(20)
                turtle.left(190)
                joe.left(190)
                turtle.backward(50)
                joe.backward(25)
                turtle.right(160)
                joe.right(160)
                turtle.forward(100)
                joe.forward(50)
