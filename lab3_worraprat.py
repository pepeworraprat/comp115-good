"""
Lab 3: Draw some basic shapes with Turtle Graphics, using loop algorithms.

Complete exercise 1-2 (each values 50 points, 100 points in total).

Author:  <Worraprat Wuttisan>
Due Date: This Friday (Jan. 23) 5:00pm.
    
"""

import turtle
drawing_screen = turtle.Screen()

"""
Understanding the following three examples is beneficial for you to move to the exercise 1 below.
"""

# Example 1 - Draw 10 steps with each step 20 pixels by 20 pixels.
num_steps = 10
alex = turtle.Turtle()
alex.speed(5)  # 1 sets the drawing speed as the slowest.
for _ in range(num_steps): # _ means this loop variable is unused, just repeat loop body num_steps times
    alex.forward(20) # 20 pixels
    alex.left(90) # Angle
    alex.forward(20)
    alex.right(90)
alex.shape("blank")  # After drawing, make the alex/pen/brush invisible.


# Example 2 - Draw an equilateral triangle with side length 100 pixels
# Uncomment the line 33 to 41

alex.clear()  # Clear the previous drawing on the screen.
alex.speed(1)
alex.shape("turtle")
side_length = 100
exterior_angle = 360 / 3  # Calculate the exterior angle of an equilateral triangle.
for _ in range(3):
    alex.forward(side_length)
    alex.left(exterior_angle)
alex.shape("blank")


# Example 3 - Draw a sqaure with side length 200 pixels
# Uncomment the line 47 to 57

alex.clear()  # Clear the previous drawing on the screen.
alex.shape("arrow")
alex.up() # alex.up() lifts alex/pen/brush up;
alex.goto(0, 0) # Go to the center of the drawing screen
alex.down() # alex.down() puts alex/pen/brush down, ready for drawing.
side_length = 100
exterior_angle = 360 / 4  # Calculate the exterior angle of an equilateral triangle.
for _ in range(4):
    alex.forward(side_length)
    alex.left(exterior_angle)
alex.shape("blank")


'''
Exercise 1 - To draw a regular hexagon:

You may have noticed that to draw a square is very similar 
to draw an equilateral triangle. We need to calculate 
the exterior angle of a square, which is the angle your turtle/pen/brush
will turn.

Now, similar as example 2 and 3, 
but draw a regular hexagon (6 sides) with side length 100.

Hint:
num_sides = 6
exterior_angle = 360 / num_sides
'''

# Code your exe 1 here
alex.clear()  # Clear the previous drawing on the screen.
alex.speed(1)
alex.shape("turtle")

side_length = 100
num_sides = 6
exterior_angle = 360 / num_sides

for _ in range(num_sides):
    alex.forward(side_length)
    alex.left(exterior_angle)
alex.shape("blank")







"""
Part 2

Understanding the following examples 4 and 5 is beneficial for you to move to the exercise 2 below.
"""

'''
Example 4 - Review lab2 last exercise
Uncomment the code below in this example, run the file and see the output 
This example clearly demonstrates accessing list elements by index.
'''
day_today = 3
days_trip = 5
day_back = (day_today + days_trip)%7

days_week = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

print(f'''
Your trip starts on day {day_today} ({days_week[day_today]}),
lasts days {days_trip}. 
You are back on day {day_back} ({days_week[day_back]}).
''')

'''
Example 5 - Draw a number of concentric circles
Uncomment the code below in this example, run the file and see the output 
This example clearly demonstrates accessing list elements by loop variables.
'''

num_circles = 7
rainbow_colors = ["violet", "indigo", "blue",
                   "green", "yellow", "orange", "red"]
radius = 30
radius_increase = 10
alex.clear()  # Clear the previous drawing on the screen.
alex.speed(5)
alex.pensize(5)
alex.up()
for rainbow_color in rainbow_colors:
    alex.color(rainbow_color)
    alex.goto(0, -radius)
    alex.down()
    alex.circle(radius)
    radius = radius + radius_increase
    alex.up()
alex.shape("blank")



'''
Exercise 2 - To draw a rainbow (like this one https://elearn.capu.ca/mod/assign/view.php?id=3237843):
You can set your own initial radius and increment value.

Hint: You may need to use the functions below:
alex.circle(-radius, 180)
alex.backward()
'''

# Code your exe 2 here
num_circles = 7
rainbow_colors = ["violet", "indigo", "blue",
                   "green", "yellow", "orange", "red"]

alex.clear()  # Clear the previous drawing on the screen.
alex.speed(5)
alex.pensize(10)

radius = 30
radius_increase = 10

alex.up()
alex.goto(radius, 0)
alex.setheading(90)
for rainbow_color in rainbow_colors:
    alex.color(rainbow_color)
    alex.goto(radius, 0) # right end of the arc
    alex.setheading(90) # face up
    alex.down()

    alex.circle(radius, 180) # top half circle
    alex.up()

    radius = radius + radius_increase
    
alex.shape("blank")



drawing_screen.mainloop() # Wait for the user to close the drawing screen


"""
Well done! Now you've finished your lab3 successfully. Please upload it 
to your GitHub repository and submit your lab3 GitHub link on e-learn, 
as you did for lab1 and lab2. That's all.

Resource (optional): For exercise 1, feel free to review the concept of exterior angles of regular polygons from here:
https://www.teachoo.com/8592/2789/Exterior-Angles-of-Regular-Polygons/category/Sum-of-Exterior-Angles-of-Polygons/
