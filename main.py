from dis import dis
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from discord import Interaction, app_commands

load_dotenv()
TOKEN = os.getenv('TOKEN')


class abot(discord.Client):
	def __init__(self):
		super().__init__(intents=discord.Intents.default())
		self.synced = False

	async def on_ready(self):
		await tree.sync(guild=discord.Object(id=776172679731347538))
		self.synced = True
		print('Bot is online')

bot = abot()
tree = app_commands.CommandTree(bot)

@tree.command(name='ping', description='pings the user', guild=discord.Object(id=776172679731347538))
async def self(interation = discord.Interaction):
	await interation.response.send_message('Pong')
	

bot.run(TOKEN)