import asyncio
import time
from telethon import events
from userbot import bot
from userbot.system import dev_cmd
import time
from platform import python_version
from telethon import version
from . import ALIVE_NAME, StartTime, catversion, get_readable_time, mention, reply_id

@bot.on(dev_cmd(pattern="alive", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    uptime = await get_readable_time((time.time() - StartTime))
    await event.edit(f"**Userbot Online** ✅\n\n • 🗃 **Database:** `Working` \n • 🪐 **AtomicUserbot Version:** `4.3` \n • 🐍 **Python Version:** `3.9.2` \n • 📚 **Telethon Version:** `1.21.1` \n  • ⏳ **UpTime:** `{uptime}`")
