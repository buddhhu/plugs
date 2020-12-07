from datetime import datetime
@plus_ub(pattern="ping", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    a = await event.client.send_message(event.chat_id, "Pong!")
    await event.delete()
    end = datetime.now()
    ms = (end - start).microseconds / 100000
    await a.edit("Pong!\n**{:.2f} ms**".format(ms))