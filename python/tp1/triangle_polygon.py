import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 
  
n = int(input("Enter the no of the sides of the polygon : ")) 
  
l = int(input("Enter the length of the sides of the polygon : ")) 
  
  
for x in range(n): 
    t.forward(l) 
    t.left(360 / n) 

turtle.done()