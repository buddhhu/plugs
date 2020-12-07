"""Color Plugin for @UniBorg
Syntax: .color <color_code>"""
from telethon import events
import os
from PIL import Image, ImageColor


@plus_ub(pattern="color (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    if input_str.startswith("#"):
        try:
            usercolor = ImageColor.getrgb(input_str)
        except Exception as e:
            await event.client.send_message(event.chat_id, str(e))
            return False
        else:
            im = Image.new(mode="RGB", size=(1280, 720), color=usercolor)
            im.save("UniBorg.png", "PNG")
            input_str = input_str.replace("#", "#COLOR_")
            await event.client.send_file(
                event.chat_id,
                "UniBorg.png",
                force_document=False,
                caption=input_str,
                reply_to=message_id
            )
            os.remove("UniBorg.png")
            await event.delete()
    else:
        await event.client.send_message(event.chat_id, "Syntax: `.color <color_code>`")
