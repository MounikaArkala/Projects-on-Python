import turtle
window=turtle.Screen()
window.bgcolor("pink")
def draw_rangoli():
    brad=turtle.Turtle()
    brad.color("red")
    brad.shape("turtle")
    brad.speed(2)
    for i in range(0,35):      
        for j in range(0,4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    window.exitonclick()

draw_rangoli()     
        
   
    
