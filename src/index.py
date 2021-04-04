import discord
from discord.ext import commands

from bs4 import BeautifulSoup
import requests
import time

bot = commands.Bot(command_prefix='<', description="El bot Stonks")

@bot.command()
async def ping(ctx):
   await ctx.send('pong')

@bot.command()
async def price(ctx, coin):
    url = 'https://coinmarketcap.com/es/currencies/' + coin + '/'

    HTML = requests.get(url)

    soup = BeautifulSoup(HTML.text, 'html.parser')

    text = soup.find('div', attrs={'class':'priceValue___11gHJ'})
    
    await ctx.send(text.text)






@bot.event 
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Hacer Stonks", url="http://www.hypixel.com"))
    print('My Bot is Ready')
 
bot.run('ODI3OTg4NjY4NTc2NDMyMTU4.YGjCiQ.OVJZ8EzDk_3mB1Jj_RPJ4AIO3Qc')
