from asyncio.tasks import run_coroutine_threadsafe
import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand
import asyncio
import random
from discord.ext.commands.errors import BotMissingPermissions
from discord_slash.utils.manage_commands import create_option
import requests
import youtube_dl
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "e!", description = "Tutititutu mais en Python", intents=intents)
slash = SlashCommand(bot, sync_commands = True)
musics = {}
ytdl = youtube_dl.YoutubeDL()

funFact = ["Elbot était créer de base pour diffuser seulement le tutitititutu sur un Channel du serveur Ubuntu le best",
"Elbot a été créer le jeudi 11 février 2021, 09:47:42", 
"Le saviez-vous, il existe un bot by elbot qui permet de réveiller les projets glitch pour que vos bots soi H24 allumé",
"Le créateur de elbot est el2zay",
"Un prochain bot sous le nom de elwatch online, permettera de surveiller vos bots H24, gratuitement. (il sera codé et mis en ligne prochainement)",
"Elbot est open source. Pour voir son code faites la commande e!github.",
"Le saviez-vous? Elbot a été abondoné quelques semaines, plus tard puis el2zay a commencé à le coder grâce à scratch (oui, oui) puis c'est mis au vrai code.",
"Le saviez-vous? Johan et un peu Azrod ont poussé el2zay à me coder.",
"Elbot est toujours en cours de développement et à chaque semaine des mise à jours.",
"Je suis héberger sur glitch et sur la Freebox Delta de el2zay. (et un tout petit bout de code sur le Chrottebook de Johan)"]


status = ["Chante tutititutu tout en changeant pour Ubuntu",
"https://el2zay/elbot.is-a.dev",
"Entrain d'être coder en python et en JS"
"LE CODE JS EST HS!!! Il revient bientôt dès que le bot sera en discord.js13"]

bot.remove_command("help")


@bot.event
async def on_ready():
	print("Le code Python est allumé !")
	changeStatus.start()
@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.idle, activity = game)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title="Commande inexistante", description="Cette commande n'existe pas. Vérifiez que vous n'avez pas fait d'erreur de frappe. Sinon vous pouvez consultez la page d'aide https://el2zay.is-a.dev/elbot/ ", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
        await ctx.message.reply(embed=embed)

    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Erreur", description="Un argument manque (nombre, mot/lettres etc...)\nMerci de réessayer avec un argument.\nCode Erreur:  Erreur N°1", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
        await ctx.message.reply(embed=embed)

    elif isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title="Erreur", description="Vous n'avez pas les permissions requises. Demandez à un administrateur ou au fondateur du serveur.\nCode Erreur : Erreur N°2", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
        await ctx.message.reply(embed=embed)
    elif isinstance(error.original, discord.Forbidden):
      embed=discord.Embed(title="Erreur", description="Je n'ai pas l'autorisation pour faire cette commande. \nEssayez de vérifier les paramètres des rôles sur le serveur.\nCode erreur : Erreur N°3", color=0xff0000)
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
      await ctx.message.reply(embed=embed)




# EN CAS DE TROU DE MÉMOIRE COMMENT ENVOYER UN MESSAGE    
#@bot.event
#async def on_message(message):
 #if message.author == bot.user:
 # return
 #await message.channel.send(f"> {message.content}\n {message.author}")
 #await bot.process_commands(message)

@bot.command()
async def infoserver(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels) #ok
    numberOfVoiceChannels = len(server.voice_channels) #ok
    serverDescription = server.description #ok
    numberOfPerson = server.member_count #ok
    serverName = server.name #ok
    serverOwner = server.owner
    serverRegion = server.region #ok
    serverIcon = server.icon_url #ok
    serverRoles = len(server.roles) #ok
    serverID = server.id #ok
    emoji_count = len(server.emojis) #ok
    embed = discord.Embed(title = "Commande infoserver", description = f"Information sur le serveur **{serverName}**", color=0x00ffff)
    embed.set_thumbnail(url = serverIcon)
    embed.add_field(name = "Nombre de personne : ", value= numberOfPerson, inline = True)
    embed.add_field(name = "Description : ", value= serverDescription, inline = True)
    embed.add_field(name = "Fondateur : ", value = serverOwner, inline = True)
    embed.add_field(name='Date de création :', value=server.created_at.__format__("%d/%m/%Y à %H:%M"), inline=True)
    embed.add_field(name = "ID : ", value = serverID, inline = True)	
    embed.add_field(name = "Region : ", value = serverRegion, inline = True)
    embed.add_field(name = "Nombre de salons textuels : ", value = numberOfTextChannels, inline = True)	
    embed.add_field(name = "Nombre de salons vocaux : ", value = numberOfVoiceChannels, inline = True)	
    embed.add_field(name = "Total de nombre de salons : ", value = numberOfTextChannels+numberOfVoiceChannels, inline = True)	
    embed.add_field(name = "Nombre de personnes : ", value = numberOfPerson, inline = True)	
    embed.add_field(name = "Nombre d'émoji du serveur : ", value = emoji_count, inline = True)		
    embed.add_field(name = "Nombre de rôles : ", value = serverRoles, inline = True)	
    await ctx.send(embed = embed)
	

@bot.command()
async def infoserver2(ctx):
    server = ctx.guild
    serverIcon = server.icon_url
    serverName = server.name
    serverListRole = [r.mention for r in server.roles]
    embed = discord.Embed(title = "Commande infoserver suite", description = f"Partie 2 : Information sur le serveur **{serverName}**", color=0x00ffff)
    embed.set_thumbnail(url = serverIcon)
    embed.add_field(name='Liste des rôles :', value=", ".join(serverListRole))    
    await ctx.send(embed = embed)



@bot.command()
async def heberger(ctx):
 message = ("Le code python est en ce moment hébergé sur la freebox de Elie (c'est pas une blague)")
 await ctx.send(message)

 
#@bot.command()
#async def bonjour(ctx, response):
   # server = ctx.guild
    #serverName = server.name
  #  message = f"Bonjour jeune *padawan* ! Savais tu que tu te trouvais sur le serveur {serverName}, c'est d'ailleur un super serveur car **JE** suis dedans."
  #  await ctx.send(" ".join(message))


@bot.command()
async def funfact(ctx):
 await ctx.send(random.choice(funFact))

@bot.command()
async def chinese(ctx, *text):
	chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append(" ")
	await ctx.send("".join(chineseText))


@bot.command()
async def removebg(ctx, response, texte):
 response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': {texte},
        'size': 'auto'
    },
    headers={'X-Api-Key': 'cUvtLgu3rsbiCCtvxjExGvg1'},
)
 if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
 else:
    print("Error:", response.status_code, response.text)

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
 reason = " ".join(reason)
 await ctx.guild.kick(user, reason = reason) 
 await ctx.send(f"{user} à été kick.Pour la raison: {reason}")
"""
async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)

@bot.command()
@commands.has_permissions(mute_members = True)
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été mute !")

@bot.command()
@commands.has_permissions(mute_members = True)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute !")
"""
#https://www.color-hex.com
#ne pas oublier le 0x avant le code de la couleur




@bot.command()
async def avatar(ctx):
	embed = discord.Embed(title = "Avatar", description = "Voici votre avatar")
	embed.set_thumbnail(url = ctx.author.avatar_url)
	await ctx.send(embed = embed)



	
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *, reason = None):
 if reason is None:
  reason = "aucune raison"
 reason = "".join(reason)
 await ctx.guild.ban(user, reason = reason)
 embed = discord.Embed(title = "Bannissement", description = "Un modérateur a frappé !", color=0xff2812)
 embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url) #url = "lien" 
 embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/795288700594290698/879044070255759410/pngaaa.com-1429166.png")
 embed.add_field(name = "Membre banni", value= user.name, inline = True)
 embed.add_field(name = "Raison", value = reason, inline = True)
 embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
 #embed.set_footer(text = "Coucou")
 await ctx.send(embed = embed)


@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été unban.")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

 

def isOwner(ctx):
 return ctx.message.author.id == 727572859727380531

@bot.command()
@commands.check(isOwner)
async def private(ctx):
	await ctx.send("Cette commande peut seulement être effectuéee par le propriétaire du bot !")
 
@bot.command()
async def roulette(ctx):
	await ctx.send("La roulette commencera dans 10 secondes. Envoyez \"moi\" dans ce channel pour y participer.")
	
	players = []
	def check(message):
		return message.channel == ctx.message.channel and message.author not in players and message.content == "moi"

	try:
		while True:
			participation = await bot.wait_for('message', timeout = 10, check = check)
			players.append(participation.author)
			print("Nouveau participant : ")
			print(participation)
			await ctx.send(f"**{participation.author.name}** participe au tirage ! Le tirage commence dans 10 secondes")
	except: #Timeout
		print("Demarrage du tirrage")

	gagner = ["ban", "kick", "role personnel", "mute", "gage"]

	await ctx.send("Le tirage va commencer dans 3...")
	await asyncio.sleep(1)
	await ctx.send("2")
	await asyncio.sleep(1)
	await ctx.send("1")
	await asyncio.sleep(1)
	loser = random.choice(players)
	price = random.choice(gagner)
	await ctx.send(f"La personne qui a gagnée un {price} est...")
	await asyncio.sleep(1)
	await ctx.send("**" + loser.name + "**" + " !")



@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Le ping pong c'est de la merde je préfère utiliser des briques comme raquettes mais en tout cas j'ai {round(bot.latency * 1000)}ms (PY)")


#slash

@slash.slash(name="number", guild_ids=[865914342041714700], description="Choisi un nombre au hasard pour toi.", options=[
    create_option(name="limite_inferieure", description="Le nombre le plus bas.", option_type=4, required= True),
    create_option(name="limite_superieure", description="Le nombre le plus haut.", option_type=4, required= True)

])
async def number(ctx, limite_inferieure = 1, limite_superieure = 10):
     await ctx.send("Le nombre choisi par moi même est...")
     await asyncio.sleep(1)
     await ctx.send("Roulement de tambours")
     await asyncio.sleep(2)
     await ctx.send("https://tenor.com/view/pitch-perfect-belly-drum-belly-fat-gif-4484753")
     await asyncio.sleep(1)
     num = random.randint(limite_inferieure, limite_superieure)
     await ctx.send(f"**{num}**")








#JAVASCRIPT 

@bot.command()
async def pessi(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)

@bot.command()
async def say(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)

@bot.command()
async def uno(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)

@bot.command()
async def sondage(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)



@bot.command()
async def restart(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)



@bot.command()
async def clear(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)

@bot.command()
async def invite(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)

@bot.command()
async def github(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: el2zay.is-a.dev/elbot\nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)


@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)


@bot.command()
async def play(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)

@bot.command()
async def stop(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)

@bot.command()
async def brique(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)

@bot.command()
async def rickdetect(ctx):
    embed=discord.Embed(title="Erreur", description="Le code JS n'est pas disponible pour l'instant.\nPour savoir quelles commandes sont disponibles en Python vous pouvez aller voir la page d'aide: https://el2zay.is-a.dev/elbot \nLe code JS revient bientôt!\nCode erreur : Erreur N°4", color=0xff0000)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
    await ctx.message.reply(embed=embed)

bot.run("T'as cru quoi mdrrr")
