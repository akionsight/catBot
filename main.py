from discord.ext import commands
import requests
from startup import *
bot = commands.Bot(command_prefix='`')

@bot.event
async def on_ready():
    print('bot has started')

    
@bot.command()
async def cat(ctx):
    channel_id = ctx.channel.id
    if str(channel_id) in allowed_channels:
        await ctx.send(requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url'])
    else:
        await ctx.send('Sorry, Cat Images are not allowed in this channel')

bot.run(token)


# https://discord.com/api/oauth2/authorize?client_id=839169888098451456&permissions=268435584&scope=bot