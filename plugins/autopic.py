# Modded by @buddhhu

import os, asyncio, shutil
from userbot import *
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from global_variables_sql import FONT_FILE_TO_USE, AUTOPIC_STR, COLOUR, AUTO_PIC_FONT, AUTOPIC_COMMENT, AUTOPIC_FONT_COLOUR

FONT_FILE_TO_USE = f"fonts/{AUTO_PIC_FONT}"
AUTOPIC_STR = str(AUTOPIC_COMMENT) if AUTOPIC_COMMENT else "Life Is too Short.\n And so is TG account."
COLOUR = str(AUTOPIC_FONT_COLOUR) if AUTOPIC_FONT_COLOUR else (255, 255, 255)

@plus_ub(pattern="autopic", from_users=sudo)
async def autopic(event):
	await event.reply("**Autopic has been enabled!!!**")
	a = await event.get_reply_message()
	downloaded_file_name = "userbot/original_pic.png"
	downloader = await plus.download_media(a, downloaded_file_name)
	photo = "userbot/photo_pfp.png"
	counter = -30
	while True:
		shutil.copy(downloaded_file_name, photo)
		im = Image.open(photo)
		file_test = im.rotate(counter, expand=False).save(photo, "PNG")
		current_time = datetime.now().strftime(f"Time: %H:%M \nDate: %d.%m.%y \n{AUTOPIC_STR}")
		img = Image.open(photo)
		drawn_text = ImageDraw.Draw(img)
		fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
		color = (COLOUR)
		drawn_text.text((95, 250), current_time, font=fnt, fill=color)
		img.save(photo)
		file = await event.client.upload_file(photo)
		try:
			await event.client(functions.photos.UploadProfilePhotoRequest(file))
			os.remove(photo)
			counter -= 30
			await asyncio.sleep(60)
		except:
			return
