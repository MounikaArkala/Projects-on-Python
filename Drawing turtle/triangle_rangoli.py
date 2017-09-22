import turtle
window=turtle.Screen()
window.bgcolor("pink")
def draw_rangoli():
    brad=turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(15)
    for i in range(0,35):      
        for i in range(0,3):
            brad.forward(100)
            brad.left(120)
        brad.right(170)
    window.exitonclick()

draw_rangoli()     
        
