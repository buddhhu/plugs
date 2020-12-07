#  (c)2020 TeleBot
#
# You may not use this plugin without proper authorship and consent from @TeleBotSupport
# Credits @xditya for creating
# Credits @itzsjdude for porting

from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio, os

KK = os.environ.get("FBAN_GROUP_ID", None)
if KK:
     KK = int(KK)
EX = os.environ.get("EXCLUDE_FED", None)


# By @HeisenbergTheDanger, @its_xditya
@plus_ub(pattern="superfban ?(.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Starting a Mass-FedBan...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        FBAN = previous_message.sender_id
        REASON = event.pattern_match.group(1)
        if REASON.strip() == "":
            REASON = " #TBMassBanned "
    else:
        arg = event.pattern_match.group(1)
        args = arg.split()
        if len(args) > 1:
            FBAN = args[0]
            REASON = ""
            for a in args[1:]:
                REASON += (a + " ")
        else:
            FBAN = arg
            REASON = " #TBMassBanned "
    try:
        int(FBAN)
        if int(FBAN) == 667805879 or int(FBAN) == 779890498 or int(FBAN) == 988398034:
            await event.reply("Something went wrong.")
            return
    except:
        if FBAN == "@buddhhu" or FBAN == "@itzsjdude" or FBAN == "@MrPeRfEcT_Official":
            return
    if KK:
        chat = KK
    else:
        chat = await event.get_chat()
    fedList = []
    async with event.client.conversation("@MissRose_bot") as bot_conv:
        await bot_conv.send_message("/start")
        await asyncio.sleep(3)
        await bot_conv.send_message("/myfeds")
        await asyncio.sleep(3)
        response = await bot_conv.get_response()
        await asyncio.sleep(3)
        if "make a file" in response.text:
            await asyncio.sleep(8)
            await response.click(0)
            fedfile = await bot_conv.get_response()
            if fedfile.media:
                downloaded_file_name = await event.client.download_media(
                fedfile,
                "fedlist"
                )
                file = open(downloaded_file_name, 'r')
                lines = file.readlines()
                for line in lines:
                    fedList.append(line[:line.index(":")])
            else:
                return
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("Try again after 5 mins.")
            return
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True
                    
            elif In:
                tempFedId += x

    await event.edit(f"Fbaning in {len(fedList)} feds.")
    try:
        await event.client.send_message(chat, f"/start")
    except:
        await event.edit("FBAN_GROUP_ID is incorrect.")
        return
    await asyncio.sleep(6)
    if EX:
        excludeFed = EX.split("|")
        for n in range(len(excludeFed)):
            excludeFed[n] = excludeFed[n].strip()
    exCount = 0
    for fed in fedList:
        if EX and fed in excludeFed:
            await event.client.send_message(chat, f"{fed} Excluded.")
            exCount += 1
            continue
        await event.client.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(6)
        await event.client.send_message(chat, f"/fban {FBAN} {REASON}")
        await asyncio.sleep(6)
    await event.edit(f"SuperFBan Completed. Affected {len(fedList) - exCount} feds.\n#TB")  
# By @HeisenbergTheDanger, @its_xditya
@plus_ub(pattern="superunfban ?(.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Starting a Mass-UnFedBan...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        FBAN = previous_message.sender_id
    else:
        FBAN = event.pattern_match.group(1)
    
    if KK:
        chat = KK
    else:
        chat = await event.get_chat()
    fedList = []
    async with event.client.conversation("@MissRose_bot") as bot_conv:
        await bot_conv.send_message("/start")
        await bot_conv.send_message("/myfeds")
        response = await bot_conv.get_response()
        if "make a file" in response.text:
            await asyncio.sleep(8)
            await response.click(0)
            fedfile = await bot_conv.get_response()
            if fedfile.media:
                downloaded_file_name = await event.client.download_media(
                fedfile,
                "fedlist"
                )
                file = open(downloaded_file_name, 'r')
                lines = file.readlines()
                for line in lines:
                    fedList.append(line[:line.index(":")])
            else:
                return
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("Try again after 5 mins.")
            return
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True
                    
            elif In:
                tempFedId += x

    await event.edit(f"UnFbaning in {len(fedList)} feds.")
    try:
        await event.client.send_message(chat, f"/start")
    except:
        await event.edit("FBAN_GROUP_ID is incorrect.")
        return
    await asyncio.sleep(6)
    for fed in fedList:
        await event.client.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(6)
        await event.client.send_message(chat, f"/unfban {FBAN}")
        await asyncio.sleep(6)
    await event.edit(f"SuperUnFBan Completed. Affected {len(fedList)} feds.\n#TB")  
# By @HeisenbergTheDanger, @its_xditya

"""
.superfban <username/userid> <reason>\
\n**Usage**: Mass-Ban in all feds you are admin in.\
\nSet `EXCLUDE_FED fedid1|fedid2` in heroku vars to exclude those feds.\
\nSet var `FBAN_GROUP_ID` ti the group with rose, where you want FBan to take place.\
\n\nGet help - @TeleBotSupport\
"""
