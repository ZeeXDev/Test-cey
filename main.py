import asyncio
from aiohttp import web
from bot import Bot
from web_server import web_server
import pyrogram.utils
import os

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

async def main():
    # Serveur AdsGram
    app = await web_server()
    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"🌐 Web server actif sur le port {port}")

    # Bot Telegram
    bot = Bot()
    await bot.start()

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())