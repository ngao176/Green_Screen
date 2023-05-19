from CSE8AImage import *

def check_validity(image, col_index, row_index, region_height, region_width):
    if col_index < 0  or row_index < 0 or region_height < 0 or region_width < 0:
        return False
    if col_index + region_width > width(image) or row_index + region_height > height(image):
        return False
    if col_index >=width(image) or row_index  >= height(image):
        return False
    return True


def flip_vertical(image, col_index, row_index, region_height, region_width):
    # Check validity of input parameters
    if not check_validity(image, col_index, row_index, region_height, region_width):
        return False


    else:
        for i in range(region_height//2):
            for j in range(region_width):
                temp = image[row_index+i][col_index+j]
                image[row_index+i][col_index+j] = image[region_height+row_index-i-1][col_index+j]
                image[region_height+row_index-i-1][col_index+j] = temp
 
        return True


    # Return True if successfully flipped the image 

