import disnake
from disnake.ext import commands

import config as cfg

import random


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
            title=f"{user.display_name}'s Avatar"
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

        embed.set_author(name=f"{user.display_name}", icon_url=user.display_avatar)
        embed.set_thumbnail(user.display_avatar)

        embed.add_field(
            name="ID",
            value=user.id,
            inline=False
        )

        embed.add_field(
            name="Username",
            value=user,
            inline=False
        )

        creation_date = disnake.utils.format_dt(user.created_at, "R")

        embed.add_field(
            name="Created",
            value=creation_date,
            inline=False
        )

        if isinstance(user, disnake.Member):
            join_date = disnake.utils.format_dt(user.joined_at, "R")

            embed.add_field(
                name="Joined",
                value=join_date,
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


    @commands.slash_command()
    async def roll(inter: disnake.AppCmdInter, size: int, amount: int = 1):
        """
        Roll dice

        Parameters
        ----------
        size: Size of dice (limit of 100)
        amount: Amount of dice to roll (limit of 20)
        """

        if size > 100:
            raise commands.BadArgument("Dice size exceeds the limit")

        if amount > 20:
            raise commands.BadArgument("Dice amount exceeds the limit")
        
        outcome = []
        for i in range(amount):
            outcome.append(random.randint(1, size))

        outcome = ", ".join(str(i) for i in outcome)
        msg = f"{inter.author.mention} rolled {amount} d{size}'s and got **{outcome}**"

        if amount == 1:
            msg = f"{inter.author.mention} rolled a d{size} and got **{outcome}**"

        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title="Dice Roll",
            description=msg
        )

        await inter.send(embed=embed)


    @roll.error
    async def roll_error(self, inter: disnake.AppCmdInter, error):
        if isinstance(error, commands.BadArgument):

            embed = disnake.Embed(
                color=cfg.ERROR,
                title="Error",
                description=error
            )

            await inter.send(embed=embed, ephemeral=True)


    @commands.message_command(name="Steal Sticker")
    async def steal_sticker(self, inter: disnake.MessageCommandInteraction, msg: disnake.Message):
        """Steals a sticker"""

        if not msg.stickers:
            raise commands.BadArgument("Sorry, that message doesn't contain a sticker")
        
        sticker = msg.stickers[0]

        if sticker.format == disnake.StickerFormatType.lottie:
            raise commands.BadArgument("Sorry, stickers of format 'lottie' can't be stolen (this is normal for certain stickers)")

        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=f"Sticker Stolen: {sticker.name}"
        )

        embed.set_image(sticker.url)

        await inter.send(embed=embed)
        
    
    @steal_sticker.error
    async def steal_sticker_error(self, inter: disnake.MessageCommandInteraction, error):
        if isinstance(error, commands.BadArgument):

            embed = disnake.Embed(
                color=cfg.ERROR,
                title="Error",
                description=error
            )

            await inter.send(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
