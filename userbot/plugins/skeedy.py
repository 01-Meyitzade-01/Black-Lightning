# Created By @krish1303y For Black Lightning


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="skeedy?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SkeddyBot"
    await event.edit("```Wait...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message("Asia/Kolkata")
            await conv.get_response()
            await conv.send_message("➕Add" + input_str)
            await conv.get_response()
            await borg.send_message(event.chat_id, audio.text)
            await event.delete()
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SkeddyBot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("👀")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)   
