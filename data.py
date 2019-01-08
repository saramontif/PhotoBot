import gridfs
from pymongo import mongo_client
from PIL import Image

c = mongo_client.MongoClient()
db = c.botPhotos
fs = gridfs.GridFS(db)

def save_image(path, c_id, num):
  fs.put(path.encode('ascii'), chat=c_id, filename=f"{c_id}_{num}.jpg")

from io import BytesIO
import requests
def load_image(c_id):
   photos = []
   for grid_out in fs.find({"chat": c_id}):
       file = grid_out.read()
       a = requests.get(file.decode("utf-8", "ignore"))
       img = Image.open(BytesIO(a.content))
       photos.append(img)
   return photos