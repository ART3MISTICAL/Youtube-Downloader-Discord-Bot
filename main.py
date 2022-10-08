from dis import dis
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

class abot(discord.Client):
	def __init__(self):
		super().__init__(intents=discord.Intents.default())
		self.synced = False

	async def on_ready(self):
		await tree.sync(guild=discord.Object(id=776172679731347538))
		self.sync = True
		print('Bot is online')

bot = abot()
tree = app_commands.CommandTree(bot)

bot.run(TOKEN)