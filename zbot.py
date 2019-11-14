import discord
import asyncio
import feedparser


async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


client = MyClient()


@client.event
async def on_message(message):
    # Stops the bot from replying to itself
    if message.author == client.user:
        return

    if message.content.startswith('~info'):
        msg = '```Author: CamoMano```'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('~site'):
        msg = 'https://www.playzgame.net'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('~buy'):
        msg = 'https://store.steampowered.com/app/786770/Z_The_End/'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('~contact'):
        msg = 'contact@ridgelinestds.com'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('~help'):
        msg = '''```
        ~help       Shows this message
        
        ~info       Shows information about the bot
        
        ~site       Links to the website
        
        ~buy        Links to the Steam page
        
        ~contact    Gives contact information
        
        ~devblog    Links to the latest devblog
        ```'''.format(message)
        await message.channel.send(msg)

    # Gets the latest devblog from the sites RSS feed
    if message.content.startswith('~devblog'):
        site_rss = "http://z.ridgelinestds.com/feed"

        feed = feedparser.parse(site_rss)

        request = feed.entries[0]['link']
        msg = request.format(message)
        await message.channel.send(msg)


client.run('yourkeyhere')
