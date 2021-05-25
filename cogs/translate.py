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

@bot.event
async def on_reaction_add(reaction, user):
    print("You added a reaction"+reaction.emoji)

    received_emoji = reaction.emoji
    country_name = get_country(received_emoji)
    print(country_name)
    if country_name is not None:
        languages = supported_languages.SupportedLanguages
        if country_name["name"]["common"] == "France":
            language = languages.French
        elif country_name["name"]["common"] == "Germany":
            language = languages.German
        elif country_name["name"]["common"] == "India":
            language = languages.Hindi
        elif country_name["name"]["common"] == "United States":
            language = languages.English
        elif country_name["name"]["common"] == "Spain":
            language = languages.Spanish
        elif country_name["name"]["common"] == "Russia":
            language = languages.Russian
        elif country_name["name"]["common"] == "Portugal":
            language = languages.Portuguese
        elif country_name["name"]["common"] == "Japan":
            language = languages.Japanese
        else:
            language = None

        if language is not None:
            api = TranslatorApi.TranslatorApi()
            text = [{"text": reaction.message.content}]
            translation = api.translate(text, language)
            response = translation.text
            response = json.loads(response)
            if response[0]["detectedLanguage"] is not None:
                if response[0]["translations"] is not None:
                    translated_text = response[0]["translations"][0]["text"]
                    if user.dm_channel is None:
                        await user.create_dm()
                    await user.dm_channel.send("Message `" + reaction.message.content + "` from user " + reaction.message.author.name +  " \ntranslated message : `" + translated_text + "`")
                else:
                    print(response)
                    await reaction.message.channel.send("Translation Failed")
            else:
                print(response)
                await reaction.message.channel.send("We were not able to detect input language")

        else:
            await reaction.message.channel.send("Languages of {} are currently not supported".format(country_name["name"]["common"]))
    else:
        print("Normal emoji found exiting")
    return

def setup(client):
    client.add_cog(translate(client))