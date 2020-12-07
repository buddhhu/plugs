# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from telethon import events

@plus_ub(pattern="tagall", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    mentions = "Taged All?"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 50000):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()
