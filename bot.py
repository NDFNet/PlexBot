import nextcord
from nextcord.ext import commands

from PlexBot.config import discord_prefix, discord_token, VERSION, blacklist, discord_owners
from PlexBot.logging import log

log.info(f"Starting PlexBot {VERSION}")

# Intents and bot
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=discord_prefix, intents=intents, owner_ids=discord_owners)
bot.load_extension("cogs.main")
bot.load_extension("cogs.media")
bot.load_extension("cogs.owner")

@bot.event
async def on_ready():
    log.info(f"Logged into Discord as {bot.user}")
    
@bot.check
async def blacklist_check(ctx):
    if ctx.author.id in blacklist:
        log.error(f"User {ctx.author} is on blacklist")
        return False
    else:
        return True

@bot.event
async def on_command_error(ctx: commands.Context, error):
  if isinstance(error, commands.CheckFailure):
      log.error(f"User check for {ctx.author} failed: {error}")

# Start the bot
bot.run(discord_token)
