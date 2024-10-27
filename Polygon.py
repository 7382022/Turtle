import turtle   #importing libary
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #defined Variable


num_sides=4 #Variable
side_length = 70
angle = 360.0 / num_sides#iterate loop fir total number of sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()