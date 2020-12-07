"""Emoji
Available Commands:
.support
Credits to noone
"""

from telethon import events

import asyncio

@plus_ub(pattern="support", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "support":
    a = await event.reply("For our support group")
    animation_chars = [
            "Click [here](https://t.me/pIusub)"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await a.edit(animation_chars[i % 18], preview_link=False)
