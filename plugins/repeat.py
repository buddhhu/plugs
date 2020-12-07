import asyncio
from asyncio import wait


@plus_ub(pattern="repeat ?(.*)", from_users=sudo)
async def _(event):
    message = event.text[10:]
    count = int(event.text[8:10])
    repmessage = message * count
    await wait([event.respond(repmessage)for i in range(count)])
    await event.delete()
