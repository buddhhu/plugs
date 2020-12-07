from telethon import events
import subprocess, io, asyncio, time
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError


@plus_ub(pattern="webupload ?(?:(.*?) \| )?(.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    a = await event.reply("Processing ...")
    PROCESS_RUN_TIME = 100
    input_str = event.pattern_match.group(1)
    selected_transfer = event.pattern_match.group(2)
    if input_str:
        file_name = input_str
    else:
        reply = await event.get_reply_message()
        file_name = await event.client.download_media(reply.media, Var.TEMP_DOWNLOAD_DIRECTORY)
    reply_to_id = event.message.id
    CMD_WEB = {"anonfiles": "curl -F \"file=@{}\" https://anonfiles.com/api/upload", "transfer": "curl --upload-file \"{}\" https://transfer.sh/", "anonymousfiles": "curl -F file=\"@{}\" https://api.anonymousfiles.io/", "bayfiles": "curl -F \"file=@{}\" https://bayfiles.com/api/upload"}
    try:
        selected_one = CMD_WEB[selected_transfer].format(file_name)
    except KeyError:
        await a.edit("Invalid selected Transfer")
    cmd = selected_one
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    await a.edit(f"{stdout.decode()}")