# Lots of lub to @r4v4n4 for gibing the base <3
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

@plus_ub(pattern="scan ?(.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.reply("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.reply("```reply to a media message```")
       return
    chat = "@DrWebBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.reply("```Reply to actual users message.```")
       return
    a = await event.reply(" `Sliding my tip, of fingers over it`")
    async with plus.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
              await plus.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await a.edit("```Please unblock @sangmatainfo_bot and try again```")
              return
          if response.text.startswith("Forward"):
             await a.edit("```can you kindly disable your forward privacy settings for good?```")
          else:
          	if response.text.startswith("Select"):
          		await a.edit("`Please go to` @DrWebBot `and select your language.`") 
          	else: 
          			await a.edit(f"**Antivirus scan was completed. I got dem final results.**\n {response.message.message}")
