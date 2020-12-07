# Code from pro sar Spechide's fork of Uniborg.
"""Rename Telegram Files
Syntax:
.rnupload file.name"""

import asyncio, os, time
from datetime import datetime


thumb_image_path = Var.TEMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@plus_ub(pattern="rnupload (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    a = await event.client.send_message(event.chat_id, "**Downloading your file...**\n**And will upload in few seconds...**", reply_to=event.reply_to_msg_id)
    await event.delete()
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        end = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        to_download_directory = Var.TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await event.client.download_media(
            reply_message,
            downloaded_file_name,
            )
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            c_time = time.time()
            await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
                )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await a.edit("Downloaded in {} seconds. Uploaded in {} seconds.".format(ms_one, ms_two))
        else:
            await a.edit("File Not Found {}".format(input_str))
    else:
        await a.edit("Syntax // .rnupload file.name as reply to a Telegram media")
