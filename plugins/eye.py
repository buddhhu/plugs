"""COMMAND : .eye"""

from telethon import events

import asyncio



@plus_ub(pattern="eye", from_users=sudo)

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "eye":

    a = await event.reply("👁👁")

    animation_chars = [

            "👁👁\n  👄  =====> Abey Ja Na Gandu",
            "👁👁\n  👅  =====> Abey Ja Na Madarchod",    
            "👁👁\n  💋  =====> Abey Ja Na Randi",
            "👁👁\n  👄  =====> Abey Ja Na Betichod",
            "👁👁\n  👅  =====> Abey Ja Na Behenchod",    
            "👁👁\n  💋  =====> Abey Ja Na Na Mard",
            "👁👁\n  👄  =====> Abey Ja Na Randi",
            "👁👁\n  👅  =====> Abey Ja Na Bhosdk",    
            "👁👁\n  💋  =====> Abey Ja Na Chutiye",
            "👁👁\n  👄  =====> Hi All, How Are You Guys..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await edit.edit(animation_chars[i % 103])
