# (c) @UniBorg

from telethon import events
import asyncio
from collections import deque

@plus_ub(pattern="thinklol", from_users=sudo)
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🤔🧐🤔🧐🤔🧐"))
	a = await event.reply("Thinking...")
	for _ in range(60):
		await asyncio.sleep(0.1)
		await a.edit("".join(deq))
		deq.rotate(1)
    
