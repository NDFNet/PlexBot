from ast import alias
import sys
from nextcord.ext import commands
from PlexBot import config

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="Shuts down the bot", alias=["die", "ceasetobe"])
    async def kill(self, ctx: commands.Context):
        if ctx.author.id in config.discord_owners:
            await ctx.send("**Shutting down...**")
            sys.exit(0)
        
def setup(bot):
    bot.add_cog(Owner(bot))