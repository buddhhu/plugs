#credits: @buddhhu
import asyncio
from datetime import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

@plus_ub(pattern="ascii", from_users=sudo)
async def _(event):
	if event.fwd_from:
		return
	if not event.reply_to_msg_id:
		await event.reply("`Reply to any user message` **Bruh**")
		return
	reply_message = await event.get_reply_message() 
	if not reply_message.media:
		await event.reply("`Reply to an image` **Bruh**")
		return
	start = datetime.now()
	chat = "@asciiart_bot"
	sender = reply_message.sender
	if reply_message.sender.bot:
		await event.reply(
		"Reply to actual users message."
		)
		return
	downloaded_file_name = await event.client.download_media(reply_message, Var.TEMP_DOWNLOAD_DIRECTORY)
	end = datetime.now()
	ms = (end - start).seconds
	a = await event.reply("Downloaded to `{}` in **{}** seconds.".format(downloaded_file_name, ms))
	async with borg.conversation(chat) as conv:
		try:
			await conv.send_message("/start")
			response = await conv.get_response()
			await conv.send_file(downloaded_file_name)
			ascii = await conv.get_response()
			await event.client.send_file(event.chat_id, ascii, caption="💠**Here's the requested ascii image!**💠\n\n   `Check out` [Plus+ UserBot](https://github.com/amitsharma123234/Plus)\n\n", link_preview=False, force_document=False, reply_to=reply_message)
			await event.delete()
			await a.delete()
		except YouBlockedUserError:
			await a.edit("**Error:** `unblock` @asciiart_bot `and retry!`")
			await event.delete()