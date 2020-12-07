from userbot.google_images_download import googleimagesdownload
import os
import shutil
from re import findall
from userbot import CMD_HELP

@plus_ub(pattern="img ?(.*)", from_users=sudo)
async def img_sampler(event):
    a = await event.reply("`Processing....`")
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply.text:
        query = reply.message
    else:
    	await a.edit("`What I am Supposed to Search `")
    	return
        
    lim = findall(r"lim=\d+", query)
    # lim = event.pattern_match.group(1)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = (Var.TG_GLOBAL_ALBUM_LIMIT)
    response = googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory"
    }

    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(await event.client.get_input_entity(event.chat_id), lst, caption=query)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()
    await a.delete()

CMD_HELP.update({"img": "`.img <Name>` or `.img (replied message)`\
    \nUSAGE: do google image search and sends images." 
})    
