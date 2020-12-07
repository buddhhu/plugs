#Credits @Itzsjdude
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved


import asyncio

@plus_ub(pattern="find (.*)", from_users=sudo)
async def _(event):
    chat='@songdl_Bot'
    input_str = str(event.text[6:])
    if 'spotify' in input_str:
    	lund = await event.reply("**Searching your requested song...**")
    	await event.client.send_message(chat, input_str)
    	await asyncio.sleep(3)
    	huuh = await event.client.get_messages(chat)
    	if 'wrong' in huuh[0].message:
    		await lund.edit('**Cannot download song from spotify☹️**')
    		await event.delete()
    	else:
    		await event.client.send_file(event.chat_id, huuh, caption='')
    		await event.delete()
    		await lund.delete()
    else:
    	chut = await event.reply(f'**Searching for** `{input_str}`')
    	async with event.client.conversation(chat) as bot_conv:
    		await event.client.send_message(chat, input_str)
    		await asyncio.sleep(10)
    		reply = await event.client.get_messages(chat)
    		if "Pick" in reply[0].message:
    			await chut.edit('**Sending Your requested song...**')
    			await reply[0].click(0)
    			await asyncio.sleep(3)
    			a = await event.client.get_messages(chat)
    			ac = a[0]
    			await event.client.send_file(event.chat_id, ac, caption=f'**{input_str}\nUploaded by [Plus+ Userbot](t.me/plusub)**')
    			await chut.delete()
    			await event.delete()
    		else:
    			await chut.edit("**Failed to get your song...**")
    			await event.delete()
    
    