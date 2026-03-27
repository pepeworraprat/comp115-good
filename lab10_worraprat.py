"""
Lab 10 - Image Processing

Name: Worraprat Wuttisan
Due Date: Mar. 27, 2026, 5pm

Note: Run the file first, if you see an error of "No module of PIL",
install the package "pillow" by: pip install pillow
"""

import random
from PIL import Image

"""
Pixel is the smallest unit of a digital image. 
A digital image is a finite collection of pixels.

These pixels are organized in a two-dimensional grid. 
Each image (grid of pixels) has its own width and its own height. 
The width is the number of columns of pixels,
and the height is the number of rows of pixels.

In image processing, we access pixels in the grid by using column index and row index.
E.g, you can open the image_pixel_grid.png file in this folder (on the left).
The pixel of the pink one is found at column c and row r. 
And the pixel at the top left corner can be accessed as column 0 and row 0. 
Yes, we are always counting from 0 in computer science.

In color images, each pixel is represented by three values (r, g, b). 
The values indicate the intensity of red, green, and blue, respectively.

Before we start our lab, let's read some image processing examples below.
"""


def create_red_one_pixel():
    """
    This function creates an image with only one red pixel.
    We access that pixel by its col index 0, and row index 0.
    The rgb value of red color is (250, 0, 0)
    """
    one_pixel_image = Image.new('RGB', (1, 1))   # Create an image of dimension 1 x 1
    one_pixel_image.putpixel((0, 0), (255, 0, 0))  # Set that pixel to red color
    one_pixel_image.save("red_one_pixel.png")  # Save the image as a file named ed_one_pixel.png


# Uncomment the following line to call the function. Observe the generated imag.
# create_red_one_pixel()


def create_red_more_pixels(width, height):
    """
    This function creates an image of dimension width x height pixels.
    We access pixels by index row and index col.
    And we set each pixel to be red color.
    """
    im = Image.new('RGB', (width, height))
    for row in range(height):
        for col in range(width):
            im.putpixel((col, row), (255, 0, 0))
    im.save("red_more_pixels.png")

# Uncomment the following line to call the function. Observe the generated imag.
# create_red_more_pixels(300, 300)
"""
Note: if you click and view the image files red_one_pixel.png and red_more_pixels.png,
you might see them almost the same. However, if you download these two files onto 
your computer, and see its size and dimensions. 
You will find the difference:
The size of red_one_pixel.png is much less than the size of red_more_pixels.png. 
The dimension of red_one_pixel.png is 1 x 1 pixel, 
while the dimension of red_more_pixels.png is 300 x 300 pixels.

"""

palette_pixels = [(255, 0, 0), (254, 152, 191), (255, 127, 0), (255, 255, 0),
                  (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]
# red, pink, orange, yellow, green, blue, indigo, violet


def create_eight_pixels_image():
    """
    This function creates a colorful image with eight pixels.
    """
    eight_pixels_image = Image.new('RGB', (4, 2)) # Image dimension is 4 colums (width) x 2 rows (height)
    # eight_pixels_image.putdata(palette_pixels)
    i = 0  # Index of the list palette_pixels
    for row in range(2):
        for col in range(4):
            r = palette_pixels[i][0]
            g = palette_pixels[i][1]
            b = palette_pixels[i][2]
            eight_pixels_image.putpixel((col, row), (r, g, b))
            i += 1
    eight_pixels_image.save("palette_eight_pixels.png")

# Uncomment the following line to call the function. Observe the generated imag.
# create_eight_pixels_image()


def create_palette_more_pixels(width, height):
    """
    This function creates an colorful image with width x height pixels.
    """
    im = Image.new('RGB', (width, height))
    for row in range(height):
        for col in range(width):
            im.putpixel((col, row), (255, row % 256, col % 256))
    im.save("palette_more_pixels.png")

# Uncomment the following line to call the function. Observe the generated imag.
# create_palette_more_pixels(250, 250)
    
"""
Exercise 1 - Dim the image palette_more_pixels.png (20 marks)

Complete the following function to load the image file "palette_more_pixels.png", 
create its dim version,
and save as a new image file named "img1_palette_dim.png".
The rgb values of the pixels in "img1_palette_dim.png" should equal to
the half of the rgb values of the pixels in "palette_more_pixels.png".

Hint: 
Update r, g, b values with about the half of its original values. 
You may need just 3 lines of code to complete this function.

"""


def dim_eight_pixels_image():
    """
    This function dims an image to its half colorfulness
    """
    im = Image.open("palette_more_pixels.png")
    im_dim = Image.new("RGB", (im.width, im.height))
    for row in range(im.height):
        for col in range(im.width):
            (r, g, b) = im.getpixel((col, row))
            r = r // 2
            g = g // 2
            b = b // 2
            im_dim.putpixel((col, row), (r, g, b))
    im_dim.save("img1_palette_dim.png")


#dim_eight_pixels_image()


"""
Exercise 2 - Blue-washed Rick and Morty (20 marks)

In the interactive textbook Activity: 8.11.3.5 Multiple Choice, we created a red-washed bell image.
In this exercise, let's create an image of a blue-washed version of "rick_and_morty.png", 
and save the blue-washed version as "img2_rick_blue_washed.png".
"""


def blue_washed_image():
    """
    This function creates a blue-washed version of "rick_and_morty.png",
    and save the blue-washed version as "img2_rick_blue_washed.png"
    """
    im = Image.open("rick_and_morty.png")
    im_blue = Image.new("RGB", [im.width, im.height])
    
    for row in range(im.height):
        for col in range(im.width):
            (r, g, b) = im.getpixel((col, row))
            b = 255
            im_blue.putpixel((col, row), (r, g, b))

    im_blue.save("img2_rick_blue_washed.png")


#blue_washed_image()

# Uncomment the following 4 lines of code, and run it, 
# which generated rick_changing.gif file. 
# You can open the gif to see it. Do you like it?
# img1 = Image.open("rick_and_morty.png")
# img2 = Image.open("img2_rick_blue_washed.png")
# frames = [img1, img2]  # Save into a GIF file that loops forever
# frames[0].save('rick_changing.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)


"""
Exercise 3 - Create a white-black-line image (20 marks)

Create an image called img3_alternate_lines.png where we have horizontal lines 
that alternate between white and black.

Hint:
The rgb color of white color is (255, 255, 255).
The rgb color of black color is (0, 0, 0).
We may set the pixels to white if its row is even.
"""


def create_alternate_lines(width, height):
    """
    Create an image called img3_alternate_lines.png where we have horizontal lines 
    that alternate between white and black. The first line is white.
    """
    im = Image.new("RGB", (width, height))

    for row in range(height):
        for col in range(width):
            if row % 2 == 0:
                im.putpixel((col, row), (255, 255, 255))
            else:
                im.putpixel((col, row), (0, 0, 0))
    im.save("img3_alternate_lines.png")


#create_alternate_lines(100, 120)
    
"""
Exercise 4 - Create a randome noise image (20 marks)

Using the random.random() function, create an image called img4_random.png where
each pixel has a 50% chance of being white or black.

We have imported random module at the top of this file.

Hint: 
1. random.random() generates a random decimal number in the interval [0, 1).
2. random.random() has a 50% chance of generating a decimal number larger than 0.5 or less than 0.5.
"""


def create_random_noise(width, height):
    """
    Create an image called img4_random.png where each pixel has a 50% chance of being white or black.
    """
    im = Image.new("RGB", (width, height))
    
    for row in range(height):
        for col in range(width):
            (r, g, b) = im.getpixel((col, row))
            if random.random() < 0.5:
                im.putpixel((col, row), (255, 255, 255))
            else:
                im.putpixel((col, row), (0, 0, 0))

    im.save("img4_random.png")

#create_random_noise(150, 150)
    
"""
Exercise 5 - Decode an image (20 marks)

Steganography is the practice of concealing a file, message, image, or video
within another file, message, image, or video. 

The file rick_encoded.png looks normal, 
but we actually hid a secret image inside the red channel.  

Implement the following algorithm:
 - Create a secret image with the same width and height as rick_encoded.png
 - Use our nested loop to process each pixel:
     - If the red channel is odd, turn the resulting pixel on the new image to black,
     i.e., (0, 0, 0)
     - Otherwise, if the red channel is even, turn the resulting pixel on the new image
     to red, i.e., (255, 0, 0)
 - Save the new image to an image called img5_rick_secret.png

"""


def decode_image():
    im = Image.open("rick_encoded.png")
    im_secret = Image.new("RGB", [im.width, im.height])

    for row in range(im.height):
        for col in range(im.width):
            (r, g, b) = im.getpixel((col, row))
            if r % 2 == 1:
                im_secret.putpixel((col, row), (0, 0, 0))
            else:
                im_secret.putpixel((col, row), (255, 0, 0))

    im_secret.save("img5_rick_secret.png")


#decode_image()
    
# Congratulations! Hope you had fun with lab10.
# Upload it to your github account, and copy the link to e-learn. That's all.
