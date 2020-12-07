# For @UniBorg
# (c) Shrimadhav U K

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest

@plus_ub(pattern="listmyusernames", from_users=sudo)

async def mine(event):
    """ For .reserved command, get a list of your reserved usernames. """
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await event.reply(output_str)
