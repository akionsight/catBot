from discord.ext import commands
import aiohttp
from startup import *
bot = commands.Bot(command_prefix='`')

@bot.event
async def on_ready():
    print('bot has started')

    
@bot.command()
async def cat(ctx):
    channel_id = ctx.channel.id
    if str(channel_id) in allowed_channels:
        async with aiohttp.request("GET", "https://api.thecatapi.com/v1/images/search") as r:
            r = await r.json()
            await ctx.send(r[0]['url'])
    else:
        await ctx.send('Sorry, Cat Images are not allowed in this channel')

bot.run(token)


# https://discord.com/api/oauth2/authorize?client_id=839169888098451456&permissions=268435584&scope=bot