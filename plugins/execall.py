import subprocess, io, asyncio, time, inspect, traceback, sys
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
from telethon import events, errors, functions, types
from .. import CMD_HELP

CMD_HELP.update({
    "execall":
    ".bash <terminal cmds>\
\nUsage: Runs terminal cmds\
\n\n.eval python cmds\
\nUsage: Runs python cmds\ "
})


@plus_ub(pattern="bash ?(.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    start_time = time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "No output"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"**• COMMAND:**\n`{cmd}` \n\n**• PID:**\n`{process.pid}`\n\n**• ERROR:** \n`{e}`\n\n**• OUTPUT:**\n`{o}`"
    if len(OUTPUT) > 4095:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "bash.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
            await event.delete()
    await event.reply(OUTPUT)
    await event.delete()

@plus_ub(pattern="eval", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    a = await event.reply("Processing ...")
    cmd = event.text.split(" ", maxsplit=1)[1]
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "**• EVAL**:\n`{}` \n\n**• OUTPUT**:\n`{}` \n".format(cmd, evaluation)

    if len(final_output) > 4095:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
            await event.delete()
    else:
        await a.edit(final_output)
        await event.delete()


async def aexec(code, event):
    exec(
        f'async def __aexec(event): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](event)
