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
            prefix="+ TriHard ",
            initial_channels=["pajlada", "mmattbtw"],
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return

        elif (
            message.author.name in ["pajbot", "mmattbot"]
            and message.content == "pajaS 🚨 ALERT"
        ):
            response = httpx.post(
                "https://pajlada.pajbot.com/api/v1/banphrases/test",
                json={"message": "BatChest 🚨 BAAAAT"},
            )

            print(response.json())
            if response.json()["banned"] == False:
                await message.channel.send(".me BatChest 🚨 BAAAAT")
            else:
                print("Banphrased monkaOMEGA")
        
        print(message.content)

        await self.handle_commands(message)

    @commands.command(name="dank")
    async def dank(self, ctx, *, text: str):
        if ctx.author.name == "mmattbtw":
            response = httpx.post(
                "https://pajlada.pajbot.com/api/v1/banphrases/test",
                json={"message": text},
            )
            print(response.json())
            if response.json()["banned"] == False:
                await ctx.send(text)
            else:
                await ctx.send("monkaGIGA Banphrased")


bot = Bot()
bot.run()
