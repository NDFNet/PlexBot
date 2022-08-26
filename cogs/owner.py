import json
import nextcord
from nextcord.ext import commands
from PlexBot import config
from PlexBot.logging import log

class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        
    async def cog_check(self, ctx):
        if not await self.bot.is_owner(ctx.author): return False
        else: return True
        
    @commands.command(brief="Shuts down the bot", alias=["die", "ceasetobe"], )
    async def kill(self, ctx: commands.Context):
        #if not bot.is_owner(ctx.author): return
        log.info("Shutdown triggered by command")
        await ctx.send("**Shutting down...**")
        await self.bot.close()
            
    @commands.command(brief="Blacklists the specified user", usage="[user]")
    async def blacklist(self, ctx: commands.Context, user: nextcord.User = None):
        if user:
            user_id = 0
            try:
                user_id = user.id
            except commands.UserNotFound:
                await ctx.send("User not found")
                return
            if ctx.author.id == user_id:
                await ctx.send("You can't blacklist yourself!")
                return
            with open("config.json",'r') as jsonfile:
                json_content = json.load(jsonfile)

            if user_id in json_content["discord"]["blacklist"]:
                json_content["discord"]["blacklist"].remove(user_id)
                config.blacklist.remove(user_id)
                await ctx.reply(f"Unblacklisted {user}")
            else:
                json_content["discord"]["blacklist"].append(user_id)
                config.blacklist.append(user_id)
                await ctx.reply(f"Blacklisted {user}")

            with open("config.json",'w') as jsonfile:
                json.dump(json_content, jsonfile, indent=4)
        else: # If no user specified, show blacklist
            if len(config.blacklist) == 0:
                await ctx.send("Blacklist is empty!")
                return
            blacklist = "```\n"
            for user_id in config.blacklist:
                currentuser = await self.bot.fetch_user(user_id)
                blacklist += f"{currentuser.name}\n"
            blacklist += "```"
            await ctx.send(blacklist)
            
        
def setup(bot):
    bot.add_cog(Owner(bot))