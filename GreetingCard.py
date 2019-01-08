import PIL
import cloudinary

# import PyImage as PyImage

from PIL import Image,ImageOps, ImageEnhance
def new_Greeting(im):
    target_img = Image.new("RGB", (300, 600), "#29495d")
    out = im.convert("RGB", (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0 ))
    out.save("Image.jpg")
    o = Image.blend(im, out, 0.5)

    o = o.resize((300, 200))

    target_img.paste(o, (0, 400))
    return target_img

