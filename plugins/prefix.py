# This software is a part of https://github.com/buddhhu/Plus
# Credits @buddhhu


sudo = Var.SUDO_USERS
handler = Var.COMMAND_HAND_LER
from telethon import events
@plus.on(events.NewMessage(pattern="^.prefix", from_users=sudo))
async def prefix(event):
	await event.reply(handler + "     👈 is your current prefix for plugins")
	await event.delete()