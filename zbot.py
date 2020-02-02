import discord
import asyncio
import feedparser
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='~')
bot.remove_command('help')


@bot.event
async def on_ready():
    print("--------------------")
    print("Successfully logged in as")
    print(bot.user)
    print("--------------------")


async def on_message(self, message):
    # Stops the bot from replying to itself
    if message.author == self.user:
        return


@bot.command()
async def info(ctx):
    await ctx.send('```Author: CamoMano```')


        await message.channel.send(msg)
@bot.command()
async def site(ctx):
    await ctx.send('https://z.ridgelinestds.com')


@bot.command()
async def buy(ctx):
    await ctx.send('https://store.steampowered.com/app/786770/Z_The_End/')


@bot.command()
async def contact(ctx):
    await ctx.send('contact@ridgelinestds.com')


@bot.command()
async def help(ctx):
    await ctx.send(
        '''```
        ~help       Shows this message
        
        ~info       Gives information about the bot
        
        ~site       Links to the website
        
        ~buy        Links to the Steam page
        
        ~contact    Gives contact information
        
        ~devblog    Links to the latest devblog
        ```''')


@bot.command()
async def devblog(ctx):
    site_rss = "http://z.ridgelinestds.com/feed"
    feed = feedparser.parse(site_rss)
    request = feed.entries[0]['link']
    await ctx.send(request)


bot.run('yourkeyhere')
