"""
Lab 9 - DNA

Name: Worraprat Wuttisan
Due Date: Mar. 20, 2026, 5pm

This lab contains 3 small exercises in total. The objectives are:
1. Review how to utilize the different data types in different scenarios, such as dict, strings.
2. Review the accumulator algorithm pattern.
3. Learn about one of the DNA visualization method in bioinformatics, and how to break down a problem into subproblems.


Bioinformatics is a field where biologists use the power of computers
to help analyze biological data, such as DNA.

DNA can be represented as a long string of 4 characters: 'A', 'T', 'G', and 'C'.

In this lab, we will create a graph of DNA using the Squiggle’s visualization method.
In essence, a DNA sequence is first converted into binary using the 2bit encoding scheme
that maps 'T' to '00', 'C' to '01', 'A' to '10', and 'G' to '11',
e.g., 'ATGC' becomes: '10001101'

If you want to know more about Squiggle method, please refer to the following article:
https://squiggle.readthedocs.io/en/latest/methods.html#squiggle

"""


import turtle

# The following DNA sequences are for testing, implemented as a python dictionary.
# i.e. DNA['Human'] will return a snippet of the human DNA string
DNA = {
    'Human':
    'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAG',
    'Rat':
    'ATGGTGCACCTGACTGATGCTGAGAAGGCTGCTGTTAATGGCCTGTGGGGAAAGGTGAACCCTGATGATGTTGGTGGCGAG',
    'Rhesus':
    'ATGGTGCATCTGACTCCTGAGGAGAAGAATGCCGTCACCACCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAG',
    'Chimpanzee':
    'ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAG'
}

# Squiggle's DNA mapping pairs from DNA bases to binary codes
DNA_TO_CODE_DICT = {
    'T': '00',
    'C': '01',
    'A': '10',
    'G': '11'
}

"""
Exercise 1 (30 marks: function implementation, 10 marks: time complexity analysis)

Given a DNA sequence, return a coded sequence of 1's and 0's.
You will use the DNA_TO_CODE_DICT to map between base and
the code, i.e.:

dna_to_code('A') returns '10'
dna_to_code('T') returns '00'
dna_to_code('G') returns '11'
dna_to_code('C') returns '01'
dna_to_code('AA') returns '1010'
dna_to_code('AATT') returns '10100000'
"""


def dna_to_code(dna):
    """
    This function returns a coded sequence of 1's and 0's, 
    based on the mapping method: T to 00, C to 01, A to 10, and G to 11.
    """
    coded = ''

    for i in dna:
        coded = coded + DNA_TO_CODE_DICT[i] # add each code one by one

    return coded 
    # Hint: use the accumulator pattern to process each character of
    # the input dna string.  Convert each character to its
    # coded counterpart using DNA_TO_CODE_DICT
    

# Unit tests
# assert dna_to_code('AATT') == '10100000'
# assert dna_to_code('AA') == '1010'


# Question: What is the time complexity of the function dna_to_code(dna),
# assuming the length of dna is n?

# Your Answer: O(n) because we go through each character in the dna string once



### The following draw functions are provided for you to use in Exercise 2

def draw_0(t):
    t.right(80)
    t.forward(20)
    t.left(80)


def draw_1(t):
    t.left(80)
    t.forward(20)
    t.right(80)


"""
Exercise 2 (30 marks)

Given a coded sequence and a color, graph the sequence using turtle
by looping over every character (either 0 or 1) and call 
the appropriate draw function provided above.

"""


def draw_coded(coded, color):
    # A turtle is already setup for you
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    t.goto(-300, -200)
    t.color(color)
    t.pendown()

    # process every character in the coded string and
    # call the corresponding draw function as provided above.
    for c in coded:
        if c == '0':
            draw_0(t)
        else:
            draw_1(t) # only 0 or 1 so else is fine


# You can uncomment the following 3 lines to test your function draw_coded(),
# and remember to comment these 3 lines after your testing for exercise 2.

# drawing_screen = turtle.Screen()
# draw_coded('10001101', 'red')
# drawing_screen.mainloop()




"""
Exercise 3 (30 marks)

With draw_coded written, we can create a DNA visualization
using the following sequence of commands:

code = dna_to_code('AGTTGC')
draw_coded(code, 'red')

To make it more convenient, complete the following
visualize() function by utilizing function dna_to_code() and draw_coded(),
such that we can pass in a DNA sequence
instead of a coded sequence, and our user will mainly 
interact with this visualize() function to visualize a DNA sequence.
"""


def visualize(dna, color):
    """
    This function performs the entire operation of visualizing a DNA sequence
    """
    # Hint: You need at most 2 lines of code to finish this function
    code = dna_to_code(dna)
    draw_coded(code, color)




# The main function below simply visualizes 4 sample DNA sequences
# in different colors. Uncomment the lines of main() below, run the program,
# and your output would look similar to the image of lab9_DNA_Visualization.png,
# which is here: https://github.com/awang-capu/comp115-capu/blob/main/lab9_DNA_Visualization.png

# if __name__ == "__main__":
#     drawing_screen = turtle.Screen()
#     visualize(DNA['Human'], 'red')
#     visualize(DNA['Rat'], 'green')
#     visualize(DNA['Rhesus'], 'blue')
#     visualize(DNA['Chimpanzee'], 'pink')
#     drawing_screen.mainloop() # Wait for the user to close the drawing screen
