import skimage as ski
from PIL import Image
import random

def recognize_box(img):
    shape_tuple = img.shape
    start_pixel = (random.randint(0, shape_tuple[0] - 1), random.randint(0, shape_tuple[1] - 1))
    print(img[start_pixel])




if __name__ == "__main__":
    path = "/Users/jzeld/Documents/hackathon/test_drawing.png"
    img = ski.io.imread(path)

    recognize_box(img)
    
