from telethon import events

import asyncio
from userbot.utils import admin_cmd
from telethon.tl.functions.users import GetFullUserRequest



@borg.on(admin_cmd(pattern=r"gmailhack"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 20)

    #input_str = event.pattern_match.group(1)

    #if input_str == "hack":

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        if idd==953414679:
            await event.edit("`Wait a second, This is my boss!`\n**How dare you threaten to hack my boss' google account stupid!**\n\n__Your account will be hacked in a few minutes! Pay 99$ to my Boss__ [IndianBhai](https://t.me/pureindialover) __OR delete your telegram account to prevent the virus getting into your Gmail account __😏")
        else:
            await event.edit("Hacking Gmail..")
            animation_chars = [
        
            "`Connecting To Dark WEB Secret Server...`",
            "`Connection Successful!`",
            "`Targetting` this dumb's `Google Account.`",
            "`Attempting method I... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method I FAILED!`",
            "`Attempting method II... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Method II Out Of Order!`",
            "`Attempting method III... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Disabling Account Security... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Getting Password... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Pulling Information... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Modifying Recovery Information... 69%\n█████████████████▒▒▒▒▒▒▒▒ `",
            "`Hacking... 74%\n███████████████████▒▒▒▒▒▒ `",
            "`Hacking.... 80%\n█████████████████████▒▒▒▒ `",
            "`Adding Modules... 86%\n██████████████████████▒▒▒ `",
            "`Adding Finishing Touches... 98%\n████████████████████████▒`",
            "`HACKED 100%\n█████████████████████████ `",
            "`Targeted Google Account Hacked Successfully...`\nThis dumb user's __account is under Boss' control now__\n\n**Pay 99$ To** @pureindialover **Or Get Ready To See Your E-Mail and YouTube Channel Spamming Everywhere.**"

        ]

            for i in animation_ttl:

                await asyncio.sleep(animation_interval)

                await event.edit(animation_chars[i % 20])
    else:
        await event.edit("No User is Defined\n are u dumb\n reply to a user.")
