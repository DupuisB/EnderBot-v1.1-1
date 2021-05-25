import discord
from discord.ext import commands
from os import environ, listdir
import requests, json

def get_weather(city):
    try:
        base_url = "http://api.weatherapi.com/v1/current.json?key=1962ba72cdc748e49eb63520211105"
        complete_url = base_url + "&q=" + city
        response =  requests.get(complete_url) 
        result = response.json()

        city = result['location']['name']
        country = result['location']['country']
        time = result['location']['localtime']
        wcond = result['current']['condition']['text']
        celcius = result['current']['temp_c']
        fahrenheit = result['current']['temp_f']
        fclike = result['current']['feelslike_c']
        fflike = result['current']['feelslike_f']

        embed=discord.Embed(title=':white_sun_cloud: 'f"{city}"' Weather', description=f"{country}", color=0x14aaeb)
        embed.add_field(name=":thermometer: Temprature C°", value=f"{celcius}", inline=True)
        embed.add_field(name=":thermometer: Temprature F°", value=f"{fahrenheit}", inline=True)
        embed.add_field(name=":wind_blowing_face: Wind Condition", value=f"{wcond}", inline=False)
        embed.add_field(name=":man_standing: Feels Like C°", value=f"{fclike}", inline=True)
        embed.add_field(name=":person_standing: Feels Like F°", value=f"{fflike}", inline=True)
        embed.set_footer(text='Time: 'f"{time}")
        return embed
    except:
        embed=discord.Embed(title="No response", color=0x14aaeb)
        embed.add_field(name="Error", value="Oops!! Please enter a city name", inline=True)
        return embed

class City_Weather(commands.Cog) :
    def __init__(self, client) :
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self) :
        # await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Hello There!'))
        print("City-Weather Cog is working")

    @commands.command(aliases =['weather', 'city'])
    async def weather2(self, ctx, *city):
            print(city)
            city = str(city)
            city = city.lower()
            result = get_weather(city)
            await ctx.channel.send(embed=result)
            
def setup(bot) :
    bot.add_cog(City_Weather(bot))