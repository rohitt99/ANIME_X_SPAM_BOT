#  Copyright (c) 2022 @TheoxybotoeL - oxybotoeL
# Telegram Ban All Bot 
# Creator - oxybotoeL

import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var
from time import sleep
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl import functions
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)

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


logging.basicConfig(level=logging.INFO)

print("Starting.....")

#oxybot = TelegramClient('oxybot', Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)


SUDO_USERS = []
for x in Var.SUDO: 
    SUDO_USERS.append(x)

@oxybot.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**Feel The TN Power ⚡** \n\n 𝙼𝚢 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 @ITACHI_TNs! `{ms}` ms")


@oxybot.on(events.NewMessage(pattern="^/kickall"))
async def kickall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"Noob !! Use This Cmd in Group."
         await event.reply(Reply)
     else:
         await event.delete()
         oxybot = await event.get_chat()
         oxybotoeLop = await event.client.get_me()
         admin = oxybot.admin_rights
         creator = oxybot.creator
         if not admin and not creator:
              return await event.reply("𝙸 𝚍𝚘𝚗'𝚝 𝙷𝚊𝚟𝚎 𝚜𝚞𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝 𝚁𝚒𝚐𝚑𝚝𝚜!!")
         oxybotoeL = await oxybot.send_message(event.chat_id, "**Feel The TN Power ⚡**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         kimk = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
                if user.id not in admins_id:
                    await event.client.kick_participant(event.chat_id, user.id)
                    kimk += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                    print(str(e))
                    await asyncio.sleep(0.1)
         await oxybotoeL.edit(f"**𝚄𝚜𝚎𝚛𝚜 𝙺𝚒𝚌𝚔𝚎𝚍 𝚂𝚞𝚌𝚌𝚎𝚜𝚏𝚞𝚕𝚕𝚢⚡! \n\n 𝙺𝚒𝚌𝚔𝚎𝚍:** `{kimk}` \n **𝚃𝚘𝚝𝚊𝚕:** `{all}`")
    

@oxybot.on(events.NewMessage(pattern="^/b"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"Noob !! Use This Cmd in Group."
         await event.reply(Reply)
     else:
         await event.delete()
         oxybot = await event.get_chat()
         oxybotoeLop = await event.client.get_me()
         admin = oxybot.admin_rights
         creator = oxybot.creator
         if not admin and not creator:
              return await event.reply("𝙸 𝚍𝚘𝚗'𝚝 𝙷𝚊𝚟𝚎 𝚜𝚞𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝 𝚁𝚒𝚐𝚑𝚝𝚜!!")
         oxybotoeL = await oxybot.send_message(event.chat_id, "**Feel The TN Power ⚡**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         bann = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
               if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                   print(str(e))
                   await asyncio.sleep(0.1)

    
@oxybot.on(events.NewMessage(pattern="^/unbanall"))
async def unban(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"Noob !! Use This Cmd in Group."
         await event.reply(Reply)
     else:
         msg = await event.reply("Searching Participant Lists.")
         p = 0
         async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
              rights = ChatBannedRights(until_date=0, view_messages=False)
              try:
                await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
              except FloodWaitError as ex:
                 print(f"sleeping for {ex.seconds} seconds")
                 sleep(ex.seconds)
              except Exception as ex:
                 await msg.edit(str(ex))
              else:
                  p += 1
         await msg.edit("{}: {} unbanned".format(event.chat_id, p))


@oxybot.on(events.NewMessage(pattern="^/leave"))
async def _(e):
    if e.sender_id in SUDO_USERS:
        oxybotoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = oxybotoel[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝙻𝚎𝚊𝚟𝚎𝚍 𝙵𝚛𝚘𝚖 𝚃𝚑𝚎 𝙲𝚑𝚊𝚝𝚜 𝙵𝚒𝚕𝚕𝚎𝚍 𝚆𝚒𝚝𝚑 𝙽𝚒𝚐𝚐𝚎𝚛𝚜")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝙻𝚎𝚊𝚟𝚎𝚍 𝙵𝚛𝚘𝚖 𝚃𝚑𝚎 𝙲𝚑𝚊𝚝𝚜 𝙵𝚒𝚕𝚕𝚎𝚍 𝚆𝚒𝚝𝚑 𝙽𝚒𝚐𝚐𝚎𝚛𝚜")
            except Exception as e:
                await event.edit(str(e))   
          

@oxybot.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "__Restarting__ !!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await oxybot.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


print("\n\n")
print("TN 𝙱𝚊𝚗𝚊𝚕𝚕 𝙱𝚘𝚝 𝙳𝚎𝚙𝚕𝚘𝚢𝚎𝚍 𝚂𝚞𝚌𝚌𝚎𝚜𝚏𝚞𝚕𝚕𝚢⚡")

#oxybot.run_until_disconnected()
