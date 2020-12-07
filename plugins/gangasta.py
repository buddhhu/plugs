from telethon import events
import random, re, asyncio

@plus_ub(pattern="gangasta ?(.*)", from_users=sudo)
async def _(event):
	a = await event.reply("EVERyBOdy")
	await asyncio.sleep(0.3)
	await a.edit("iZ")
	await asyncio.sleep(0.2)
	await a.edit("GangSTur")
	await asyncio.sleep(0.5)
	await a.edit("UNtIL ")
	await asyncio.sleep(0.2)
	await a.edit("I")
	await asyncio.sleep(0.3)
	await a.edit("ArRivE")
	await asyncio.sleep(0.3)
	await a.edit("🔥🔥🔥")
	await asyncio.sleep(0.3)
	await a.edit("EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥🔥🔥")
