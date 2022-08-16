from PlexBot.config import discord_prefix, discord_token, config
from PlexBot.logging import logger
import PlexBot.help

import logging
import discord
from discord.ext import commands

# logging
if not config["debug"]:
    logging.getLogger("discord.gateway").setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s <%(levelname)s> %(message)s')

# Intents and Bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=discord_prefix, intents=intents)
bot.load_extension("cogs.main")
        
bot.help_command = PlexBot.help.SupremeHelpCommand()

@bot.event
async def on_ready():
    logger.info(f'Logged in as: {bot.user}')

bot.run(discord_token)