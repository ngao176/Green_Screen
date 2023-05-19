from CSE8AImage import *
import math

def change_background(image, new_background, replace_color):
    region_height=height(image)
    region_width = width(image)

    for i in range(region_height):
        for j in range(region_width):
            pixel = image[i][j]

            if pixel[1] >= replace_color[1] and pixel[0] < replace_color[0]:
                image[i][j] = new_background[i][j]
    save_img(image, "creative.png")
    return None
    #TODO

def color_distance(color1, color2):

    return None
    #TODO
# load the source image and new background image
img = load_img('Greenscreen.png')
forest = load_img('autumn-japan-kyoto-lake.jpeg')
green= (60,100,0)
# change the background
change_background(img, forest, green)
# save the image to a new file

