import discord
import asyncio
#print(discord.__version__)  # check to make sure at least once you're on the right version!

token = "*********"  # I've opted to just save my token to a text file. 

client = discord.Client()  # starts the discord client.


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome home Master {member.name}! 👋🏿\n\nSince this is your first time in the House, please make sure to read through the entire #🚨start-here🚨 channel to get the most out of being on our server!\n\nIf you have any questions about anything, please don’t hesitate to DM @GlassHouseFX! Happy Trading! 🚀'
    )
    await member.dm_channel.send("https://gfycat.com/linedradiantafricanaugurbuzzard-the-fresh-prince-of-belair-joseph-marcell")


client.run(token)  # recall my token was saved!