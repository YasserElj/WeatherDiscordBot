import discord
from weatherAPI import weatherAPI
import time

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

        timeNow = time.strftime("%a, %d %b %Y %H:%M:%S",time.gmtime(time.time()))

        await message.channel.send(f'{u[0]}°C {u[3]}  \n{u[1]} \n{timeNow} GMT')

    if message.content.startswith('!time'):
        timeNow = time.strftime("%a, %d %b %Y %H:%M:%S",time.gmtime(time.time()))
        await message.channel.send(f'{timeNow} GMT')


#You can get the Token from your Discord Developer Portal.
client.run('TOKEN')