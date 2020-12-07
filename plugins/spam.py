import time, os, subprocess, pybase64, asyncio
from asyncio import wait, sleep
from userbot import CMD_HELP
from telethon.tl.functions.messages import ImportChatInviteRequest as Get


@plus_ub(pattern = "spam ?(.*)", from_users=sudo)
#@bot2.on(admin_cmd(pattern="spam ?(.*)"))
async def spammer(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    e = event
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    cat = event.pattern_match.group(1).split(' ', 1)		
    counter = int(cat[0])	
    if len(cat)==2:
        spam_message = str(event.pattern_match.group(1).split(' ', 1)[1])
        await event.delete()
        for i in range(counter):
            if event.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
                await asyncio.sleep(0.5)
            else:
               await event.client.send_message(event.chat_id , spam_message)
               await asyncio.sleep(0.5)
        if Var.BOTLOG:
            if event.is_private:
                await event.client.send_message(Var.BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in [User](tg://user?id={event.chat_id}) chat with {counter} messages of \n" +f"`{spam_message}`")
            else:
                await event.client.send_message(Var.BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in {event.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n" +f"`{spam_message}`")
    elif reply_to_id.media:
        to_download_directory = Var.TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, "spam")
        downloaded_file_name = await event.client.download_media(reply_to_id.media, downloaded_file_name)
        await event.delete()		
        if os.path.exists(downloaded_file_name):
            for i in range(counter):
                await event.client.send_file(
                    event.chat_id,
                    downloaded_file_name
                    ) 
                await asyncio.sleep(1)
            if BOTLOG:
                if event.is_private:
                    await event.client.send_message(Var.BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} times with below message")
                    await event.client.send_file(Var.BOTLOG_CHATID, downloaded_file_name)
                    os.system(f"rm -rf {downloaded_file_name}")
                else:
                    await event.client.send_message(Var.BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) with {counter} times with below message") 
                    await event.client.send_file(Var.BOTLOG_CHATID, downloaded_file_name)
                    os.system(f"rm -rf {downloaded_file_name}")
    elif reply_to_id.text and e.reply_to_msg_id:
        spam_message = 	reply_to_id.text
        await event.delete()
        for i in range(counter):
            if event.reply_to_msg_id:
                await reply_to_id.reply(spam_message)
                await asyncio.sleep(0.5)
            else:
               await event.client.send_message(event.chat_id , spam_message)
               await asyncio.sleep(0.5)
        if BOTLOG:
            if event.is_private:
                await event.client.send_message(Var.BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in [User](tg://user?id={e.chat_id}) chat with {counter} messages of \n" +f"`{spam_message}`")
            else:
                await event.client.send_message(Var.BOTLOG_CHATID, "#SPAM\n" +f"Spam was executed successfully in {e.chat.title}(`{e.chat_id}`) chat  with {counter} messages of \n" +f"`{spam_message}`")
