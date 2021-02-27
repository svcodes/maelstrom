from discord.ext import commands
from discord import Intents, Message
from typing import Optional
from traceback import print_exc

from aiohttp import ClientSession


class Bot(commands.Bot):
    """A subclass of `commands.Bot` with additional features."""

    def __init__(self, *args, **kwargs):
        intents = Intents.default()
        intents.members = True

        super().__init__(
            command_prefix=self.get_prefix,
            intents=intents,
            *args,
            **kwargs,
        )

        self.session: Optional[ClientSession] = None

    def load_cogs(self, *exts) -> None:
        """Load a set of extensions."""

        for ext in exts:
            try:
                self.load_extension(ext)
            except Exception as e:
                print_exc()

    async def login(self, *args, **kwargs) -> None:
        """Create the ClientSession before logging in."""

        self.session = ClientSession()

        await super().login(*args, **kwargs)

    async def get_prefix(self, message: Message) -> str:
        """Get a dynamic prefix for the bot."""

        return "!"