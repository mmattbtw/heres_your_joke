from twitchio.ext import commands

import dotenv
import os

import httpx

dotenv.load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(
            token=os.environ.get("TOKEN"),
            prefix="??????? TriHard",
            initial_channels=["pajlada"],
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return

        elif message.author.name == "pajbot" and message.content == "pajaS 🚨 ALERT":
            response = httpx.post(
                "https://pajlada.pajbot.com/api/v1/banphrases/test",
                json={"message": "BatChest 🚨 BAAAAT"},
            )

            if response.json()["banned"] == False:
                await message.channel.send("BatChest 🚨 BAAAAT")
            else:
                print("Banphrased monkaOMEGA")


bot = Bot()
bot.run()
