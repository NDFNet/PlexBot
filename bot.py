import nextcord
from nextcord.ext import commands
from plexapi.audio import Track
from plexapi.server import PlexServer

from PlexBot.config import discord_prefix, discord_token, config
from PlexBot.logging import log
# Init
VERSION = "DEV-0.1.0"

log.info(f"Starting PlexBot {VERSION}")

# Intents and bot
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=discord_prefix, intents=intents)
bot.load_extension("cogs.main")

@bot.event
async def on_ready():
    log.info(f"Logged into Discord as {bot.user}")
    

# Start the bot
bot.run(discord_token)