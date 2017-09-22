import turtle
window=turtle.Screen()
window.bgcolor("pink")
def draw_rangoli():
    brad=turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(1)
    x=100
    a=1
    for j in range(0,3):
        brad.forward(x/a)
        brad.left(120)
    a=a*2
    for i in range(0,3):
        brad.forward(x/a)
        brad.left(120)
        for j in range(0,3):
            brad.forward(x/a)
            brad.right(120)
        a=a*2
       
    window.exitonclick()

draw_rangoli()     
        
