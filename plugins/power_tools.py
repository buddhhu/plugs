"""Restart or Terminate the bot from any chat
Available Commands:
.softupdate"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import os, sys, asyncio

@plus_ub(pattern="softupdate", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    regex = Var.COMMAND_HAND_LER
    await event.client.send_message(event.chat_id, f"**Softupdate in progress.**\nDo `{regex}ping` or `{regex}alive` after **1 min**. to check I am alive.")
    await event.delete()
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
