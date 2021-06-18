from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    bot.load_extension('commands.General')
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
