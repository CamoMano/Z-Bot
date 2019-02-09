import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('------------------------------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------------------------')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('~info'):
        msg = '```Author: CamoMano```'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('~site'):
        msg = 'https://www.playzgame.net'.format(message)
        await client.send_message(message.channel, msg)


    if message.content.startswith('~buy'):
        msg = 'https://store.steampowered.com/app/786770/Z_The_End/'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('~help'):
        msg = '''```
        ~help       Shows this message
        
        ~info       Shows bot info
        
        ~site       Links website
        
        ~buy        Links steam page
        ```'''.format(message)
        await client.send_message(message.channel, msg)
        

        
     
        
       


client.run('yourkeyhere')
