import skimage as ski
from PIL import Image
import random
import numpy as np

def extract_shapes(img):
    shape_tuple = img.shape
    start_pixel = (random.randint(1, shape_tuple[0] - 2), random.randint(1, shape_tuple[1] - 2))
    print(img[0,0])
    new_shape = find_shape(img, start_pixel)
    #for pixel in new_shape[0]:
    #    img[pixel] = [0, 255, 0, 255]
    #for pixel in new_shape[1]:
    #    img[pixel] = [200, 50, 100, 255]
    ski.io.imsave("my_saved_image.png", new_shape[1])

    

def find_shape(img, start_pixel):   #start_pixel is a coordinate tuple
    """Starting at a pixel, expand outwards until a pixel of a different color is detected
    for all sides."""
    seeking_color = img[start_pixel]
    dims = img.shape
    inner_coordinate_list = [] 
    outer_coordinate_list = [start_pixel]
    expansion_candidates = []
    k = 0
    while True:
        k += 1
        
        for pixel in outer_coordinate_list:
            if pixel[0] != 0:                       
                new_pix = (pixel[0] - 1, pixel[1])
                if new_pix not in (inner_coordinate_list + outer_coordinate_list):
                    expansion_candidates.append(new_pix)
            if pixel[0] != dims[0] - 1:
                new_pix = (pixel[0] + 1, pixel[1])
                if new_pix not in (inner_coordinate_list+outer_coordinate_list):
                    expansion_candidates.append(new_pix)
        

        top_pixels = []
        bottom_pixels = []
        outer_coordinate_list = sorted(outer_coordinate_list, key=lambda p: p[1])
        for pixel in outer_coordinate_list:
            if pixel[1] == outer_coordinate_list[0][1]:
                top_pixels.append(pixel)
            if pixel[1] == outer_coordinate_list[-1][1]:
                bottom_pixels.append(pixel)
  

        for bottom_pixel in bottom_pixels:
            if bottom_pixel[1] != dims[1] - 1:
                new_pix = (bottom_pixel[0], bottom_pixel[1] + 1)
                if new_pix not in (inner_coordinate_list + outer_coordinate_list):
                    expansion_candidates.append(new_pix)
        for top_pixel in top_pixels:
            if top_pixel[1] != 0:
                new_pix = (top_pixel[0], top_pixel[1] - 1)
                if new_pix not in (inner_coordinate_list + outer_coordinate_list):
                    expansion_candidates.append(new_pix)

        invalid_pixels = []
        for expansion_pixel in expansion_candidates:
            
            if not (img[expansion_pixel][0] == seeking_color[0] and
                img[expansion_pixel][1] == seeking_color[1] and
                img[expansion_pixel][2] == seeking_color[2]):
                invalid_pixels.append(expansion_pixel)
        for invalid_pixel in invalid_pixels:
            expansion_candidates.remove(invalid_pixel)
   

        if len(expansion_candidates) == 0:
            print(k)
            break
        #if k == 200:
        #    break
        

        inner_coordinate_list += outer_coordinate_list
        outer_coordinate_list = expansion_candidates[:]
        expansion_candidates = []
        print(len(inner_coordinate_list))

        



        
    inner_coordinate_list += outer_coordinate_list
    return [inner_coordinate_list, outer_coordinate_list]
        








def get_size_arrays(arrays):
    count = 0
    for array in arrays:    
        count += array.size
    return count




if __name__ == "__main__":
    path = "/Users/jzeld/Documents/hackathon/test_drawing_4.png"
    img = ski.io.imread(path)

    extract_shapes(img)
    
