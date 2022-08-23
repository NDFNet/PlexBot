import nextcord
from nextcord.ext import commands

from PlexBot.config import discord_prefix, discord_token, VERSION
from PlexBot.logging import log

log.info(f"Starting PlexBot {VERSION}")

# Intents and bot
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=discord_prefix, intents=intents)
bot.load_extension("cogs.main")
bot.load_extension("cogs.media")
bot.load_extension("cogs.owner")

@bot.event
async def on_ready():
    log.info(f"Logged into Discord as {bot.user}")
    

# Start the bot
bot.run(discord_token)
