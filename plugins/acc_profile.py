import os
from telethon import events
from telethon.tl import functions
from .. import CMD_HELP

CMD_HELP.update({
    "acc_profile":
    ".pbio <bio>\
\n**Usage**: To change bio \
\n\n.ppic \
\n**Usage**: Reply to a pic to set it as your profile pic \
\n\n.pname <name> \
\n**Usage**: .pname first_name \n last_name "
})

@plus_ub(pattern="pbio (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            about=bio
        ))
        await event.client.send_message(event.chat_id, "Succesfully changed my profile bio")
        await event.delete()
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.client.send_message(event.chat_id, str(e))
        await event.delete()


@plus_ub(pattern="pname ((.|\n)*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if  "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await event.client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
            first_name=first_name,
            last_name=last_name
        ))
        await event.client.send_message(event.chat_id, "My name was changed successfully")
        await event.delete()
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.client.send_message(event.chat_id, str(e))
        await event.delete()


@plus_ub(pattern="ppic", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    a = await event.client.send_message(event.chat_id, "Downloading Profile Picture to my local ...", reply_to=reply_message)
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    photo = None
    try:
        photo = await event.client.download_media(  # pylint:disable=E0602
            reply_message,
            Var.TEMP_DOWNLOAD_DIRECTORY  # pylint:disable=E0602
        )
        await event.delete()
    except Exception as e:  # pylint:disable=C0103,W0703
        await a.edit(str(e))
    else:
        if photo:
            await a.edit("now, Uploading to @Telegram ...")
            file = await event.client.upload_file(photo)  # pylint:disable=E0602
            try:
                await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                    file
                ))
            except Exception as e:  # pylint:disable=C0103,W0703
                await a.edit(str(e))
            else:
                await a.edit("My profile picture was succesfully changed")
                await event.delete()
    try:
        os.remove(photo)
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
