#Credit: @r4v4n4
"""Emoji

Available Commands:

.fleave"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@plus_ub(pattern=r"(.*)", from_users=sudo)

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 17)

    input_str = event.pattern_match.group(1)

    if input_str == "fleave":

        a = await event.reply(input_str)

        animation_chars = [
        
            "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
            "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",    
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
            "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
            "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
            "**Chat Message Exported To** `./Inpu/`",
            "**Chat Message Exported To** `./Inpu/homework/`",
            "**Chat Message Exported To** `./Inpu/homework/groupchat.txt`",
            "__Legend is leaving this chat.....! Gaand Marao Bc..__",
            "__Legend is leaving this chat.....! Gaand Marao Bc..__"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await a.edit(animation_chars[i % 17])
