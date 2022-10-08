import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('Bot is online')

bot.run(TOKEN)