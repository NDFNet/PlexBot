import json
import pathlib
import random

import nextcord
from nextcord.ext import commands
from plexapi.audio import Track
from plexapi.server import PlexServer
from pysimplelog import Logger

# init shit
VERSION = "DEV-0.1.0"

# logging shit
log = Logger("PlexBot")
log.set_log_file_basename("logs/plexbot")
log.info(f"Starting PlexBot {VERSION}")

config = json.loads(pathlib.Path("config.json").read_text())
plex: PlexServer = PlexServer(config["plex_baseurl"], config['plex_token'])
log.info(f"Logged into Plex as {plex.myPlexUsername}")
intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=config["prefix"], intents=intents, owner_ids=config["owner_ids"], description='A basic music bot to play music from Plex servers.')

@bot.event
async def on_ready():
    log.info(f"Logged into Discord as {bot.user}")

# classes
class PlexBotEmoji:
    def norton_think():
        return bot.get_emoji(880601441985765426)
    def norton():
        return bot.get_emoji(962200850942550106)
    def billgates():
        return bot.get_emoji(844399371742609438)
    def nortonn():
        return bot.get_emoji(858742806989504543)

class random_footer:
    def __init__(self):
        num = random.randint(0, 10)
        match num:
            case 0:
                self.text = "An agpwat moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/873056708728082442.png"
            case 1:
                self.text = "A norton moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/962200850942550106.png"
            case 2:
                self.text = "A sadkek moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/882088202326904832.png"
            case 3:
                self.text = "A raffi moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/859185490234179615.png"
            case 4:
                self.text = "A mild_dissatisfaction moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/925227914566463498.png"
            case 5:
                self.text = "A klaus moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/825880863862423552.png"
            case 6:
                self.text = "A shitcord moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/835620319540674570.png"
            case 7:
                self.text = "A billgates moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/844399371742609438.png"
            case 8:
                self.text = "A magikkek moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/881959153977942017.gif"
            case 9:
                self.text = "A kek moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/859461499247919104.png"
            case 10:
                self.text = "A rafficlose moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/849364281454755890.png"
            case 11:
                self.text = "A gillbates moment has occurred!"
                self.image = "https://cdn.discordapp.com/emojis/963406960651300864.png"

class UserChecks:
    async def do_vc_check(ctx: commands.Context):
        if ctx.author.voice is None:
            embed = nextcord.Embed(
                title="{} You must be in a voice channel to use that!".format(PlexBotEmoji.norton()),
                description="Please join a voice channel to use this command!", 
                color=nextcord.Color.red()
            )
            if ctx.voice_client:
                embed.description = "Please join the voice channel " + ctx.voice_client.channel.mention + " to use this command!"
                embed.color = nextcord.Color.yellow()
            footer = random_footer()
            embed.set_footer(text=footer.text, icon_url=footer.image)
            await ctx.reply(embed=embed)
            raise Exception("user not in vc")

    async def do_same_vc_check(ctx: commands.Context):
        if ctx.voice_client.channel != ctx.author.voice.channel:
            embed=nextcord.Embed(
                title="{} You aren't in the same VC as me!".format(PlexBotEmoji.norton_think()),
                description="I am currently in the vc " + ctx.voice_client.channel.mention + ". Please join this vc to use this command!",
                color=nextcord.Color.red()
            )
            footer = random_footer()
            embed.set_footer(text=footer.text, icon_url=footer.image)
            await ctx.reply(embed=embed)
            raise Exception("user not in same vc")

    async def do_blacklist_check(ctx: commands.Context):
        if ctx.author.id in config["blacklist"]:
            embed=nextcord.Embed(
                title="{} You are on the blacklist!".format(PlexBotEmoji.nortonn()),
                description="You are on the blacklist! Please contact a moderator to be removed from the blacklist!",
                color=nextcord.Color.red()
            )
            footer = random_footer()
            embed.set_footer(text=footer.text, icon_url=footer.image)
            await ctx.reply(embed=embed)
            raise Exception("user on blacklist")
        
    async def do_bot_in_vc_check(ctx: commands.Context):
        global vc
        if ctx.voice_client is None:
            embed=nextcord.Embed(
                title="{} I am not in a voice channel!".format(PlexBotEmoji.norton_think()),
                description="Joining the channel" + ctx.author.voice.channel.mention + " now",
                color=nextcord.Color.yellow()
            )
            footer = random_footer()
            embed.set_footer(text=footer.text, icon_url=footer.image)
            msg = await ctx.reply(embed=embed)
            vc = await ctx.author.voice.channel.connect()
            embed.title="{} I am now in the voice channel:".format(PlexBotEmoji.billgates())
            embed.description=ctx.author.voice.channel.mention
            embed.color=nextcord.Color.green()
            await msg.edit(embed=embed)


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(brief="Gets the bot's latency to the discord gateway or something", usage="")
    async def ping(self, ctx: commands.Context):
        embed = nextcord.Embed(
            title="🏓 Pong!",
            description=f"{ctx.bot.latency * 1000:.2f} ms\n",
            color=nextcord.Color.green()
        )
        footer = random_footer()
        embed.set_footer(text=footer.text, icon_url=footer.image)
        await ctx.reply(embed=embed)
    @commands.command()
    async def about(self, ctx: commands.Context):
        embed = nextcord.Embed(
            title="{} About PlexBot".format(PlexBotEmoji.norton_think()),
            description="A basic music bot to play music from " + bot.get_user(584532167002947604).mention + " and " + bot.get_user(437970062922612737).mention + "'s Plex servers.",
            color=nextcord.Color.green(),
            url="http://ndfnet.com/plexbot"
        )
        embed.add_field(name="Authors:", value=bot.get_user(702311240407449710).mention+", "+bot.get_user(437970062922612737).mention)
        embed.add_field(name="Version:", value=VERSION)
        embed.add_field(name="Latency:", value=f"{ctx.bot.latency * 1000:.2f} ms")

        embed.set_thumbnail(url=bot.user.avatar.url)
        await ctx.reply(embed=embed)
    @commands.command()
    async def restart(self, ctx: commands.Context):
        if await bot.is_owner(ctx.author) or ctx.author.guild_permissions.kick_members:
            return
        else:
            embed = nextcord.Embed(
                title="{} An Error has occurred!".format(PlexBotEmoji.norton_think()),
                description="You do not have permission to use this command.\n",
                color=nextcord.Color.red()
            )
            footer = random_footer()
            embed.set_footer(text=footer.text, icon_url=footer.image)
            await ctx.reply(embed=embed)

class Media(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Plays the requested song idk", usage="[title]")
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
        print(track.getStreamURL())
        vc.play(nextcord.FFmpegOpusAudio(track.getStreamURL()))



bot.add_cog(Main(bot)); log.info('Registered cog "Main"')
bot.add_cog(Media(bot)); log.info('Registered cog "Media"')
# bot.add_cog(Queueing(bot)); log.info('Registered cog "Queueing"')
# bot.add_cog(Controls(bot)); log.info('Registered cog "Controls"')


bot.run(config["discord_token"])