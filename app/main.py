from asyncio.tasks import run_coroutine_threadsafe
import discord
from discord.ext import commands, tasks
import asyncio
import random
import requests
import youtube_dl


bot = commands.Bot(command_prefix = "e!", description = "Tutititutu mais en Python")
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
"e!help",
"https://el2zay/elbot.is-a.dev",
"Entrain d'être coder en python et en JS"]



@bot.event
async def on_ready():
	print("Le code Python est allumé !")
	changeStatus.start()
@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.dnd, activity = game)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title="Commande inexistante", description="Cette commande n'existe pas. Vérifiez que vous n'avez pas fait d'erreur de frappe. Sinon vous pouvez consultez la page d'aide https://el2zay.is-a.dev/elbot/ ", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
        await ctx.message.reply(embed=embed)

@bot.command()
async def pessi(ctx):
    await ctx.send()

@bot.command()
async def say(ctx):
    await ctx.send()

@bot.command()
async def uno(ctx):
    await ctx.send()

@bot.command()
async def sondage(ctx):
    await ctx.send()

@bot.command()
async def test(ctx):
    await ctx.send()


@bot.command()
async def restart(ctx):
    await ctx.send()



@bot.command()
async def clear(ctx):
    await ctx.send()

@bot.command()
async def invite(ctx):
    await ctx.send()

@bot.command()
async def github(ctx):
    await ctx.send()

@bot.command()
async def play(ctx):
    await ctx.send()

@bot.command()
async def stop(ctx):
    await ctx.send()

@bot.command()
async def brique(ctx):
    await ctx.send()

@bot.command()
async def rickdetect(ctx):
    await ctx.send()



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
    serverOwner = server.owner #ok
    serverRegion = server.region #ok
    serverIcon = server.icon_url #ok
    serverRoles = len(server.roles) #ok
    serverID = server.id #ok
    serverRoleList = [r.mention for r in server.roles] #ok
    emoji_count = len(server.emojis) #ok
    embed = discord.Embed(title = "Commande infoserver", description = f"Information sur le serveur **{serverName}**", color=0x00ffff)
    embed.set_thumbnail(url = serverIcon)
    embed.add_field(name = "Nombre de personne : ", value= numberOfPerson, inline = True)
    embed.add_field(name = "Description : ", value= serverDescription, inline = True)
    embed.add_field(name = "Fondateur : ", value = serverOwner, inline = True)
    embed.add_field(name = "ID : ", value = serverID, inline = True)	
    embed.add_field(name = "Region : ", value = serverRegion, inline = True)
    embed.add_field(name = "Nombre de salons textuels : ", value = numberOfTextChannels, inline = True)	
    embed.add_field(name = "Nombre de salons vocaux : ", value = numberOfVoiceChannels, inline = True)	
    embed.add_field(name = "Total de nombre de salons : ", value = numberOfTextChannels+numberOfVoiceChannels, inline = True)	
    embed.add_field(name = "Nombre de personnes : ", value = numberOfPerson, inline = True)	
    embed.add_field(name = "Nombre d'émoji du serveur : ", value = emoji_count, inline = True)		
    embed.add_field(name = "Nombre de rôles : ", value = serverRoles, inline = True)	
    embed.add_field(name = "Liste des rôles", value = serverRoleList, inline = True)
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






bot.run("ba nan mdr")
