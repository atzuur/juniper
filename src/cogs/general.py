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
        """
        Get a users avatar

        Parameters
        ----------
        user: Mention a user or enter their ID
        """

        embed = disnake.Embed(
            color=SUCCESS,
            title=f"{user.mention}'s avatar"
        )

        embed.set_image(user.display_avatar)
        await inter.send(embed=embed)


    @commands.slash_command()
    async def member_info(inter: disnake.AppCmdInter, member: disnake.Member):
        """
        Get info about a member

        Parameters
        ----------
        member: Mention a member or enter their ID
        """

        embed = disnake.Embed(color=SUCCESS)

        embed.set_author(name=member, icon_url=member.display_avatar)
        embed.set_thumbnail(member.display_avatar)

        embed.add_field(
            name="ID",
            value=member.id,
            inline=False
        )

        creation_date = f"<t:{int(member.created_at.timestamp())}:R>"
        embed.add_field(
            name="Created",
            value=creation_date,
            inline=False
        )

        join_date = f"<t:{int(member.joined_at.timestamp())}:R>"
        embed.add_field(
            name="Joined",
            value=join_date,
            inline=False
        )

        embed.add_field(
            name="Status",
            value=member.status.name.capitalize(),
            inline=False
        )

        roles = member.roles[1:] # exclude @everyone
        
        if len(roles) > 0:
            embed.add_field(
                name=f"Roles [{len(roles)}]",
                value=", ".join(role.mention for role in roles),
                inline=False
            )

        
        await inter.send(embed=embed)  

    @member_info.error
    async def info_error(inter: disnake.AppCmdInter, error):
        if isinstance(error, commands.BadArgument):
            await inter.send("Sprry, couldn't find that member", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(GeneralCommands(bot))
