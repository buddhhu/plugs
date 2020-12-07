from telethon import events
import asyncio


@plus_ub(pattern="undlt ?(.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    c = await event.get_chat()
    limit = event.pattern_match.group(1)
    if c.admin_rights or c.creator:
        a = await event.client.get_admin_log(event.chat_id, limit, search="", edit=False, delete=True)
        for i in a:
          await event.reply(i.original.action.message)
    else:
        a = await event.reply("You need administrative permissions in order to do this command")
        await event.delete()
        await asyncio.sleep(3)
        await a.delete()
        
