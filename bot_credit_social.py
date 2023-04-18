import discord
from discord.ext import commands

default_intents = discord.Intents.all()


client = discord.Client(intents = default_intents)
bot = commands.Bot(command_prefix="!", intents = default_intents)



@bot.event
async def on_ready():
	print("le bot est pret")
	


@bot.event
async def on_message(message):
	mess = message.content.lower()

	if mess=="nan" or mess=="non" or mess=="nn" :
		await message.channel.send("Bril !")

	
	elif mess=="oui" or mess=="wi" or mess=="ui" :
		await message.channel.send("Fi !")

	elif "dictature" in mess :
		await message.channel.send("N'oublions pas que le Royaume de Chagasse n'est pas une dictatur* ! Gloire à notre Sainte Chagasse !")

	elif mess=="a" or mess=="ha" or mess=="ah" :
		await message.channel.send("ah !")

	elif mess=="qui" or mess=="qui " or mess=="qui ?" :
		await message.channel.send("Quette !")

	elif "quoi" in mess or "qwa" in mess or mess=="coi" or mess=="coi ?":
		await message.channel.send("Feur !")

@bot.event
async def on_message2(message):
	mess = message.content.lower()

	if "quoi" in mess or "qwa" in mess or mess=="coi" or mess=="coi ?":
		await message.channel.send("Feur !")





bot.run("MTA5MDY4MjYwMDAyNjI4NDEwMg.GtQoeC.Tegd8TP-jcV_xfTzvFLVTInqhafoiHF4XW2CAo")