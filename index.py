import discord
import random
from discord import channel
from discord.ext import commands, tasks
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *

client = commands.Bot(command_prefix = "+", description = "Bot crée par Monsieur Théo#3379 pour Shadow PUB")
slash = SlashCommand(client, sync_commands=True)
status = ["By Monsieur Théo#3379",
		"Shadow PUB"]

client.remove_command("help")

@client.event
async def on_ready():
	changeStatus.start()
	"""
	channel = client.get_channel(923285976732823623)
	embed = discord.Embed(title = "", description = f"**Drink's BOT a redémarré**", color=0x0CFF00)
	embed.set_footer(text = "Par : Monsieur Théo#3379", icon_url = "https://media.discordapp.net/attachments/890524731961384982/923240996714741820/20210919_120117.png?width=676&height=676")
	await channel.send(embed=embed)
	"""
	print("Prêt !")

@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await client.change_presence(status = discord.Status.online,activity = game)

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("**Désoler mais cette commande n'hésiste pas !**")

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("**Il manque une / des information/s.**")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("**Vous n'avez pas les permissions pour faire cette commande.**")
	elif isinstance(error, commands.CheckFailure):
		await ctx.send("**Oups vous ne pouvez utilisez cette commande.**")
	if isinstance(error.original, discord.Forbidden):
		await ctx.send("**Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande**")

@client.event
async def on_message(message):
	channelverif = client.get_channel(916672530037735444)
	channelwarn = client.get_channel(922468798571900938)
	channellogs = client.get_channel(890524731961384982)
	namepuber = {message.author}
	pubeurnonname = {message.author.id}
	if message.author == client.user:
		return
	embedun = discord.Embed(title = f"**{message.guild.name}**", description = f"**➥ Votre pub doit contenir une __description__.** \n **➥ Votre pub ne doit pas être __NSFW__ et doit respecter les __ToS__ discord.** \n **➥ Votre pub doit respecter le __règlement__ du serveur.**", color=0x0CFF00)
	embedun.set_thumbnail(url = f"{message.guild.icon_url}")
	embedun.set_footer(text = f"Pub posté par : {message.author.name}")
	await message.channel.send(embed=embedun)
	await message.channel.send("https://media.discordapp.net/attachments/885916788485931038/923914538250821672/20211224_132557.png")
	buttons = [
        create_button(
            style=ButtonStyle.success,
            label="Valider la pub",
            custom_id="valider"
        ),
        create_button(
            style=ButtonStyle.danger,
            label="Refuser la pub",
            custom_id="refuser"
        )
    ]
	buttonsrefuser = [
        create_button(
            style=ButtonStyle.blue,
            label="A",
            custom_id="a"
        ),
        create_button(
            style=ButtonStyle.blue,
            label="B",
            custom_id="b"
        ),
        create_button(
            style=ButtonStyle.blue,
            label="C",
            custom_id="c"
        ),
        create_button(
            style=ButtonStyle.blue,
            label="D",
            custom_id="d"
        ),
        create_button(
            style=ButtonStyle.blue,
            label="E",
            custom_id="e"
        )
    ]
	action_row = create_actionrow(*buttons)
	verifmesg = await channelverif.send(f"{message.content} \n \n **Informations :** \n **Pseudo :** {message.author} | `{message.author.id}` \n **Salon :** {message.channel.mention}", components=[action_row])
	button = await wait_for_component(client, components=action_row)
	if button.custom_id == "valider":
		await channellogs.send(f"{message.content} \n \n **Informations :** \n **Pseudo :** {message.author} | `{message.author.id}` \n **Salon :** {message.channel.mention} \n **Vérifier par :** {button.author.display_name}")
		await message.add_reaction("✅")
		await verifmesg.delete()
	if button.custom_id == "refuser":
		action_row = create_actionrow(*buttonsrefuser)
		refusmsg = await channelverif.send(f"**Pour quel motif voulez-vous supprimer la pub de {message.author} ?** \n \n **A = pub dans le mauvais salon** \n **B = lien invalide** \n **C = pub sans description** \n **D = pub hors règlement** \n **E = autre**", components=[action_row])
		button = await wait_for_component(client, components=action_row)
		if button.custom_id == "a":
			await channellogs.send(f"{message.content} \n \n **Informations :** \n **Pseudo :** {message.author} | `{message.author.id}` \n **Salon :** {message.channel.mention} \n **Refuser :** pub dans le mauvais salon \n **Vérifier par :** {button.author.display_name}")
			await channelwarn.send(f"**Warn** \n \n **Utilisateur :** {message.author.mention} \n **Raison :** pub dans le mauvais salon \n **Modérateur :** {button.author.display_name}")
			await verifmesg.delete()
			await message.delete()
			await refusmsg.delete()
		if button.custom_id == "b":
			await channellogs.send(f"{message.content} \n \n **Informations :** \n **Pseudo :** {message.author} | `{message.author.id}` \n **Salon :** {message.channel.mention} \n **Refuser :** lien invalide \n **Vérifier par :** {button.author.display_name}")
			await channelwarn.send(f"**Warn** \n \n **Utilisateur :** {message.author.mention} \n **Raison :** lien invalide \n **Modérateur :** {button.author.display_name}")
			await verifmesg.delete()
			await message.delete()
			await refusmsg.delete()
		if button.custom_id == "c":
			await channellogs.send(f"{message.content} \n \n **Informations :** \n **Pseudo :** {message.author} | `{message.author.id}` \n **Salon :** {message.channel.mention} \n **Refuser :** pub sans description \n **Vérifier par :** {button.author.display_name}")
			await channelwarn.send(f"**Warn** \n \n **Utilisateur :** {message.author.mention} \n **Raison :** pub sans description \n **Modérateur :** {button.author.display_name}")
			await verifmesg.delete()
			await message.delete()
			await refusmsg.delete()
		if button.custom_id == "d":
			await channellogs.send(f"{message.content} \n \n **Informations :** \n **Pseudo :** {message.author} | `{message.author.id}` \n **Salon :** {message.channel.mention} \n **Refuser :** pub hors règlement \n **Vérifier par :** {button.author.display_name}")
			await channelwarn.send(f"**Warn** \n \n **Utilisateur :** {message.author.mention} \n **Raison :** pub hors règlement \n **Modérateur :** {button.author.display_name}")
			await verifmesg.delete()
			await message.delete()
			await refusmsg.delete()
		if button.custom_id == "e":
			await channellogs.send(f"{message.content} \n \n **Informations :** \n **Pseudo :** {message.author} | `{message.author.id}` \n **Salon :** {message.channel.mention} \n **Refuser :** autre \n **Vérifier par :** {button.author.display_name}")
			await channelwarn.send(f"**Warn** \n \n **Utilisateur :** {message.author.mention} \n **Raison :** autre (pour plus d'informations ouvrez un ticket) \n **Modérateur :** {button.author.display_name}")
			await verifmesg.delete()
			await message.delete()
			await refusmsg.delete()
			

client.run("ODk2MDgxODI0NDQ1NTIxOTIw.YWB7Ow.Owrp0AzA9BD9FooylwRMpsWs34Q")