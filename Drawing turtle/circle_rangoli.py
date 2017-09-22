import turtle
window=turtle.Screen()
window.bgcolor("pink")
def draw_rangoli():
    brad=turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(2)
    for i in range(0,35):      
        for i in range(0,3):
            brad.circle(100)
        brad.right(10)
    window.exitonclick()

draw_rangoli()   
