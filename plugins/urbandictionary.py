# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Urban Dictionary
Syntax: .ud Query"""
from telethon import events
import asyncurban


@plus_ub(pattern="ud (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    a = await event.reply("processing...")
    word = event.pattern_match.group(1)
    urban = asyncurban.UrbanDictionary()
    try:
        mean = await urban.get_word(word)
        await a.edit("Text: **{}**\n\nMeaning: **{}**\n\nExample: __{}__".format(mean.word, mean.definition, mean.example))
    except asyncurban.WordNotFoundError:
        await a.edit("No result found for **" + word + "**")
