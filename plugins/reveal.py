# Credits @itzsjdude
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved

import os
@plus_ub(pattern=r"reveal$", from_users=sudo)
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, 'r')
    c = a.read()
    a.close()
    a = await event.reply("**Reading file...**")
    if len(c) > 4095:
    	await a.edit('`The Total words in this file is more than telegram limits.`')
    else:
    	await event.client.send_message(event.chat_id, f"```{c}```")
    	await a.delete()
    os.remove(b)
    await event.delete()