"""
Lab 2 - Fundamentals of Python: values, data types, variables, 
expressions, statements, operators, built-in functions

(100 marks in total, including
6 exercises (90 marks) + submission (10 marks))

Your Name 😍: Worraprat Wuttisan
Lab Due: 5:00pm on Jan. 16 (Friday)

Objective:
1. Practice how to use variables, expressions and statements in Python
2. Practice working with different data types: int, float, str, list
3. Practice how to use operators and built-in functions in Python
4. Practice how to debug errors in a program
"""

# ---------------------------------------------------------
# Exercise 1 (10 marks)
# Run this file. You should see the output:
#   "Exercise 1: new_num stores the value of 45."
#
# Add parentheses to the following expression on line 29:
#     num * 10 - 5
# so that the value of new_num changes from 45 to 25.
# ---------------------------------------------------------

num = 5
new_num = num * (10 - 5)   # Add parentheses to make new_num equal to 25
print(f"Exercise 1: new_num stores the value of {new_num}.")


# ---------------------------------------------------------
# Exercise 2 (10 marks)
# Uncomment the code from line 40 to line 52.
# Modify the operators in line 45 and 46 so that
# quotient and remainder store the correct results as hinted.
# ---------------------------------------------------------

dividend = 10
divisor = 3

division_result = dividend / divisor

quotient = dividend // divisor     # The quotient should be 3
remainder = dividend % divisor    # The remainder should be 1

print(f"""
Exercise 2:
{dividend} ÷ {divisor} = {division_result}   (decimal result)
{dividend} ÷ {divisor} = {quotient} remainder {remainder}
""")


# ---------------------------------------------------------
# Exercise 3 (20 marks)
# Uncomment the code from line 63 to line 65.
# Modify the following expression in line 64:
#     (marks[0] + marks[1]) / 2
# so that it calculates the correct average of all marks.
# ---------------------------------------------------------

marks = [80.5, 85.3, 76.5, 79.7]  # A list of a student's first-term course marks
mark_average = sum(marks) / len(marks)  # Correct to get the average of all marks 80.5
print(f"Exercise 3: The average mark is {mark_average}!")


# ---------------------------------------------------------
# Exercise 4 (20 marks) - Expressions and Operators
# Write a program after line 77 that:
# 1. Stores the initial circle's radius value 2 in a variable named 'radius'
# 2. Calculates the circle's area using the formula: area = 3.14 * radius * radius
# 3. Print the result nicely using an f-string, e.g.,
#    'The area of a circle with radius 2 is 12.56.'

print("\nExercise 4")  

radius = 2
area = 3.14 * radius * radius
print(f"The area of a circle with radius {radius} is {area}.")

# ---------------------------------------------------------
# Exercise 5 (30 marks)
#
# Problem:
# Suppose the days of the week are numbered as follows:
# Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3,
# Friday = 4, Saturday = 5, Sunday = 6
# You are going on a trip that lasts n days.
#
# Task:
# Write a Python program that:
# 1. Asks the user to input today's day number and stores it in a variable named day_today.
# 2. Asks the user to input the trip duration and stores it in a variable named days_trip.
# 3. Calculates the day number of the week it will be after the trip using the modulus operator (%).
# 4. Prints the resulting day number nicely using an f-string.
#
# Example:
# 1) If the user inputs today as 0 (Monday) and trip duration as 2,
#    the trip starts on day 0 (Monday) and lasts 2 days.
#    The user will return on Wednesday (day number 2).
#    Output: 'Your trip starts on day 0, lasts 2 days. You are back on day 2.'
#
# 2) If the user inputs today as 3 (Thursday) and trip duration as 5,
#    the trip starts on day 3 (Thursday) and lasts 5 days.
#    The user will return on Tuesday (day number 1).
#    Output: 'Your trip starts on day 3, lasts 5 days. You are back on day 1.'

print("\nExercise 5")

day_today = int(input("Enter today's day number (0-6): "))
days_trip = int(input("Enter trip duration: "))

day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_return = (day_today + days_trip) % 7

startday_name = day_names[day_today]
returnday_name = day_names[day_return]

print(
    f"Your trip starts on day {day_today} ({startday_name}), lasts {days_trip} days."
    f"You are back on day {day_return} ({returnday_name})."
)


#---------------------------------------------------------
# Submission (10 marks):
# After you finish this lab, please:
# 1. rename the lab file as lab2_{your_first_name}.py.
# 2. upload your lab2 python file to your GitHub "comp115" repository.
# 3. submit your github comp115 repo link on the e-learn.
# Great job. Congratulations on finishing your lab2!
#---------------------------------------------------------
