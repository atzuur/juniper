import disnake
from disnake.ext import commands

import config as cfg

# sudo commands for the bot owner

class Sudo(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.slash_command()
    async def shutdown(self, inter: disnake.AppCmdInter):
        """Shutdown the bot (owner only)."""

        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title="Shutting Down",
            description="Shutting down.. See you later! :wave:"
        )

        await inter.send(embed=embed)
        await self.bot.close()


    @shutdown.error
    async def shutdown_error(self, inter: disnake.AppCmdInter, error):
        if isinstance(error, commands.NotOwner):

            embed = disnake.Embed(
                color=cfg.ERROR,
                title="Error",
                description=error
            )

            await inter.send(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Sudo(bot))
    print(f"{__name__} is ready.")
