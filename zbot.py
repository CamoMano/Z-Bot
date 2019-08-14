import discord
import asyncio


async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


client = MyClient()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
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
        msg = 'contact@ridgelinestds.net'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('~help'):
        msg = '''```
        ~help       Shows this message
        
        ~info       Shows information about the bot
        
        ~site       Links to the website
        
        ~buy        Links to the Steam page
        
        ~contact    Gives contact information
        ```'''.format(message)
        await message.channel.send(msg)


client.run('yourkeyhere')
