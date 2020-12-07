"""Find Movies Fast"""
# Made by- @DeletedUser420 idea- @AnInnocentboy and then kanged by me
# Ported by @buddhhu

from typing import Tuple, Optional
from telethon.tl.types import InputMessagesFilterVideo
from .. import CMD_HELP

CMD_HELP.update({
    "movies":
    ".movie <movie_name>\
"
})

@plus_ub(pattern="movie (.*)", from_users=sudo)
async def movie_search(event):
    """get movie from channel"""
    movie = event.pattern_match.group(1)
    if not movie:
        await event.reply("Provide a movie name")
        return
    search = await event.reply("♥ __Searching For__ **{}**".format(movie))
    chat_id = event.chat_id
    f_id = ""
    f_ref = ""
    async for msg in event.client.iter_messages("@alpacinodump", search=movie,  limit=2, filter=InputMessagesFilterVideo):
    	if msg:
    		caption = movie
    		await event.client.send_file(chat_id, msg, caption=caption, supports_streaming=True)
    		await search.delete()
    		await event.delete()
    	else:
    		await event.reply(f"{movie} **not found**")
    		await search.delete()
    		await event.delete()
