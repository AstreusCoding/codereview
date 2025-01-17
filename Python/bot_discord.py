"""
This script initializes and runs a Discord bot using the discord.py library.

The bot's token 
function from the bot_token module. The bot is configured with all
and prints a message to the console when it is ready.
Ensure that the .env file is set up with the BOT_TOKEN before running 

Functions:
    on_ready(): Prints a message to the console when the bot is ready.

Modules:
    discord: The discord.py library for creating Discord bots.
    commands: The commands extension from discord.py for creating bot commands.
    bot_token: A custom module to retrieve the bot token from the envir
"""

import discord
from discord.ext import commands
from bot_token import get_bot_token

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """Prints a message to the console when the bot is ready."""
    print(f"{bot.user} is now online!")


bot_token = get_bot_token()

if not bot_token:
    print("Bot token not found. Please set up the .env file with the bot token.")
    input("Press Enter to exit...")
    exit()

if bot_token:
    bot.run(bot_token)
