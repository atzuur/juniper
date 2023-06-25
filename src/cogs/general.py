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
    async def avatar(self, inter: disnake.AppCmdInter):
        pass
    

    @avatar.sub_command()
    async def user(inter: disnake.AppCmdInter, user: disnake.User = None):
        
        """
        Get a user's avatar

        Parameters
        ----------
        user: Mention a user or enter their ID
        """
        
        if user is None:
            user = inter.author
        
        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=f"{user.mention}'s avatar"
        )
        
        embed.set_image(user.avatar or user.default_avatar)
        await inter.send(embed=embed)


    @avatar.sub_command()
    async def server(inter: disnake.AppCmdInter, member: disnake.Member = None):
        
        """
        Get a user's server avatar

        Parameters
        ----------
        user: Mention a user or enter their ID
        """
        
        if member is None:
            member = inter.author
            
        if not isinstance(member, disnake.Member):
            raise commands.MemberNotFound(member)
    
        if not member.guild_avatar:
            raise commands.BadArgument(f"{member.mention} doesn't have a server avatar set.")
        
        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=f"{member.mention}'s guild avatar"
        )
        
        embed.set_image(member.guild_avatar)
        await inter.send(embed=embed)


    @avatar.error
    async def avatar_error(self, inter: disnake.AppCmdInter, error):
        if isinstance(error, commands.BadArgument or commands.MemberNotFound):

            embed = disnake.Embed(
                color=cfg.ERROR,
                title="Error",
                description=error
            )

            await inter.send(embed=embed, ephemeral=True)


    @commands.slash_command()
    async def whois(inter: disnake.AppCmdInter, user: disnake.Member | disnake.User):
        
        """
        Get info about a user

        Parameters
        ----------
        user: Mention a user or enter their ID
        """

        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=user.mention
        )
        
        embed.set_author(name=user, icon_url=user.display_avatar)
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
    print(f"{__name__} is ready")
