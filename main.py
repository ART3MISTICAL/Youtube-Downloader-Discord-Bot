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

@tree.command(name='ping', description='pings the user')
async def self(i: discord.Interaction):
	await i.response.send_message('Pong')
	
@tree.command(name='download-video', description='download video from youtube')
@app_commands.choices(res=[
    app_commands.Choice(name="720", value="720p"),
    app_commands.Choice(name="360", value="360p"),
    ])
async def self(i: discord.Interaction, url:str, res: app_commands.Choice[str]):
	await i.response.send_message(f'Click on this link to download\nhttps://youtube-video-downloader.devansharora.repl.co/downloadforbot/?url={url}&res={res.value}')

@tree.command(name='download-music', description='download music from a yt link')
async def self(i: discord.Interaction, url: str):
	await i.response.send_message(f'Click on this link\nhttps://youtube-video-downloader.devansharora.repl.co/download-music/?url={url}')

@tree.command(name='download-music-playlist', description='download music playlist from yt')
async def self(i: Interaction, url: str):
	await i.response.send_message(f'Click on this link and wait for it download, it might take 3-5 mins\nhttps://youtube-video-downloader.devansharora.repl.co/download-playlist/?url={url}')

bot.run(TOKEN)