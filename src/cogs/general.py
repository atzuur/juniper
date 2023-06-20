import disnake
from disnake.ext import commands

from config import SUCCESS


class GeneralCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.AppCmdInter):
        """Get the bot's current websocket latency"""
        await inter.send(f"Pong! {round(self.bot.latency * 1000)}ms")


    @commands.slash_command()
    async def avatar(inter: disnake.AppCmdInter, user: disnake.User):
        """Get a users avatar"""

        embed = disnake.Embed(
            color=SUCCESS,
            title=f"{user.mention}'s avatar"
        )

        embed.set_image(user.display_avatar)
        await inter.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(GeneralCommands(bot))
