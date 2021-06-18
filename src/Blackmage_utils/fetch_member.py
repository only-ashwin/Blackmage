import discord
from discord.ext import commands
import re

from discord.guild import Guild

async def fetch_member(ctx:commands.Context, user:str) -> discord.Member:
    userid = None
    guild:Guild = ctx.guild
    if re.match("<@.?[0-9]*?>", user):
        userid = ''.join([str(elem) for elem in re.findall("[0-9]", user)])
    else:
        userid = user
    return await guild.fetch_member(int(userid))
# ban @Octopus  1 hello<@.?[0-9]*?>