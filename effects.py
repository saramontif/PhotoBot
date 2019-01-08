from PIL import Image



def SeaCollor(im):
    out = im.convert("RGB", (
        0.412453, 0.357580, 0.180423, 0,
        0.212671, 0.715160, 0.072169, 0,
        0.019334, 0.119193, 0.950227, 0))
    return out


def Shine(im):
    img = SeaCollor(im)
    out2 = img.convert("RGB", (
        0.9756324, 0.154789, 0.180423, 0,
        0.212671, 0.715160, 0.254783, 0,
        0.123456, 0.119193, 0.950227, 0))
    return out2

def BlackWhite(im):
    out3 = im.convert("1")
    out3.save("Image4.jpg")
    return out3

def Sunny(im):
    out4 = im.convert("RGB", (
        0.986542, 0.154789, 0.756231, 0,
        0.212671, 0.715160, 0.254783, 0,
        0.123456, 0.119193, 0.112348, 0))
    return out4

def Old(im):
    out4=Sunny(im)
    out5 = Image.blend(im, out4, 0.5)
    return out5











