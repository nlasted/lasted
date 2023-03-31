from discord.ext import commands
from art import tprint
import colorama, os

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(colorama.Fore.GREEN + f"[+] Loaded bot (ID: {self.bot.user.id}) | Latency: {round (self.bot.latency * 1000)}ms | ¯\_(ツ)_/¯")
        print(colorama.Fore.YELLOW + f"[!] All discord.py logs will be saved in lasted.log.")

async def setup(bot):
    await bot.add_cog(Events(bot))