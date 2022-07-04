import discord
from weatherAPI import weatherAPI
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('weather') or message.content.startswith('Weather') or message.content.startswith('WEATHER'):
        city = message.content.split(" ", 1)[1] 
        u = weatherAPI(city)

        await message.channel.send(f'{u[0]}°C {u[4]}  \n{u[1]} \n{u[3]}')


#You can get the Token from your Discord Developer Portal.
client.run('TOKEN')
