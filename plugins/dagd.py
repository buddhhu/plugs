"""DA.GD helpers in @UniBorg
Available Commands:
.dns google.com
.url <long url>
.unshort <short url>"""
from telethon import events
import os
import requests
import json


@plus_ub(pattern="dns (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.reply("DNS records of {} are \n{}".format(input_str, response_api))
    else:
        await event.reply("i can't seem to find {} on the internet".format(input_str))


@plus_ub(pattern="url (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.reply("Generated {} for {}.".format(response_api, input_str))
    else:
        await event.reply("something is wrong. please try again later.")


@plus_ub(pattern="unshort (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith('3'):
        await event.reply("Input URL: {}\nReDirected URL: {}".format(input_str, r.headers["Location"]))
    else:
        await event.reply("Input URL {} returned status_code {}".format(input_str, r.status_code))
