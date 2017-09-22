import turtle
window=turtle.Screen()
window.bgcolor("pink")
def draw_square():
    
    brad=turtle.Turtle()
    brad.color("green")
    brad.shape("arrow")
    brad.speed(5)
    for i in range(0,4):
        brad.forward(100)
        brad.right(90)
def draw_circle():
    angie=turtle.Turtle()
    angie.color("yellow")
    angie.circle(100)
    angie.speed(5)
def draw_triangle():
    tri=turtle.Turtle()
    tri.color("blue")
    tri.shape("arrow")
    tri.speed(5)
    for i in range(0,3):
        tri.forward(100)
        tri.left(120)
    
    
    
    
       
          
  
    window.exitonclick()
draw_square()
draw_circle()
draw_triangle()
        
        
   
    
