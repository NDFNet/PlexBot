from nextcord.ext import commands
from PlexBot.userchecks import UserChecks
from PlexBot.plex import plex
from plexapi.audio import Track
from PlexBot.logging import log
import nextcord

class Media(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(brief="Plays the requested song")
    async def play(self, ctx: commands.Context, *, arg):
        await UserChecks.do_blacklist_check(ctx)
        await UserChecks.do_vc_check(ctx)
        await UserChecks.do_bot_in_vc_check(ctx)
        await UserChecks.do_same_vc_check(ctx)
                
        tracks = plex.search(arg, mediatype='track', limit=10)
        try: track: Track = tracks[0]
        except IndexError: await ctx.reply(f"No results for \"{arg}\""); return
        log.info(f"{ctx.author.name} queued \"{track.title}\"")
        await ctx.reply(f"Now Playing: {track.title}")
        try: vc = await ctx.author.voice.channel.connect()
        except nextcord.ClientException: pass
        vc.play(nextcord.FFmpegOpusAudio(track.getStreamURL()))
        
def setup(bot):
    bot.add_cog(Media(bot))
