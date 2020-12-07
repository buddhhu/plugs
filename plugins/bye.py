# For @UniBorg

# Courtesy @yasirsiddiqui

"""

.leave

"""



from telethon.tl.functions.channels import LeaveChannelRequest

import time





@plus_ub(pattern="bye", from_users=sudo)

async def leave(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.reply("`I am leaving this chat.....!`")

        time.sleep(3)

        if '-' in str(e.chat_id):

            await e.client(LeaveChannelRequest(e.chat_id))

        else:

            await e.reply('`Sir This is Not A Chat`')
