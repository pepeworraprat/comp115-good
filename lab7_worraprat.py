"""
Lab 7 - Strings and Tuples 
(100 marks in total)

Author:  <Worraprat Wuttisan>
Due Date: This Friday (Mar. 6) 5 pm.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """
    result = ""

    for char in s:
        result = char + result

    return result


# Your unit tests
assert reverse_str("Abd") == "dbA"
assert reverse_str("COMP115") == "511PMOC"
assert reverse_str("app") == "ppa"


"""
Exercise 2 (10 marks: function implementation: 5 marks, unit tests: 5 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    s = s.lower()
    count = 0

    for char in s:
        if char in "aeiou":
            count += 1

    return count

# Your unit tests
assert count_vowels("Apple") == 2
assert count_vowels("Hmmm") == 0
assert count_vowels("Education") == 5


"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: in
"""
def remove_duplicates(s):
    """
    parameters:
    - s (string): The original string
    
    Returns:    
    - (string): A new string with duplicate characters removed    
    
    Examples:    
    >>> remove_duplicates("apple")    
    'aple'    >>> remove_duplicates("Popsipple")    
    'Popsile'
    """     

    result = ""    
    
    for char in s:        
        if char not in result:            
            result += char    
    return result
    
    
# Your unit tests
assert remove_duplicates("apple") == "aple"
assert remove_duplicates("Popsipple") == "Popsile"
assert remove_duplicates("pear") == "pear"


"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""  

def find_index(s, t):
    """
    parameters:    
    - s (string): The string to search in    
    - t (string): The character to find    
    
    Returns:    
    - (int): The lowest index where t appears in s.
             Returns -1 if the character is not found.    
    
    Examples:    
    >>> find_index("Abd", 'b')
    1
    >>> find_index("Abdccc", 'c')
    3
    >>> find_index("Abd", 'w')    
    -1    
    """

    for i in range(len(s)):
        if s[i] == t:
            return i

    return -1

# Your unit tests
assert find_index("Abd", 'b') == 1
assert find_index("Abdccc", 'c') == 3
assert find_index("Abd", 'w') == -1


"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    parameters:    
    - day (string): The starting day of the week    
    - days_to_completion (int): Number of days required    
    
    Returns:    
    - (string): The day of the week when the project completes    
    
    Examples:    
    >>> project_completion_day('Monday', 4)    
    'Friday'    
    >>> project_completion_day('Saturday', 2)    
    'Monday'   
    """
    
    start_index = days_week.index(day)

    completion_index = (start_index + days_to_completion) % 7

    return days_week[completion_index]


# Your unit tests
assert project_completion_day('Monday', 4) == 'Friday'
assert project_completion_day('Monday', 7) == 'Monday'
assert project_completion_day('Saturday', 2) == 'Monday'
assert project_completion_day('Saturday', 1) == 'Sunday'



"""Log Parsing Exercise (20 marks - function implementation 10, unit test 5, function usage 5)

You are given a log string containing application logs 
in a standardized format. Each log entry contains 
a timestamp, severity level, module name, and message.
Your task is to implement two functions to parse and filter
these logs.

Log format - Each log line follows this pattern:
YYYY-MM-DD HH:MM:SS [LEVEL] module.py Message

Sample log data:
log_string = "
2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
"

Implement a function parse_log_line(line) to parse a single log line into its components.

Your function returns:
A tuple of 4 elements: (timestamp, level, module, message)

timestamp (str): Date and time in format "YYYY-MM-DD HH:MM:SS"
level (str): Log severity level ("ERROR", "WARNING", or "INFO")
module (str): The Python module/file name (e.g., "database.py")
message (str): The log message text

E.g.,
line = '2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s'
parse_log_line(line) == ('2024-03-05 14:32:15', 'ERROR', 'database.py', 'Connection timeout after 30s')

Hints:
1. str.split() returns a list of strings, split by default (whitespace).
"hello world python".split()
# Returns: ['hello', 'world', 'python']

2. string concatenation
'I like ' + 'you'
# Returns 'I like you'

3. str.join()
list = ['Hello, ', 'world!']
' '.join(list)
# Returns 'Hello,  world!'
"""

def parse_log_line(line):
    """
    Parses a log line into timestamp, level, module, and message.

    Parameters:
    - line (string): A single log entry

    Returns:
    - tuple: (timestamp, level, module, message)
    """

    parts = line.split()

    timestamp = parts[0] + " " + parts[1]
    level = parts[2][1:-1]
    module = parts[3]

    message = " ".join(parts[4:])

    return (timestamp, level, module, message)


# Your unit tests
line = "2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s"

assert parse_log_line(line) == (
    "2024-03-05 14:32:15",
    "ERROR",
    "database.py",
    "Connection timeout after 30s"
)



# Use your parse_log_line() to parse all the lines in the sample data log_string,
# and store each tuple item in a list.
# Hint: log_string.split('\n') will return a list of lines.

log_string = """
2024-03-05 14:32:15 [ERROR] database.py Connection timeout after 30s
2024-03-05 14:32:18 [WARNING] api.py Slow query detected (2.3s)
2024-03-05 14:32:22 [INFO] server.py Server started on port 8000
2024-03-05 14:32:45 [ERROR] database.py Connection lost to primary
2024-03-05 14:33:02 [WARNING] cache.py Redis connection unstable
2024-03-05 14:33:15 [ERROR] api.py Request handler crashed
2024-03-05 14:33:22 [INFO] database.py Attempting reconnect
"""

parsed_logs = []

for line in log_string.split("\n"):
    if line != "":
        parsed_logs.append(parse_log_line(line))

print(parsed_logs)


"""
Congratulations on finishing your lab7. Hope you feel more confident 
on function implementation.

Now you just need to upload it to your GitHub repository, and paste the link on e-learn. That's all.
"""
