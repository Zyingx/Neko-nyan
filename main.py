import discord
import os
import time

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Neko'))
    print('You have successfully logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.hello'):
        await message.channel.send("AintNoWay")
        time.sleep(1) 
        await message.channel.send("https://tenor.com/view/noway-gif-254273188714127328")
        return

client.run("MTEzODM3Nzc1MzU0OTM1Mjk4MA.GyLvAb.o_9gglQKoNTOXJ6LfWitJ601P-G5c0EhMnlRf4")