import sys
from pyrogram import Client
from config import Config

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="FileStoreBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins={"root": "plugins"}
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"@{me.username} Started Successfully!")

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped. Bye!")

if __name__ == "__main__":
    Bot().run()
