#credits @leoatomic
import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, bot, versions
from userbot.system import dev_cmd
import time
from . import StartTime, get_readable_time

from datetime import datetime


@bot.on(dev_cmd(pattern="alive", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await event.edit(f"ㅤ  [✅](tg://user?id=845549379) **Userbot Online** \n\n **《 🗃 Database:** `Working` \n **《 🪐 AtomicUserbot Version:** `1.0` \n **《 🐍 Python Version:** `3.9.2`\n **《 📚 Telethon Version:** `1.21.1` \n **《 📶 Ping:** `Calcolo...` \n**《 📶 Attivo da:** `{uptime}`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"ㅤ  [✅](tg://user?id=845549379) **Userbot Online** \n\n **《 🗃 Database:** `Working` \n **《 🪐 AtomicUserbot Version:** `1.0` \n **《 🐍 Python Version:** `3.9.2`\n **《 📚 Telethon Version:** `1.21.1` \n **《 📶 Ping:** `{ms}`  \n**《 📶 Attivo da:** `{uptime}`")

@bot.on(dev_cmd(pattern=f"on", outgoing=True))
async def amireallyalive(on):
    """ For .alive command, check if the bot is running. """
    await on.edit("**Online** [✔️](tg://user?id=845549379)")
