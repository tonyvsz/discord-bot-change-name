import discord

#discord.py install (pip3 install discord) (https://pypi.org/project/discord.py/)

client = discord.Client()

token = 'TOKEN HERE'

name="NAME HERE"

@client.event
async def on_ready():
    await client.user.edit(username=name)
    
client.run(token)