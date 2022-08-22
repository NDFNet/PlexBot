from PlexBot.config import blacklist
from PlexBot.exceptions import UserOnBlacklist, UserNotInSameVC, UserNotInVC
import nextcord
from nextcord.ext import commands

class UserChecks:
    def __init__(self):
        self.vc = vc
    async def do_vc_check(ctx: commands.Context):
        if ctx.author.voice is None:
            embed = nextcord.Embed(
                title="You must be in a voice channel to use that!",
                description="Please join a voice channel to use this command!",
                color=nextcord.Color.red()
            )
            if ctx.voice_client:
                embed.description = f"Please join the voice channel {ctx.voice_client.channel.mention} to use this commmand!"
                embed.color = nextcord.Color.yellow()
            # TODO: random footer
            await ctx.reply(embed=embed)
            raise UserNotInVC()
    
    async def do_same_vc_check(ctx: commands.Context):
        if ctx.voice_client is None: return
        if ctx.voice_client.channel != ctx.author.voice.channel:
            embed=nextcord.Embed(
                title="You aren't in the same VC as me!",
                description=f"I am currently in the VC {ctx.voice_client.channel.mention}. Please join this vc to use this command!",
                color=nextcord.Color.red()
            )
            # TODO: random footer
            await ctx.reply(embed=embed)
            raise UserNotInSameVC()
    
    async def do_blacklist_check(ctx: commands.Context):
        if ctx.author.id in blacklist:
            embed=nextcord.Embed(
                title="You are on the blacklist!",
                description="You are on the blacklist! Please contact a moderator to be removed from the blacklist!",
                color=nextcord.Color.red()
            )
            # TODO: random footer
            await ctx.reply(embed=embed)
            raise UserOnBlacklist()
        
    async def do_bot_in_vc_check(ctx: commands.Context):
        if ctx.voice_client is None:
            global vc
            embed=nextcord.Embed(
                title="I am not in a voice channel!",
                description=f"Joining the channel {ctx.author.voice.channel.mention} now",
                color=nextcord.Color.yellow()
            )
            # TODO: random footer
            #msg = await ctx.reply(embed=embed)
            #vc = await ctx.author.voice.channel.connect()
            #embed.title="I am now in the voice channel"
            #embed.description=ctx.author.voice.channel.mention
            #embed.color=nextcord.Color.green()
            #await msg.edit(embed=embed)