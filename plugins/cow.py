""".cowsay, .tuxsay, .milksay, .kisssay, .wwwsay, .defaultsay, .bunnysay,
.moosesay, .sheepsay, .rensay, .cheesesay, .ghostbusterssay, .skeletonsay,
and may cmd would be added soon."""


import asyncio
from telethon import events
from cowpy import cow


@plus_ub(pattern=r"(\w+)say (.*)", from_users=sudo)
async def univsaye(cowmsg):
    """ For .cowsay module, uniborg wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.client.send_message(cowmsg.chat_id, f"`{cheese.milk(text).replace('`', '´')}`")
