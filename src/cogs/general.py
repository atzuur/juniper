import disnake
from disnake.ext import commands

import config as cfg

# general purpose commands

class General(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.AppCmdInter):
        
        """Gets the bot's current websocket latency"""
        await inter.send(f"Pong! {round(self.bot.latency * 1000)}ms")


    @commands.slash_command()
    async def avatar(self, inter: disnake.AppCmdInter):
        pass
    

    @avatar.sub_command()
    async def user(inter: disnake.AppCmdInter, user: disnake.User | disnake.Member = None):
        
        """
        Gets a user's avatar

        Parameters
        ----------
        user: User to fetch the avatar from
        """
        
        if user is None:
            user = inter.author
        
        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=f"Avatar for {user.mention}"
        )
        
        embed.set_image(user.avatar or user.default_avatar)
        await inter.send(embed=embed)


    @avatar.sub_command()
    async def guild(inter: disnake.AppCmdInter, user: disnake.Member = None):
        
        """
        Gets a users's guild avatar (if they have one set)

        Parameters
        ----------
        user: User to fetch the avatar from
        """
        
        if user is None:
            user = inter.author
            
        if not isinstance(user, disnake.Member):
            raise commands.MemberNotFound(user)
    
        if not user.guild_avatar:
            raise commands.BadArgument(f"{user.mention} doesn't have a guild avatar set.")
        
        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=f"Guild avatar for {user.mention}"
        )
        
        embed.set_image(user.guild_avatar)
        await inter.send(embed=embed)


    @avatar.error
    async def avatar_error(self, inter: disnake.AppCmdInter, error: commands.CommandError):
        if isinstance(error, commands.BadArgument or commands.MemberNotFound):

            embed = disnake.Embed(
                color=cfg.ERROR,
                title="Error",
                description=error
            )

            await inter.send(embed=embed, ephemeral=True)


    @commands.slash_command()
    async def whois(inter: disnake.AppCmdInter, user: disnake.User | disnake.Member = None):
        
        """
        Gets info about a user

        Parameters
        ----------
        user: User to fetch info from
        """
        
        if user is None:
            user = inter.author

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
