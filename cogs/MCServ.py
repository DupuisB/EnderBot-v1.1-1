import discord
import socket
from discord.ext import commands
from mcstatus import MinecraftServer

class MCServ(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.servers = [{
            "ip": "35.233.48.175",
            "desc": "SMP server"
        }]
        self.mc_embed = discord.Embed(
            title="**Minecraft server status :**", description="_ _\n")
        self.mc_embed.set_thumbnail(
            url=
            "https://i.imgur.com/lFmprqT.jpg"
        )

    @commands.command(
        brief='Minecraft server status',
        aliases=['mcserv', 'mcstatus', 'servip', 'servmc', 'serv'])
    async def mc(self, ctx):
        self.mc_embed.clear_fields()
        for server in self.servers:
            try:
                status = MinecraftServer.lookup(server['ip']).status()
            except (ConnectionRefusedError, socket.timeout):
                embed_value = ':x: Server is offline!'
                embed_value += '\n\n_ _' if server == self.servers[0] else ''
                self.mc_embed.add_field(
                    name=server['desc'], value=embed_value, inline=False)
            else:
                online_players = status.players.online
                sample = sorted([
                    p.name for p in status.players.sample
                ]) if status.players.sample is not None else []
                sample_title = "Online players" if online_players != 1 else "Online player"
                sample_txt = ''
                if online_players != 0:
                    diff = online_players - len(sample)
                    if diff > 0:
                        sample_txt = ", ".join(sample) + f" et {diff} autre"
                        sample_txt += "." if diff == 1 else "s."
                    elif online_players == 1:
                        sample_txt = sample[0]
                    else:
                        sample_txt = ", ".join(
                            sample[:-1]) + " et " + sample[-1]
                embed_value = f':white_check_mark: Server is online!\n\n**{online_players} {sample_title}**\n' + discord.utils.escape_markdown(
                    sample_txt)
                embed_value += '\n\n_ _' if server == self.servers[0] else ''
                self.mc_embed.add_field(
                    name=server['desc'], value=embed_value, inline=False)
        await ctx.send(embed=self.mc_embed)


def setup(client):
    client.add_cog(MCServ(client))
