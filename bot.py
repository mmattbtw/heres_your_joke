import os

import dotenv
from twitchio.ext import commands

dotenv.load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(
            token=os.environ.get("TOKEN"),
            prefix="+ TriHard ",
            initial_channels=["elpws", "mmattbtw"],
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return
        elif "wiggle beep" in message.content.lower():
            await message.channel.send(".me WIGGLE BOOP")
        elif "wiggle boop" in message.content.lower():
            await message.channel.send(".me WIGGLE BEEP")

        print(message.content)
        await self.handle_commands(message)


bot = Bot()
bot.run()
