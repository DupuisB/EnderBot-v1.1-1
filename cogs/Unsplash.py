import discord
import requests
import datetime
from discord.ext import commands



class Unsplash(commands.Cog, name='Unsplash API Cog'):
    def __init__(self, client):
        self.client = client
        self.client_id = "iLV6ovgx4BSReJmcvj7TiJ7CBRwqLbCE4HjTatV1V6c"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Client-ID {self.client_id}'
        }

    @commands.Cog.listener()
    async def unsplash(self, ctx):
        pass  #Can put command or message detailing sub-commands for unsplash

    @commands.command(name='photosearch', aliases= ['picsearch', 'imagesearch', 'picturesearch'])
    async def photosearch(self, ctx, *query):
        if query == None:
            embed = discord.Embed(colour=0xffffff,
                                  description="No search query was provided")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_author(name="Something is not right...")
            embed.set_footer(text="Thanks to Brady! ")
            await ctx.send(embed=embed)
        else:
            try:
                url = f'https://api.unsplash.com/search/photos?page=1&query={query}&per_page=1'  #change the amount of results the API gets per page. Follow API guidlines.
                r = requests.get(url, headers=self.headers)
                data = r.json()
                embed = discord.Embed(
                    colour=int(data['results'][0]['color'].strip('#'), 16))
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_image(url=f"{data['results'][0]['urls']['regular']}")
                embed.set_author(
                    name=
                    f"Photo by {data['results'][0]['user']['name']} on Unsplash",
                    url=f"{data['results'][0]['user']['links']['html']}")
                embed.set_footer(text="Thanks Brady!")
                embed.add_field(name="Photo Likes",
                                value=f"`{data['results'][0]['likes']}`",
                                inline=True)
                embed.add_field(
                    name="More info about photo",
                    value=
                    f"[Click here]({data['results'][0]['links']['html']})",
                    inline=True)
                try:
                    embed.add_field(
                        name="Photo Description",
                        value=f"`{data['results'][0]['description']}`",
                        inline=True)
                except:
                    embed.add_field(name="Photo Description",
                                    value=f"`No Description Provided`",
                                    inline=True)
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(
                    colour=0xffffff,
                    description="No photos for query provided")
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_author(name="Something is not right...")
                embed.set_footer(text="Thanks Brady! ")
                await ctx.send(embed=embed) 
                
    @commands.command(name='random', aliases=['wall','wallpaper'])
    async def random(self, ctx):
        url = f'https://api.unsplash.com/photos/random'
        r = requests.get(url, headers=self.headers)
        data = r.json()
        embed = discord.Embed(colour=int(data['color'].strip('#'), 16))
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_image(url=f"{data['urls']['regular']}")
        embed.set_author(name=f"Photo by {data['user']['name']} on Unsplash",
                         url=f"{data['user']['links']['html']}")
        embed.set_footer(
            text="OMG IT WORKED"
        )  #add your own bot name and profile image if you prefer
        embed.add_field(name="Photo Downloads",
                        value=f"`{data['downloads']}`",
                        inline=True)
        embed.add_field(name="Photo Likes",
                        value=f"`{data['likes']}`",
                        inline=True)
        try:
            embed.add_field(
                name="Photo Location",
                value=
                f"`{data['location']['city']}, {data['location']['country']}`",
                inline=True)
        except:
            embed.add_field(name="Photo Location",
                            value=f"`No Location Provided`",
                            inline=True)

        await ctx.send(embed=embed)


    @commands.command()
    async def profile(self, ctx, username=None):
        if username == None:
            embed = discord.Embed(colour=0xffffff,
                                  description="No username was provided")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_author(name="Something is not right...")
            embed.set_footer(text="Maybe")
            await ctx.send(embed=embed)
        else:
            try:
                url = f'https://api.unsplash.com/users/{username}'
                r = requests.get(url, headers=self.headers)
                data = r.json()
                embed = discord.Embed(colour=0x845169,
                                      description=f"{data['bio']}")
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_thumbnail(url=f"{data['profile_image']['small']}")
                embed.set_author(name=f"{data['name']} on Unsplash",
                                 url=f"https://unsplash.com/@{username}",
                                 icon_url=f"{data['profile_image']['large']}")
                embed.set_footer(text="oh my god")
                embed.add_field(
                    name="Total Downloads",
                    value=f"`{data['downloads']}`",
                    inline=True
                )  #add your own bot name and profile image if you prefer
                embed.add_field(name="Total Likes",
                                value=f"`{data['total_likes']}`",
                                inline=True)
                embed.add_field(name="Total Photos",
                                value=f"`{data['total_photos']}`",
                                inline=True)
                embed.add_field(name="Total Followers",
                                value=f"`{data['followers_count']}`",
                                inline=True)
                embed.add_field(name="Total Following",
                                value=f"`{data['following_count']}`",
                                inline=True)
                embed.add_field(name=f"{data['name']}'s Location",
                                value=f"`{data['location']}`",
                                inline=True)
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(colour=0xffffff,
                                      description="This user does not exist")
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_author(name="Something is not right...")
                embed.set_footer(text="lol")
                await ctx.send(embed=embed)

    #If your query contains a space replace it  with '-'. For example, if your search query is white house, instead use white-house or it will just search for white.
    #I will eventually auto add it, but for now, just add it manually. It's easy.
    #If you want more than the first result just copy/pase the else statement and change the lists to 1 to get the second query

def setup(bot):
    bot.add_cog(Unsplash(bot))
    print('Unsplash API Cog loaded')
