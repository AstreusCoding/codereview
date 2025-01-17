# bot_main.py
# This is the main script that initializes and runs the bot,
# importing features from all other modules.

from discord.ext import commands
from discord import Intents
from bot_token import get_bot_token


# Bot initialization
bot = commands.Bot(intents=Intents.all(), command_prefix="!")

# load dotenv

bot_token = get_bot_token()

if not bot_token:
    print("Bot token not found. Please set up the .env file with the bot token.")
    input("Press Enter to exit...")
    exit()


bot.run(bot_token)
