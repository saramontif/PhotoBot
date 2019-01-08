
import PIL

from PIL import Image,ImageOps

def frame_to_image(listofimages, border, fill):
    listofimages_border=[]
    for i in listofimages:
      img = Image.open(i)
      img_with_border = ImageOps.expand(img,border= border,fill=fill)
      img_with_border.save('bordered-%s' % i)
      listofimages_border.append('bordered-%s' % i)
    return listofimages_border

def create_collage_9(listofimages, out):
    target_img = Image.new("RGB", (600, 600))
    imgs = []
    for i in listofimages:
        im = PIL.Image.open(i)
        imgs.append(im)
    for i in range(9):
        imgs[i] = imgs[i].resize((200, 200))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (0, 200))
    target_img.paste(imgs[2], (200, 0))
    target_img.paste(imgs[3], (200, 200))
    target_img.paste(imgs[4], (400, 0))
    target_img.paste(imgs[5], (0, 400))
    target_img.paste(imgs[6], (200, 400))
    target_img.paste(imgs[7], (400, 200))
    target_img.paste(imgs[8], (400, 400))

    target_img.save(out)

def create_collage_5(listofimages, out):
    target_img = Image.new("RGB", (600, 600))
    imgs = []
    for i in listofimages:
        im = PIL.Image.open(i)
        imgs.append(im)

    imgs[0] = imgs[0].resize((300, 300))
    target_img.paste(imgs[0], (0, 0))
    imgs[1] = imgs[1].resize((300, 300))
    target_img.paste(imgs[1], (0, 300))
    imgs[2] = imgs[2].resize((300, 200))
    target_img.paste(imgs[2], (300, 0))
    imgs[3] = imgs[3].resize((300, 200))
    target_img.paste(imgs[3], (300, 200))
    imgs[4] = imgs[4].resize((300, 200))
    target_img.paste(imgs[4], (300, 400))


    target_img.save(out)

def create_collage_4(listofimages, out):
    target_img = Image.new("RGB", (600, 600))
    imgs = []
    for i in listofimages:
        im = PIL.Image.open(i)
        imgs.append(im)
    for i in range(4):
        imgs[i] = imgs[i].resize((300, 300))

    target_img.paste(imgs[0], (0, 0))
    target_img.paste(imgs[1], (0, 300))
    target_img.paste(imgs[2], (300, 0))
    target_img.paste(imgs[3], (300, 300))

    target_img.save(out)


def create_collage_6(listofimages, out):
    target_img = Image.new("RGB", (600,600))
    imgs=[]
    for i in listofimages:
        im=PIL.Image.open(i)
        imgs.append(im)
    for i in range(5):
        imgs[i+1]=imgs[i+1].resize((200, 200))


    imgs[0]=imgs[0].resize((400,400))
    target_img.paste(imgs[0], (0,0))
    target_img.paste(imgs[1], (0,400))
    target_img.paste(imgs[2], (400,0))
    target_img.paste(imgs[3], (400,200))
    target_img.paste(imgs[4], (400,400))
    target_img.paste(imgs[5], (200,400))
    target_img.save(out)

def create_collage_8(listofimages, out):
    target_img = Image.new("RGB", (600, 600))
    imgs = []
    for i in listofimages:
        im = PIL.Image.open(i)
        imgs.append(im)

    imgs[0] = imgs[0].resize((200, 100))
    target_img.paste(imgs[0], (0, 0))
    imgs[1] = imgs[1].resize((200, 250))
    target_img.paste(imgs[1], (0, 100))
    imgs[2] = imgs[2].resize((300, 250))
    target_img.paste(imgs[2], (0, 350))
    imgs[3] = imgs[3].resize((300, 200))
    target_img.paste(imgs[3], (200, 0))
    imgs[4] = imgs[4].resize((100, 150))
    target_img.paste(imgs[4], (200, 200))
    imgs[5] = imgs[5].resize((100, 200))
    target_img.paste(imgs[5], (500, 0))
    imgs[5] = imgs[5].resize((300, 200))
    target_img.paste(imgs[5], (300, 200))
    imgs[5] = imgs[5].resize((300, 200))
    target_img.paste(imgs[5], (300, 400))
    target_img.save(out)

