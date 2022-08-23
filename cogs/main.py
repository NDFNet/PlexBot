from nextcord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="Gets the latency to Discords API")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f":ping_pong: Pong! **{ctx.bot.latency * 1000:.2f}ms**")
        
def setup(bot):
    bot.add_cog(Main(bot))
