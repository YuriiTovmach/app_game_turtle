import  turtle

tom = turtle.Turtle()
tom.color('green')
tom.pensize(5)
tom.shape('turtle')

tom.forward(100)
tom.left(90)
tom.penup()
tom.forward(100)
tom.right(90)
tom.pendown()
tom.color('red')
tom.forward(100)

dan = turtle.Turtle()
dan.color('blue')
dan.pensize(20)

dan.backward(100)
dan.speed(1)