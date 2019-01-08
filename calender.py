import calendar
from PIL import Image, ImageDraw, ImageFont

def print_on_image(path):
   allManth=[]
   num = 0
   for i in range(12):
      j=i%len(path)
      my_photo=path[j]
      #image = Image.open(path)
      new_image = Image.new('RGB', (500, 800), (0, 0, 0))
      draw = ImageDraw.Draw(new_image)
      font = ImageFont.truetype(r"Roboto-Black.ttf", 50)
      (x, y) = (0, 0)
      color = 'rgb(255, 255, 255)' # black color
      im = Image.open(my_photo)
      im = im.resize((500, 400))
      new_image.paste(im, (0, 0))
      c = calendar.TextCalendar()
      draw.text((0, 0+400), c.formatmonth(2018, i+1, 0, 0), fill=color, font=font)
      # new_image.save(f'greeting_card_{num}.png')
      num += 1
      allManth.append(new_image)

   print(allManth)
   return allManth


