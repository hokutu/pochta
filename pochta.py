import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='.')
 
bot.remove_command("help")

@bot.command()

async def train(ctx):
    await ctx.send('Доставка в пути >_<')

@bot.command()

async def price(ctx):
    await ctx.send('Цены за доставку: 10мф - до 5 тыс. блоков от спавна, дальше за каждые 1 тыс. блоков к стоимости будет прибавляться 5мф.')

@bot.command(pass_context=True)

async def queue(ctx):
    embed=discord.Embed( title = "Доставка", description="На данный момент, очередь составляет: 0", color=0x979c9f)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)

async def help(ctx):
    embed=discord.Embed(title="Помощь по командам", description=".price - цены за доставку \n.queue - показывает очередь доставки \n.time - показывает время ", color = 0xf1c40f)    
    await ctx.send(embed=embed)

@bot.command(pass_context=True)

async def time(ctx):
	embed=discord.Embed(title="Время(МСК)", url="https://time100.ru/", description=" ", color=0xe91e63)
	await ctx.send(embed=embed) 

bot.run('ODEwMjIyODYyNDE3Nzg4OTc5.YCgg1w.-fgxOspoNMbZ9DklnFUY7UOnl6I')