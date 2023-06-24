import disnake
from disnake.ext import commands

import config as cfg

# event logging

class Logging(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
        
    @commands.Cog.listener()
    async def on_slash_command(self, inter: disnake.AppCmdInter):
        
        if inter.command_failed:
            return
        
        author = inter.author.mention
        command = inter.data.name
        
        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=f"Command Executed",
            description=f"{author} executed **{command}**."
        )
        
        embed.set_author(name=inter.author, icon_url=inter.author.display_avatar)
        
        logs_channel = self.bot.get_channel(cfg.LOGS_CHANNEL)
        await logs_channel.send(embed=embed)
    
        
    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: disnake.AppCmdInter, error: commands.CommandError):
        
        author = inter.author.mention
        command = inter.data.name
        
        embed = disnake.Embed(
            color=cfg.ERROR,
            title=f"Command Failed",
            description=f"{author} failed to execute **{command}**.\n Error: {error}"
        )
        
        embed.set_author(name=inter.author, icon_url=inter.author.display_avatar)
        
        logs_channel = self.bot.get_channel(cfg.LOGS_CHANNEL)
        await logs_channel.send(embed=embed)
        
        
def setup(bot: commands.Bot):
    bot.add_cog(Logging(bot))
    print(f"{__name__} is ready.")
