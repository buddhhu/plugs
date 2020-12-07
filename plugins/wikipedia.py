
"""WikiPedia.ORG
Syntax: .wikipedia Query"""
from telethon import events
import wikipedia

@plus_ub(pattern="wikipedia (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    a = await event.reply("Processing ...")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
    await a.edit("WikiPedia **Search**: {} \n\n **Result**: \n\n{}".format(input_str, result))
