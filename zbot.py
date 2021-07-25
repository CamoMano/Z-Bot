"""
Python Discord Bot(Z-Bot)
Developer: CamoMano
This is a simple Discord bot written in Python 3.7
"""

import feedparser
import discord
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext

# Sets the command prefix
client = Client(intents=Intents.default())
slash = SlashCommand(client)

# Opens key.txt where the bot key is stored
keyfile = open("key.txt", "r")

# Reads the file and sets the key
key = keyfile.read()

# Closes the file
keyfile.close()


# Shows that the bot has logged in
@client.event
async def on_ready():
    print("--------------------")
    print("Successfully logged in as")
    print(client.user.name)
    print(client.user.id)
    print("--------------------")
    await client.change_presence(activity=discord.Game(name='https://z.ridgelinestds.com/ | /help'))


@slash.slash(name="info")
async def info(ctx: SlashContext):
    await ctx.send('```Developer: CamoMano```')


@slash.slash(name="site")
async def site(ctx: SlashContext):
    await ctx.send('https://z.ridgelinestds.com')


@slash.slash(name="buy")
async def buy(ctx: SlashContext):
    await ctx.send('https://store.steampowered.com/app/786770/Z_The_End/')


@slash.slash(name="contact")
async def contact(ctx: SlashContext):
    await ctx.send('contact@ridgelinestds.com')


@slash.slash(name="help")
async def help(ctx: SlashContext):
    await ctx.send(
        '''```
        ~help       Shows this message
        
        ~info       Gives information about the bot
        
        ~site       Links to the website
        
        ~buy        Links to the Steam page
        
        ~contact    Gives contact information
        
        ~devblog    Links to the latest devblog
        ```''')


@slash.slash(name="devblog")
async def devblog(ctx: SlashContext):
    site_rss = "http://z.ridgelinestds.com/feed"
    feed = feedparser.parse(site_rss)
    request = feed.entries[0]['link']
    await ctx.send(request)


""" 
# Blank command example with explanations
@client.command()

# Change 'command' to whatever you want to command to be
async def command(ctx):

# Input what the bot should respond with
    await ctx.send('Put response here')
    await ctx.message.delete()
"""

client.run(key)
