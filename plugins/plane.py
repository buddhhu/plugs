"""By STARKTM1
cmd : .plane"""
import asyncio

@plus_ub(pattern="plane", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
        
        
    a = await event.reply("✈-------------")
    await a.edit("-✈------------")
    await a.edit("--✈-----------")
    await a.edit("---✈----------")
    await a.edit("----✈---------")
    await a.edit("-----✈--------")
    await a.edit("------✈-------")
    await a.edit("-------✈------")
    await a.edit("--------✈-----") 
    await a.edit("---------✈----")
    await a.edit("----------✈---")
    await a.edit("-----------✈--")
    await a.edit("------------✈-")
    await a.edit("-------------✈")
    await asyncio.sleep(3)
    await event.delete()
    await a.delete()

