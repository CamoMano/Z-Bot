"""
Python Discord Bot(Z-Bot)
Developer: CamoMano
This is a simple Discord bot written in Python 3.7
"""


import discord
import asyncio
import feedparser
from discord.ext import commands
from discord.ext.commands import Bot

# Sets the command prefix
bot = commands.Bot(command_prefix='~')
# Removes the default help command in favor of a custom one
bot.remove_command('help')

# Shows that the bot has logged in
@bot.event
async def on_ready():
    print("--------------------")
    print("Successfully logged in as")
    print(bot.user)
    print("--------------------")


# Stops the bot from replying to itself
async def on_message(self, message):
    if message.author == self.user:
        return


@bot.command()
async def info(ctx):
    await ctx.send('```Developer: CamoMano```')


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

""" 
# Blank command example with explanations
@bot.command()
# Change 'command' to whatever you want to command to be
async def command(ctx):
# Input what the bot should respond with
    await ctx.send('Put response here')
"""

bot.run('yourkeyhere')
