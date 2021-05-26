import codecs
import aiohttp
import discord
import discord
from bs4 import BeautifulSoup
from discord.ext import commands

'''Translator cog - Love Archit & Lyric'''



class translate(commands.Cog):
    def __init__(self, client):
        self.client = client



if country_name is not None:
        if country_name["name"]["common"] == "France":
            language = 'fr'
        elif country_name["name"]["common"] == "Germany":
            language = 'de'
        elif country_name["name"]["common"] == "India":
            language = 'hi'
        elif country_name["name"]["common"] == "United States":
            language = 'en'
        elif country_name["name"]["common"] == "Spain":
            language = 'es'
        elif country_name["name"]["common"] == "Russia":
            language = 'ru'
        elif country_name["name"]["common"] == "Portugal":
            language = 'pt'
        elif country_name["name"]["common"] == "Japan":
            language = 'ja'
        else:
            language = None




def setup(client):
    client.add_cog(translate(client))