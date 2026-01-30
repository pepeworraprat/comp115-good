"""
Lab 4 - Code Refactoring
(100 marks in total)

Name: Worraprat Wuttisan
Due Data: Jan. 30, 2023, 17:00pm

Objective:

Code refactoring in software development is to restructure code to 
a simpler, cleaner or more expressive architecture while keeping
its original functionality.

In this lab, the original code creates a beautiful symmetric drawing, 
sometimes called mandala. Run the file, and you will see the drawing.

After you read the original code, you will notice that
there is a lot of code repetition.
Your task is to rewrite the code so it still draws the same picture, 
but it uses only two functions. Each of the functions you write 
has to be very short (about 4 lines of code). In order to 
accomplish that, you need to add additional parameters to each function.

To start, figure out what the current function parameters do. 
Then figure out how the functions are different and how you can 
introduce new parameters to have only one function that 
replaces all the ones with the same name.

"""

import turtle

"""
Exercise 1:

Notice that all draw_circles functions are practically the same,
except for the resizing in each for loop iteration. 

Write a function called draw_circles to replaces all of the functions. 
draw_circles should have one additional parameters to accommodate
these varying values, and it should have about 4 lines of code.
"""


def draw_circles(t, size, decrease):
    for _ in range(4):
        t.circle(size)
        size -= decrease



"""
Exercise 2:

Similar to Exercise 1, replace all instances of draw_special function with one 
function that uses parameters. Your function must call the drawCircle function 
you developed in exercise 1.

The function draw_special you write is short as well (about 4 lines of code).
"""

def draw_special(t, size, repeat, decrease):
    for _ in range(repeat):
        draw_circles(t, size, decrease)
        t.right(360 / repeat)


"""
Exercise 3:

At this point, you would have created 2 new functions: draw_circles and draw_special.

Your job is now to rewrite the draw_picture() into draw_picture_nice() below
so that it uses the 2 new functions from Exercises 1 and 2.

The draw_picture_nice() will also meet the following constraints:

  - Use 1 turtle instead of multiple turtles

  - Use a loop to change the turtle color and the decreasing amounts. 

After you finish the draw_picture_nice(), in the main function below:
uncomment line "#draw_picture_nice()", commnet next line "draw_picture()",
and run your program to verify your implementation.


HINT: 
You may use 2 lists to avoid the if statement, which is recommended:
        ...
        colors = ['white', 'yellow', 'blue', 'orange', 'red']
        decrease_amounts = [4, 5, 10, 19, 20]
        for i in range(len(colors)):
            t.color(colors[i])
        ...

"""



def draw_picture():
    Albert = turtle.Turtle()
    Albert.speed(0)
    Albert.color('white')
    draw_special(Albert, 100, 10, 4)

    Steve = turtle.Turtle()
    Steve.speed(0)
    Steve.color('yellow')
    draw_special(Steve, 100, 10, 5)

    Barry = turtle.Turtle()
    Barry.speed(0)
    Barry.color('blue')
    draw_special(Barry, 100, 10, 10)

    Terry = turtle.Turtle()
    Terry.speed(0)
    Terry.color('orange')
    draw_special(Terry, 100, 10, 19)

    Will = turtle.Turtle()
    Will.speed(0)
    Will.color('red')
    draw_special(Will, 100, 10, 20)

def draw_picture_nice():
    t = turtle.Turtle()
    t.speed(0)

    colors = ['white', 'yellow', 'blue', 'orange', 'red']
    decrease_amounts = [4, 5, 10, 19, 20]
    
    for i in range(len(colors)):
        t.color(colors[i])
        draw_special(t, 100, 10, decrease_amounts[i])



if __name__ == "__main__":
    drawing_screen = turtle.Screen()
    drawing_screen.bgcolor('black')
    draw_picture_nice()
    
    drawing_screen.mainloop() # Wait for the user to close the drawing screen


"""
After finishing your lab, please upload the file to GitHub and copy paste the link
to your e-learn.

Hope this lab is helpful to your project 1 - Artistic Turtle Drawing. Have fun!
"""
