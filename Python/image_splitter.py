from PIL import Image


def split(img):
    sz = img.size
    pixel = img.load()
    img1 = Image.new("RGB", sz)
    img2 = Image.new("RGB", sz)
    img3 = Image.new("RGB", sz)
    pix1 = img1.load()
    pix2 = img2.load()
    pix3 = img3.load()
    for i in range(0, sz[0]):
        for j in range(0, sz[1]):
            col = pixel[i, j]
            pix1[i, j] = (col[0], 0, 0)
            pix2[i, j] = (0, col[1], 0)
            pix3[i, j] = (0, 0, col[2])
    return (img1, img2, img3)


im = Image.open(r"pic2.jpg")
new_img = split(im)
im.show()
new_img[0].show()
new_img[1].show()
new_img[2].show()
