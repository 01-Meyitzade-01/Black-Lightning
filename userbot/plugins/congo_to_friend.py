import random

from uniborg.util import edit_or_reply, admin_cmd, sudo_cmd

from userbot import CMD_HELP

RUNSREACTS = [
    "`Aur Bata Bsdk Kar Liya Tunee Party De Chal!`",
    "`Chal Gand Phad Dunga Udd Mat Abb`",
    "`Oo Wow Mere Beta Sikh Gaya!`",
    "`Chall Badhiya Congo`",
    "`Fuck You And Congo.`",
    "`Mere Ladke Lavde te lashan Akhir  Karliya Tune.`",
    "`Very Good.`",
    "`Veryy Good Nhi Bulanga Bass Tu Chutiya H!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
]



admin = "admin"

@admin.on(admin_cmd(pattern="congo"))
@admin.on(sudo_cmd(pattern="congo", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(RUNSREACTS) - 1)
    reply_text = RUNSREACTS[bro]
    await edit_or_reply(event, reply_text)


CMD_HELP.update(
    {
        "congo_to_friend": "**congo_to_friend**\
\n\n**Syntax : **`.congo2`\
\n**Usage :** This plugin is used to congratulate friend."
    }
)
