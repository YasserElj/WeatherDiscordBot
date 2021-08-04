import discord
from Weather import weather
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('weather') or message.content.startswith('Weather') or message.content.startswith('WEATHER'):
        u = weather(message.content.split(" ", 1)[1])
        w =  u[0]+'  '+u[1] #+ '\n'+u[2]
        await message.channel.send(w)

    if message.content.startswith('What is your name'):

        await message.channel.send('Wa sir khalina na3so ')

#You can get the Token from your Discord Developer Portal.
client.run('Token')
