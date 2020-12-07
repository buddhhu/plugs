"""Emoji
Available Commands:
.wtf"""

from telethon import events
import asyncio

@plus_ub(pattern="wtf", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    a = await event.reply("wtf")
    animation_chars = [
            "What",
            "What The",
            "What The Fuk",
            "What The Fuk Brah",
            "[What The Fuk Brah](https://telegra.ph//file/f3b760e4a99340d331f9b.jpg)"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await a.edit(animation_chars[i %5 ], link_preview=True)
