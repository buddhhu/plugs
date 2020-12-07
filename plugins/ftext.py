from telethon import events
import asyncio, os, sys


@plus_ub(pattern="ftext ?(.*)", from_users=sudo)
async def payf(event):
    input_str=event.pattern_match.group(1)
    if input_str:
        paytext=input_str
        pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
    else:
        pay = "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯\n"
    await event.reply(pay)
