import logging

import disnake
from disnake.ext import commands

from config import TOKEN


# the recommended logging setup 
# https://docs.disnake.dev/en/stable/logging.html
logger = logging.getLogger("disnake")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="disnake.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)


bot = commands.InteractionBot(
    intents=disnake.Intents.all(),
    test_guilds=[1115670885702041640],
    activity=disnake.Game(name="With Code")
)

@bot.event
async def on_ready():
    print("The bot is online!")

bot.run(TOKEN)
