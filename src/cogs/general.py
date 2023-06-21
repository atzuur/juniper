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
        Get a users avatar

        Parameters
        ----------
        user: Mention a user or enter their ID
        """

        embed = disnake.Embed(
            color=cfg.SUCCESS,
            title=f"{user.name.capitalize()}'s Avatar"
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

        embed.set_author(name=user.name.capitalize(), icon_url=user.display_avatar)
        embed.set_thumbnail(user.display_avatar)

        embed.add_field(
            name="ID",
            value=user.id,
            inline=False
        )

        creation_date = f"<t:{int(user.created_at.timestamp())}:R>"

        embed.add_field(
            name="Created",
            value=creation_date,
            inline=False
        )

        if isinstance(user, disnake.Member):
            join_date = f"<t:{int(user.joined_at.timestamp())}:R>"

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
            
            if len(roles) > 0:
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
        
        outcome = random.randint(1, size)
        msg = f"{inter.author.name} rolled a d{size} and got **{outcome}**".capitalize()

        if amount > 1:
            outcomes = []
            for i in range(amount):
                outcomes.append(random.randint(1, size))
                i += 1

            outcomes = ", ".join(str(outcome) for outcome in outcomes)
            msg = f"{inter.author.name} rolled {amount} d{size}'s and got **{outcomes}**".capitalize()

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

        if len(msg.stickers) == 0:
            raise commands.BadArgument("Sorry, that message doesn't contain a sticker")

        sticker = msg.stickers[0] # sticker id, so we can get info from it

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
