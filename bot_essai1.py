import discord
import os
from discord.ext import commands

token_value = os.getenv("Token")
default_intents = discord.Intents.all()


client = discord.Client(intents = default_intents)
bot = commands.Bot(command_prefix="!", intents = default_intents)



@bot.event
async def on_ready():
	print("le bot est pret")
	


@bot.event
async def on_message(message):
	mess = message.content.lower()

	if "quoi" in mess or "qwa" in mess or mess=="coi" or mess=="coi ?":
		await message.channel.send("Feur !")





bot.run("MTA5MDY4MjYwMDAyNjI4NDEwMg.GxKd2L.vd9l56q3XtdPr0yobtoMciXw9HdT8qYUYhJwLY")

