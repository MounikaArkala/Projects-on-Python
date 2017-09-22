import turtle
window=turtle.Screen()
window.bgcolor("pink")

def draw_rangoli():
    brad=turtle.Turtle()
    brad.color("red")
    #brad.shape("turtle")
    brad.speed(1)
    x=400
    for j in range(0,3):
        brad.forward(x)
        brad.left(120)
    brad.forward(x/2)
    brad.left(120)
    for j in range(0,3):
        brad.forward(x/2)
        brad.right(120)
   # brad.right(120)
    brad.forward(x/4)
    brad.left(120)
    for j in range(0,3):
        brad.forward(x/4)
        brad.right(120)
    
       
    window.exitonclick()

draw_rangoli()     
        
