

import asyncio

from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl 

# Define ban rights (example: ban from sending messages and media)
RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sb(?: |$)(.*)" % hl))
async def banall(event):
    if event.sender_id in SUDO_USERS:
        if not event.is_group:
            Reply = "Noob !! Use This Cmd in Group."
            await event.reply(Reply)
        else:
            admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
            admins_id = [i.id for i in admins]
            all_users = 0
            banned_users = 0
            async for user in event.client.iter_participants(event.chat_id):
                all_users += 1
                try:
                    if user.id not in admins_id:
                        await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                        banned_users += 1
                        await asyncio.sleep(0.1)
                except Exception as e:
                    print(str(e))
                    await asyncio.sleep(0.1)
            await event.reply(f"Banned {banned_users} out of {all_users} members.")