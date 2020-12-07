import requests , re , random 

import urllib , os 

from telethon.tl import functions

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

import asyncio

from time import sleep


# Space lovers 
COLLECTION_STRINGS = [

  "1920x1080-space-wallpapers",

  "4k-space-wallpaper",

  "cool-space-wallpapers-hd",
]

async def animepp():

    os.system("rm -rf plus.jpg")

    rnd = random.randint(0, len(COLLECTION_STRINGS) - 1)

    pack = COLLECTION_STRINGS[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile('/\w+/full.+.jpg')

    f = f.findall(pc)

    fy = "http://getwallpapers.com"+random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")

    urllib.request.urlretrieve(fy,"plus.jpg")

@plus_ub(pattern="spacedp ?(.*)", from_users=sudo)

async def main(event):

    await event.reply("**Starting Space Profile Pic...**\n\nDone !!! Check Your DP") #Owner MarioDevs

    while True:

        await animepp()

        file = await event.client.upload_file("plus.jpg")  

        await event.client(functions.photos.UploadProfilePhotoRequest( file))

        os.system("rm -rf plus.jpg")

        await asyncio.sleep(60) #Edit this to your required needs

