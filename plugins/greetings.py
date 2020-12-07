# Credits @buddhhu
# This software is a part of https://github.com/buddhhu/Plus

from global_variables_sql import GN, GM, LIKE, LOL

@plus_ub(pattern="gn", from_users=sudo)
async def gn(event):
    await event.reply(f"{GN}")
    await event.delete()
    

@plus_ub(pattern="gudmrng", from_users=sudo)
async def gm(event):
    await event.reply(f"{GM}")
    await event.delete()


@plus_ub(pattern="like", from_users=sudo)
async def like(event):
    await event.reply(f"{LIKE}")
    await event.delete()


@plus_ub(pattern="lol", from_users=sudo)
async def lol(event):
    await event.reply(f"{LOL}")
    await event.delete()

