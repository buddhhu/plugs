#Modded from dagd.py
"""
Animate How To Google
Command .ggl Search Query
By @loxxi
"""

from telethon import events
import requests

@plus_ub(pattern="ggl (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(input_str.replace(" ","+"))
    response_api = requests.get(sample_url).text
    if response_api:
        await event.reply("[{}]({})\n`Thank me Later 🙃` ".format(input_str,response_api.rstrip()))
    else:
        await event.reply("something is wrong. please try again later.")
