import asyncio
import os
from aiohttp import web

from bot import Bot
from plugins.web_server import web_server

import pyrogram.utils
pyrogram.utils.MIN_CHANNEL_ID = -1009147483647


async def main():
    # 1️⃣ Serveur web AdsGram
    app = await web_server()
    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    print(f"🌐 Web server actif sur le port {port}")

    # 2️⃣ Bot Telegram
    bot = Bot()
    await bot.start()

    print("🤖 Bot Telegram démarré")

    # 3️⃣ Ne jamais quitter
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())