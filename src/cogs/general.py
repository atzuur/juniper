import disnake
from disnake.ext import commands

import config as cfg

# general purpose commands

class General(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.AppCmdInter):
        
        """Get the bot's current websocket latency"""
        await inter.send(f"Pong! {round(self.bot.latency * 1000)}ms")


    @commands.slash_command()
    async def avatar(inter: disnake.AppCmdInter, user: disnake.User):
        
        """
        Get a user's avatar

        Parameters
        ----------
        user: Mention a user or enter their ID
        """

        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=f"Avatar for {user}"
        )

        embed.set_image(user.display_avatar)
        await inter.send(embed=embed)


    @commands.slash_command()
    async def whois(inter: disnake.AppCmdInter, user: disnake.Member | disnake.User):
        
        """
        Get info about a user

        Parameters
        ----------
        user: Mention a user or enter their ID
        """

        embed = disnake.Embed(color=cfg.SUCCESS)
        
        embed.set_author(name=f"{user}", icon_url=user.display_avatar)
        embed.set_thumbnail(user.display_avatar)

        embed.add_field(
            name="ID",
            value=user.id,
            inline=False
        )
        
        embed.add_field(
            name="Created",
            value=disnake.utils.format_dt(user.created_at, "R"),
            inline=False
        )

        if isinstance(user, disnake.Member):
            
            embed.add_field(
                name="Joined",
                value=disnake.utils.format_dt(user.joined_at, "R"),
                inline=False
            )
            
            embed.add_field(
                name="Status",
                value=user.status.name.capitalize(),
                inline=False
            )

            roles = user.roles[1:] # exclude @everyone
            
            if roles:
                embed.add_field(
                    name=f"Roles [{len(roles)}]",
                    value=", ".join(role.mention for role in roles),
                    inline=False
                )
  
        await inter.send(embed=embed)  


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
