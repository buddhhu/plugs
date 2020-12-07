import asyncio, zipfile, time, os
from plus.utils import time_formatter

@plus_ub(pattern="compress ?(.*)", from_users=sudo)

async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    mone = await event.reply("Processing ...")

    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):

        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)

    if event.reply_to_msg_id:

        reply_message = await event.get_reply_message()

        try:

            downloaded_file_name = await event.client.download_media(

                reply_message,

                Var.TEMP_DOWNLOAD_DIRECTORY

                

            )

            directory_name = downloaded_file_name

            await mone.edit("Finish downloading to my local")

            zipfile.ZipFile(directory_name + '.zip', 'w', zipfile.ZIP_DEFLATED).write(directory_name)

            await event.client.send_file(

                event.chat_id,

                directory_name + ".zip",

                caption="**Zipped By [Plus+ UserBot](https://t.me/plusub)**",

                force_document=True,

                allow_cache=False,

                reply_to=event.message.id,

            )

            try:

                os.remove(directory_name + ".zip")

                os.remove(directory_name)

            except:

                    pass

            await mone.edit("task Completed")

            await asyncio.sleep(3)

            await event.delete()

        except Exception as e:  # pylint:disable=C0103,W0703

            await mone.edit(str(e))

    elif input_str:

        directory_name = input_str

        zipfile.ZipFile(directory_name + '.zip', 'w', zipfile.ZIP_DEFLATED).write(directory_name)

        await mone.edit("Local file compressed to `{}`".format(directory_name + ".zip"))
