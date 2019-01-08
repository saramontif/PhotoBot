import random

from PIL import Image,ImageOps, ImageDraw,ImageFont
import colage
from io import BytesIO

def print_on_image_collage(im, text):

   # image = Image.open(path)
   draw = ImageDraw.Draw(im)
   font = ImageFont.truetype("arial.ttf", 50)
   color = 'rgb(255, 255, 255)' # white color
   draw.text((0, 550), text, fill=color, font=font)
   return im

def print_on_image_geeting(im, text):
    draw = ImageDraw.Draw(im)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", 40)
    # draw.text((x, y),"Sample Text",(r,g,b))
    color = 'rgb(255, 255, 255)'  # white color
    draw.text((0, 0),text, fill=color, font=font)
    im.save('sample-out.jpg')
    return im

def cut_image(lst):
    photos=[]
    print(lst)
    for i in range(len(lst)):
       # im = Image.open(lst[i])
       x=max(lst[i].size)
       y=min(lst[i].size)
       z=x-y
       if lst[i].size[0]>lst[i].size[1]:
           region = lst[i].crop((z/2,0, y+(z/2) , y ))
           photos.append(region)

       else:

           region = lst[i].crop((0 ,z/2, y,y+(z/2)))
           photos.append(region)

    return photos

def create_collage(images):
    for i in range(len(images)):
        images[i] = ImageOps.expand(images[i],border = 5,fill='black')
        images[i] = images[i].resize((600, 600))
    while(True):
        if len(images) == 0:
            return None
        if len(images) == 1:
            bio = BytesIO()
            bio.name = 'image.jpeg'
            images[0].save(bio, 'JPEG')
            return images[0]
        if len(images) == 2:
            return colage.create_collage_2(images)
        if len(images) == 3:
            return colage.create_collage_3(images)

        rand = 1
        if len(images) == 5:
            rand = random.randint(1, 2)
        if len(images) == 6 or len(images) == 7:
            rand = random.randint(1, 3)
        if len(images) == 8:
            rand = random.randint(1, 4)
        if len(images) >= 9:
            rand = random.randint(1, 5)

        if rand == 1:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_4(img))
        if rand == 2:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_5(img))
        if rand == 3:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_6(img))
        if rand == 4:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_8(img))
        if rand == 5:
            img = []
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            img.append(images.pop(0))
            images.append(colage.create_collage_9(img))

