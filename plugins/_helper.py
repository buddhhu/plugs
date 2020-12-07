from userbot import CMD_LIST
from userbot.utils import admin_cmd
import sys, io
from telethon import events, functions, __version__

@plus_ub(pattern=r"help ?(.*)", from_users=sudo)
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername == None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "🇮🇳 " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                with io.BytesIO(str.encode(string)) as out_file:
                    out_file.name = "cmd.txt"
                    await tgbot.send_file(
                        event.sender_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="**COMMANDS**",
                    )
                    await event.delete()
            else:
                await event.reply(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.reply(string)
            else:
                await event.reply(input_str + " is not a valid plugin!")
        else:
            help_string = """Userbot Helper.. \nProvided by [Plus+ UserBot](https://t.me/plusub)\n`Userbot Helper to reveal all the commands`"""
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername,
                help_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()

@plus_ub(pattern="syntax (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    if plugin_name in CMD_LIST:
        help_string = [plugin_name].__doc__
        unload_string = f"Use `.unload {plugin_name}` to remove this plugin.\n           © @UniBorg"
        if help_string:
            plugin_syntax = f"Syntax for plugin **{plugin_name}**:\n\n{help_string}\n{unload_string}"
        else:
            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin."
    else:
        plugin_syntax = "Enter valid **Plugin** name.\nDo `.plugins` or `.help` to get list of valid plugin names."
    await event.reply(plugin_syntax)