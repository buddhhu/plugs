"""use command .ddgo"""

from telethon import events
import os
import requests
import json


@plus_ub(pattern="ddgo (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ","+"))
    if sample_url:
        link = sample_url.rstrip()
        await event.reply("Let me  DuckDuckGo that for you:\n [{}]({})".format(input_str, link))
    else:
        await event.reply("something is wrong. please try again later.")
