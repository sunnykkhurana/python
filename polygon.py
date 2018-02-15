# Author: Sunny Khurana
# "import" is calling library

# turtle graphics for drawing
import turtle   
# math library with random number
import random  

# user define input background color
screen = turtle.Screen()
screen_color = input("Enter Color for background ?")
screen.bgcolor(screen_color)
# user define input angle number
angle = int(input("Enter your side for polygon ? "))
# user define input size of number
size = int(input("Enter radius for polygon ?"))
# user define input distance betwwen draw
gap = int(input("Enter number to create distance between 2 polygon ?"))
# user define repetation of draw
repet = int(input("Enter number for repetation of drawing to create art ?"))
# user define line color of polygon
Polygon_color = input("Enter the color for draw line ?")
# user define input speed of drwaing
speedOfDrawing=int(input("Speed for drawing art?"))

#base buliding for polygon
def first_polygon():
    for i in range(angle):
        turtle.forward(size)    
        turtle.right(360.0/angle) #make angle using side        
        turtle.color(Polygon_color) #color of line to draw
 #repetation of polygon 
def repet_polygon():
  for i in range(repet):
    first_polygon() # use first function to for repet
    turtle.right(gap)
    
    
#changeing and modify property of turtle
def draw_art() :   
  turtle.hideturtle() #hide turtle icon
  turtle.speed(speedOfDrawing) #increase speed of draw
  repet_polygon()           # example of calling a function for multiple polygon
 
# execute the line art drawing function
draw_art()