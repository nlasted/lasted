from terminal import terminal_size
from discord.ext import commands
from art import tprint
import colorama
import logging
import discord
import json
import os

with open('bot.json', 'r') as file:
    bot_config_data = file.read()
    bot_config = json.loads(bot_config_data)

with open('auth.json', 'r') as file:
    auth_data = file.read()
    auth = json.loads(auth_data)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=bot_config["prefix"], intents=intents)

@bot.event
async def setup_hook():
    os.system("clear")
    msg = f"Well behaved, raised with love by nlasted bot"
    print(colorama.Fore.CYAN)
    tprint("lasted")
    print(colorama.Fore.RESET)
    print(msg)
    print('=' * terminal_size())
    print(colorama.Fore.LIGHTBLUE_EX + "Loading modules...")
    for filename in os.listdir('./modules'):
        if filename.endswith('.py'):
            await bot.load_extension(f'modules.{filename[:-3]}')
            print(colorama.Fore.GREEN + f"[+] Loaded module: {filename[:-3]}")
    print(colorama.Fore.LIGHTBLUE_EX + "Modules loaded!")

handler = logging.FileHandler(filename='lasted.log', encoding='utf-8', mode='w')

bot.run(auth['token'], log_handler=handler)