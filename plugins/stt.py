"""Speech to Text
Syntax: .stt <Language Code> as reply to a speech message"""
from telethon import events
import requests
import os
from datetime import datetime


@plus_ub(pattern="stt (.*)", from_users=sudo)
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    a = await event.reply("Downloading to my local, for analysis 🙂......")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        required_file_name = await event.client.download_media(
            previous_message,
            Var.TEMP_DOWNLOAD_DIRECTORY
        )
        lan = input_str
        if Var.IBM_WATSON_CRED_URL is None or Var.IBM_WATSON_CRED_PASSWORD is None:
            await a.edit("You need to set the required ENV variables for this module. \nModule stopping")
        else:
            await a.edit("Starting analysis, using IBM WatSon Speech To Text")
            headers = {
                "Content-Type": previous_message.media.document.mime_type,
            }
            data = open(required_file_name, "rb").read()
            response = requests.post(
                Var.IBM_WATSON_CRED_URL + "/v1/recognize",
                headers=headers,
                data=data,
                auth=("apikey", Var.IBM_WATSON_CRED_PASSWORD)
            )
            r = response.json()
            if "results" in r:
                # process the json to appropriate string format
                results = r["results"]
                transcript_response = ""
                transcript_confidence = ""
                for alternative in results:
                    alternatives = alternative["alternatives"][0]
                    transcript_response += " " + str(alternatives["transcript"]) + " + "
                    transcript_confidence += " " + str(alternatives["confidence"]) + " + "
                end = datetime.now()
                ms = (end - start).seconds
                if transcript_response != "":
                    string_to_show = "Language: `{}`\nTRANSCRIPT: `{}`\nTime Taken: {} seconds\nConfidence: `{}`".format(lan, transcript_response, ms, transcript_confidence)
                else:
                    string_to_show = "Language: `{}`\nTime Taken: {} seconds\n**No Results Found**".format(lan, ms)
                await a.edit(string_to_show)
            else:
                await a.edit(r["error"])
            # now, remove the temporary file
            os.remove(required_file_name)
    else:
        await a.edit("Reply to a voice message, to get the relevant transcript.")
