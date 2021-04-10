import json
import discord
from discord.ext import commands

from bs4 import BeautifulSoup
import requests
import time

bot = commands.Bot(command_prefix='<', description="El bot Stonks")
#You must add your api key from https://fixer.io/
currency_api_key = ''

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

@bot.command()
async def currency(ctx, currency):
    url = 'http://data.fixer.io/api/latest?access_key=' + currency_api_key + '&format=1'
    response = requests.get(url).json()
    try:
        await ctx.send('1EUR = ' + str(response['rates'][currency]) + currency)
    
    except:
        await ctx.send('Invalid currency, try again!')

@bot.command()
async def convert(ctx, currency, destination, quantity):
    url = 'http://data.fixer.io/api/latest?access_key=' + currency_api_key + '&format=1'
    response = requests.get(url).json()
    currency1Eur = float(1/response['rates'][currency])
    destination1Eur = float(1/response['rates'][destination])
    total = currency1Eur / destination1Eur * float(quantity)
    await ctx.send('{}{} -> {}{}'.format(quantity, currency, round(total), destination))



@bot.event 
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Hacer Stonks", url="http://www.hypixel.com"))
    print('My Bot is Ready')
 
bot.run('')
