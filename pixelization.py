from CSE8AImage import *

def pixelization(image, square_size, column_percentage):
    # TODO
    else:


    elif row_index == 0 :
        for i in range(region_height//2):
            for j in range(region_width):
                temp = image[row_index+i][col_index+j]
                image[row_index+i][col_index+j] = image[height(image)-i-1-(height(image) - region_height)][col_index+j]
                image[height(image)-i-1-(height(image) - region_height)][col_index+j] = temp  
        return True 
    if 0 < row_index and row_index< height(image)//2:
        for i in range(region_height//2):
            for j in range(region_width):
                temp = image[row_index+i][col_index+j]
                image[row_index+i][col_index+j] = image[height(image)-i-1-(height(image)-row_index-2)][col_index+j]
                image[height(image)-i-1-(height(image)-row_index-2)][col_index+j] = temp  
        return True  
    elif row_index == height(image)//2:
        for i in range(region_height//2):
            for j in range(region_width):
                temp = image[row_index+i][col_index+j]
                image[row_index+i][col_index+j] = image[height(image)-i-2][col_index+j]
                image[height(image)-i-2][col_index+j] = temp
 
        return True
