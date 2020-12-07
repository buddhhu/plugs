# Fixed by @buddhhu & @itzsjdude

from telethon.tl.types import InputMessagesFilterDocument
from ..utils import remove_plugin, load_module
from pathlib import Path
import userbot.utils
import os
chat = Var.PLUGIN_GROUP

@plus_ub(pattern=r"installall$", from_users=sudo)
async def install(event):
	if event.fwd_from:
		return
	documentss = await event.client.get_messages(chat, None ,search='.py', filter=InputMessagesFilterDocument)
	total = int(documentss.total)
	total_doxx = range(0, total)
	b = await event.client.send_message(event.chat_id, f"**Installing {total} plugins...**")
	text =  "**Installing Plugins...**\n\n"
	a = await event.client.send_message(chat, text)
	if total == 0:
		await a.edit("**No plugins to install.**")
		await event.delete()
		return
	for ixo in total_doxx:
		mxo = documentss[ixo].id
		downloaded_file_name = await event.client.download_media(await event.client.get_messages(chat, ids=mxo), "userbot/plugins/")
		if "(" not in downloaded_file_name:
			path1 = Path(downloaded_file_name)
			shortname = path1.stem
			try:
				load_module(shortname.replace(".py", ""))
				text += f"**• Installed** `{(os.path.basename(downloaded_file_name))}` **successfully.**\n"
			except:
				text += f"**• Error installing** `{(os.path.basename(downloaded_file_name))}`\n"
		else:
			text += f"**• Plugin** `{(os.path.basename(downloaded_file_name))}` **already installed.**\n"
		await a.edit(f"{text}\n**Installed every plugin.**")
		await event.delete()