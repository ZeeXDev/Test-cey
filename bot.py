# =======================
# Imports standards
# =======================
from aiohttp import web              # ❗ Utilisé pour serveur web (AdsGram)
from plugins import web_server       # ❗ Webhook AdsGram
import asyncio
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import *

name = """
 BY CODEFLIX BOTS
"""

# =======================
# Classe principale du Bot
# =======================
class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    # =======================
    # Démarrage du bot
    # =======================
    async def start(self):
        await super().start()

        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # =======================
        # Vérification DB Channel
        # =======================
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Bot must be admin in DB Channel. CHANNEL_ID={CHANNEL_ID}"
            )
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.username = usr_bot_me.username

        self.LOGGER(__name__).info("Bot Running..!")
        self.LOGGER(__name__).info("BOT DEPLOYED BY @BotZFlix")
        self.LOGGER(__name__).info("Bot Running..! Made by @ZeeXDev")

        # ============================================================
        # ❌ PROBLÈME MAJEUR ICI
        # ============================================================
        # Ce bloc démarre UN SERVEUR WEB aiohttp
        # MAIS :
        # - le même serveur est déjà démarré dans main.py
        # - le port (10000) est donc utilisé DEUX FOIS
        # - Render refuse -> OSError: address already in use
        #
        # 👉 RÈGLE :
        #    - Serveur AdsGram = 1 seule fois
        #    - Il doit vivre UNIQUEMENT dans main.py
        #
        # 👉 Solution :
        #    - Soit tu commentes ce bloc
        #    - Soit tu le laisses mais tu ne démarres PLUS rien dans main.py
        #
        # ============================================================
        app = web.AppRunner(await web_server())
        await app.setup()
        # ============================================================

        # =======================
        # Message au propriétaire
        # =======================
        try:
            await self.send_message(
                OWNER_ID,
                "<b><blockquote> Bᴏᴛ Rᴇᴅéᴍᴀʀʀᴇʀ 🥰😘</blockquote></b>"
            )
        except:
            pass

    # =======================
    # Arrêt du bot
    # =======================
    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")

    # =======================
    # Run loop
    # =======================
    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start())

        self.LOGGER(__name__).info("Bot is now running. Thanks to @Kingcey")

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            self.LOGGER(__name__).info("Shutting down...")
        finally:
            loop.run_until_complete(self.stop())