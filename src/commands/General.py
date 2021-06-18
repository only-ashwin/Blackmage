from discord.errors import Forbidden
from Blackmage_utils.fetch_member import fetch_member
from discord.ext import commands
import discord
import math


class General(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f":ping_pong: Pong { math.floor(self.bot.latency * 1000) }ms")

    @commands.command(name="ban")
    @commands.has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def ban(self, ctx: commands.Context, user: str, delete_message_days: int = 1, reason: str = None):
        fetched_user: discord.Member = await fetch_member(ctx, user)
        try:
            # This is for checking if the fetched user is a moderator or owner
            await fetched_user.ban(reason=reason, delete_message_days=delete_message_days)
        except Forbidden:
            await ctx.send("You can't ban a moderator")
            return
        await ctx.send(f"banned {fetched_user}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to ban a member")
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("Invalid Use of the command: Ban")
        else:
            raise error

    @commands.command(name="kick")
    @commands.has_permissions(administrator=True, manage_messages=True, manage_roles=True)
    async def kick(self, ctx: commands.Context, user: str, reason: str = None):
        fetched_user: discord.Member = await fetch_member(ctx, user)
        try:
            # This is for checking if the fetched user is a moderator or owner
            await fetched_user.kick(reason=reason)
        except Forbidden:
            await ctx.send("You can't kick a moderator")
            return
        await ctx.send(f"kicked {fetched_user}")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to kick a member")
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("Invalid Use of the command: Ban")
        else:
            raise error


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
