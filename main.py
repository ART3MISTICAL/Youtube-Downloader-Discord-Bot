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
async def self(i: discord.Interaction):
	await i.response.send_message('Pong')
	
@tree.command(name='download-video', description='download video from youtube', guild=discord.Object(id=776172679731347538))
@app_commands.choices(choices=[
    app_commands.Choice(name="720", value="720"),
    app_commands.Choice(name="360", value="360"),
    ])
async def self(i: discord.Interaction, url:str, choices: app_commands.Choice[str]):
	await i.response.send_message(f'{url} in {choices.value}p')

bot.run(TOKEN)