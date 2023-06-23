import disnake
from disnake.ext import commands

import config as cfg

# event logging

class Logging(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
        
    @commands.Cog.listener()
    async def on_slash_command(self, inter: disnake.AppCmdInter):
        
        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=f"Executed Command: {inter.data.name}",
        )
        
        embed.set_author(name=inter.author, icon_url=inter.author.display_avatar)
        
        logs_channel = self.bot.get_channel(cfg.LOGS_CHANNEL)
        await logs_channel.send(embed=embed)
        
        
def setup(bot: commands.Bot):
    bot.add_cog(Logging(bot))
