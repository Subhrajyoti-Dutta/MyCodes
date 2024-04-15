import PIL
from PIL import Image
import numpy as np

src = Image.open("C:/Users/Laptop/Desktop/img.png")
pixels = src.load()

width, height = 1920, 1080

width_2, height_2 = width * 2 - 1, height * 2 - 1

out = Image.new("RGB",(width_2, height_2))
out_pix = out.load()

for w in range(0,width):
    for h in range(0,height):
        out_pix[2*w,2*h] = pixels[w,h]
        
# for the x pixels

for w in range(0,width-1):
    for h in range(0,height-1):
        p1 = out_pix[2*w,2*h]
        p2 = out_pix[2*w+2,2*h]
        p3 = out_pix[2*w,2*h+2]
        p4 = out_pix[2*w+2,2*h+2]
        out_pix[2*w+1,2*h+1] = tuple(np.sum(np.array([p1,p2,p3,p4]),axis=0)//4)


# for the even hor pix
for w in range(0,width-1):
    for h in range(0,height):
        p1 = out_pix[2*w,2*h]
        p2 = out_pix[2*w+2,2*h]
        out_pix[2*w+1,2*h] = tuple(np.sum(np.array([p1,p2]),axis=0)//2)

for w in range(0,width):
    for h in range(0,height-1):
        p1 = out_pix[2*w,2*h]
        p2 = out_pix[2*w,2*h+2]
        out_pix[2*w,2*h+1] = tuple(np.sum(np.array([p1,p2]),axis=0)//2)

        
out.save("C:/Users/Laptop/Desktop/img2.bmp")