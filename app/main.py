from asyncio.tasks import run_coroutine_threadsafe
from operator import and_
from typing import Text
import discord
from discord import message
from discord.channel import CategoryChannel
from discord.ext import commands, tasks
from discord.ext.commands.core import check
from discord.user import User
from discord_slash import ButtonStyle , SlashCommand
from discord_slash.utils.manage_components import *
import asyncio
import random
from discord.ext.commands.errors import BotMissingPermissions
from discord_slash.utils.manage_commands import create_option
import requests
import youtube_dl
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = "e!", description = "Tutititutu mais en Python", intents=intents)
slash = SlashCommand(bot, sync_commands=True)
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
"https://el2zay.is-a.dev/elbot",
"Entrain d'être coder en python et en JS",
"Les commandes / sont entrain d'être coder."]


blagueelie = "Eliecoptère\nEliectricité\nPéliecan\nMéneliemontant\n"

reactionrole1 = "**Marque/OS que vous avez**\niPhone 🍎 \nAndroid 🤖\nMac 🖥 \nmacOS nothing 🚫\nWindows 🪟\nLinux 🐧 "
reactionrole2 = "Développeur 👨🏼‍💻\nTwittos 🐦\nYoutuber ▶️\nStreamer 📹\nMonteur 🎞️\nPhotographe 📸\nAntiMEE6 🙈\nFan de tutititutu 🕺\nHomme 👨\nFemme 👩"
reactionrole3 = "Among US 🚀\nMinecraft 🌆\nJeu de course 🏎\nLoL ⚔️\nJeu simulateur 🛩"

bot.remove_command("help")

blurple = 0x6200ea
red = 0xff0000
blue = 0x0000ff
cyan = 0x00ffff
corail = 0xf1263f


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

@bot.command(aliases=['serverinfo'])  #SLASH OK
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




	

@bot.command(aliases=['serverinfo2']) #slash ok
async def infoserver2(ctx):
    server = ctx.guild
    serverIcon = server.icon_url
    serverName = server.name
    serverListRole = [r.mention for r in server.roles]
    embed = discord.Embed(title = "Commande infoserver suite", description = f"Partie 2 : Information sur le serveur **{serverName}**", color=0x00ffff)
    embed.set_thumbnail(url = serverIcon)
    embed.add_field(name='Liste des rôles :', value=", ".join(serverListRole))    
    await ctx.send(embed = embed)

@bot.command(aliases=['infouser'])
async def userinfo(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    username = member.name
    userAvatar = member.avatar_url
    usercreation = member.created_at.strftime("%d/%m/%Y à %H:%M")
    rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
    userjoin = member.joined_at.strftime("%d/%m/%Y à %H:%M")
    embed=discord.Embed(title=f'**Voici les infos de {username} !**', color=0x00ff00)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nom d'utilisateur :", value=member, inline=False)
    embed.add_field(name="Date de création :", value=usercreation, inline=False)
    embed.add_field(name="Date d'arrivée :", value=userjoin, inline=False)
    embed.add_field(name="Rôle(s) :", value=", ".join(rolelist), inline=False)
    await ctx.message.reply(embed=embed)

@bot.command() #ok
async def heberger(ctx):
 message = ("Le code python est en ce moment hébergé sur la freebox de Elie (c'est pas une blague)")
 await ctx.send(message)


 
#@bot.command()
#async def bonjour(ctx, response):
   # server = ctx.guild
    #serverName = server.name
  #  message = f"Bonjour jeune *padawan* ! Savais tu que tu te trouvais sur le serveur {serverName}, c'est d'ailleur un super serveur car **JE** suis dedans."
  #  await ctx.send(" ".join(message))


@bot.command() #fait en slash
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
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
 reason = " ".join(reason)
 await ctx.guild.kick(user, reason = reason) 
 embed = discord.Embed(title = "Kick", description = f"{user} à été kick.Pour la raison: {reason}", color=red)
 await ctx.send(embed = embed)


#https://www.color-hex.com
#ne pas oublier le 0x avant le code de la couleur




@bot.command()
async def avatar(ctx):
	embed = discord.Embed(title = "Avatar", description = "Voici votre avatar")
	embed.set_thumbnail(url = ctx.author.avatar_url)
	await ctx.send(embed = embed)


@bot.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(title = "Lock", description = f"Le salon, {ctx.message.channel} est désormais verouillé 🔒", color=0x0000ff)
    await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_channels = True)
async def unlock(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(title = "Lock", description = f"Le salon, {ctx.message.channel} est désormais déverouillé 🔓", color=0x0000ff)
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

def elWatchServ(ctx):
 return ctx.guild.id == 881488037979250768

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


@bot.command()
async def cuisiner(ctx):
    await ctx.send ("Envoyez le plat que vous voulez cuisiner")

    def checkMessage(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel
    
    try:
       recette = await bot.wait_for("message", timeout = 10, check = checkMessage)
    except:
        embed=discord.Embed(title="Erreur: TIMEOUUUUUUUUT", description="Cela fait plus de 10 secondes que la commade a été lancé et que vous n'avez pas répondu à cette commande. \nVous pouvez réessayer en recommençant la commande.\n Erreur N°5 ", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
        await ctx.message.reply(embed=embed)
    message = await ctx.send(f"La préparation de {recette.content} va commencer. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id   and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")    #pour éviter qu'une autre personne met la réaction à la place de la personne qui a demandé de cuisiner
    try:
        reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji)
        if reaction.emoji == "✅":
            await ctx.send("La recette a démarré")
        else: 
            await ctx.send("La recette a bien été annulé.")
    except:
        embed=discord.Embed(title="Erreur: TIMEOUUUUUUUUT", description="Cela fait plus de 10 secondes que la commade a été lancé et que vous n'avez pas répondu à cette commande. \nVous pouvez réessayer en recommençant la commande.\n Erreur N°5 ", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
        await ctx.message.reply(embed=embed)

#brouillon 
"""@bot.command()
@commands.check(isOwner)
async def reaction(ctx):
    embed = discord.Embed(title= "Reaction-roles",description = reactionrole1, color = blurple)
    message = await ctx.send(embed = embed)
    await message.add_reaction("🍎")
    await message.add_reaction("🤖")
    await message.add_reaction("🖥")
    await message.add_reaction("🚫")
    await message.add_reaction("🪟")
    await message.add_reaction("🐧")
    async def waitForReaction():
        reaction, user = await bot.wait_for("reaction_add")
        if reaction.emoji == "🍎":
            await ctx.send(f"{user.name} a sélectionné la réaction 🍎")
            await waitForReaction()
        if reaction.emoji == "🤖":
            await ctx.send(f"{user.name} a sélectionné la réaction 🤖")
            await waitForReaction()
        if reaction.emoji == "🖥":
            await ctx.send(f"{user.name} a sélectionné la réaction 🖥")
            await waitForReaction()
        if reaction.emoji == "🚫":
            await ctx.send(f"{user.name} a sélectionné la réaction 🚫")
            await waitForReaction()
        if reaction.emoji == "🪟":
            await ctx.send(f"{user.name} a sélectionné la réaction 🪟")
            await waitForReaction()
        if reaction.emoji == "🐧":
            await ctx.send(f"{user.name} a sélectionné la réaction 🐧")
            await waitForReaction()
    await waitForReaction()




@bot.command()
@commands.check(isOwner)
async def reaction1(ctx):
    embed = discord.Embed(title= "Vous êtes?",description = reactionrole2, color = blurple)
    message = await ctx.send(embed = embed)
    await message.add_reaction("👨🏼‍💻")
    await message.add_reaction("🐦")
    await message.add_reaction("▶️")
    await message.add_reaction("📹")
    await message.add_reaction("🎞️")
    await message.add_reaction("📸")
    await message.add_reaction("🙈")
    await message.add_reaction("🕺")
    await message.add_reaction("👨")
    await message.add_reaction("👩")
    async def waitForReaction():
        reaction, user = await bot.wait_for("reaction_add")
        if reaction.emoji == "👨🏼‍💻":
            await ctx.send(f"{user.name} a sélectionné la réaction 👨🏼‍💻")
            await waitForReaction()
        if reaction.emoji == "🐦":
            await ctx.send(f"{user.name} a sélectionné la réaction 🐦")
            await waitForReaction()
        if reaction.emoji == "▶️":
            await ctx.send(f"{user.name} a sélectionné la réaction ▶️")
            await waitForReaction()
        if reaction.emoji == "📹":
            await ctx.send(f"{user.name} a sélectionné la réaction 📹")
            await waitForReaction()
        if reaction.emoji == "🎞️":
            await ctx.send(f"{user.name} a sélectionné la réaction 🎞️")
            await waitForReaction()
        if reaction.emoji == "🕺":
            await ctx.send(f"{user.name} a sélectionné la réaction 🕺")
            await waitForReaction()
        if reaction.emoji == "👨":
            await ctx.send(f"{user.name} a sélectionné la réaction 👨")
            await waitForReaction()
        if reaction.emoji == "👩":
            await ctx.send(f"{user.name} a sélectionné la réaction 👩")
            await waitForReaction()

    
    embed2 = discord.Embed(title= "Vous jouez à quels jeux?",description = reactionrole3, color = blurple)
 

    await message2.add_reaction("🚀")
    await message2.add_reaction("🌆")
    await message2.add_reaction("🏎")
    await message2.add_reaction("⚔️")
    await message2.add_reaction("🛩")
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
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été mute !")

@bot.command()
@commands.check(isOwner)
async def verify(ctx):
    message = await ctx.send(f"> Bienvenue à vous sur le serveur **{ctx.guild.name}**\n> \n> Vous devez lire les règles pour avoir un accès complet au serveur.\n> **Règle N°1**: Surveillez votre language, interdiction aux insultes et mot innaproprié qui pourraient blessé des personnes. Cependant les mots du style merde, putain... sont autorisés mais doivent être utilisés avec modération. \n> **Règles N°2** Interdiction de everyone\n> **Règles N°3** Vous avez totalement le droit de mentionner les fondateurs sans abus pour par exemple une relance au cas où nous avons oublié de rajouter votre bot (PS: Promis ça sera très rare)\n> **Règle N°4** Vous devez avoir un pseudo sans caractères illisibles afin de vous mentionner facilement. Si vous en avez un votre pseudo sera modifié.\n> **Règles N°5** On essayera de rendre aussi ce serveur communautaire et pas seulement pour la surveillance de bot donc si vous le souhaitiez vous pouvez parler dans le général de ce serveur.\n> Des question? Vous pourrez trouver plusieurs réponses dans le prochain salon ou sinon vous pouvez demander au staff ou aux fondateurs.\n \n Tout est ok pour vous? Parfait. Vous pouvez appuyer sur la réaction ✅")
    await message.add_reaction("✅")
    reaction, user = await bot.wait_for("reaction_add")       
    if reaction.emoji == "✅":
        await ctx.send("La recette a démarré")


    


@bot.command()
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute !")


async def getVerifiéRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "👤 Membre 👤":
            return role
    
@bot.command()
async def verified(ctx, member : discord.Member):
    verifiérole = await getVerifiéRole(ctx)
    await member.add_roles(verifiérole)
    await ctx.send(f"{member.mention} a été vérifié !")

@bot.command()
async def unverified(ctx, member : discord.Member):
    verifiérole = await getVerifiéRole(ctx)
    await member.remove_roles(verifiérole)
    await ctx.send(f"{member.mention} n'est plus verifié !")  


@bot.command()
@commands.check(isOwner)
async def sayticket(ctx):
    embed = discord.Embed(title= "Ticket",description = "Bonjour,\nVous souhaitrez faire surveiller votre bot par ElwatchOnline?\nOu vous avez une question?\nOu une autre demande? C'est simple... il vous suffit tout simplement de faire la commande e!ticket dans un salon.\n\nOn est impatient de vous aidez 👀", color= 0xf1263f)
    message = await ctx.send(embed = embed)
    

@bot.command()
async def ticket(ctx, user: discord.Member=False):
    if ctx.guild.id == 881488037979250768:
        select = create_select(
        options=[
                create_select_option("Surveiller votre bot par Elwatch", value="1"),
                create_select_option("Question/Renseignement", value="2"),
                create_select_option("Autre demande...", value="3")
            ],
            placeholder="Veuillez sélectionner le type de votre demande.",
            min_values=1,
            max_values=1
        )
        fait_choix = await ctx.send("Liste Ticket", components=[create_actionrow(select)])

        def check(m):
            return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

        choice_ctx = await wait_for_component(bot, components=select, check=check)

        if choice_ctx.values[0] == "1":
            embed = discord.Embed(title= "Ticket",description = f"Bonjour,\nVous avez sélectionner l'option Surveiller votre bot par Elwatch... Merci de bien vouloir patienter un salon sera créer\n", color= blurple)
            await choice_ctx.send(embed = embed)
            category = await discord.utils.get(bot.guild.categories, id=881492021536251915)
            channel = await ctx.guild.create_text_channel('cool-channel', category = category)
        if choice_ctx.values[0] == "2":
            embed = discord.Embed(title= "Ticket",description = f"Bonjour,\nVous avez sélectionner l'option Question/Renseignement... Merci de bien vouloir patienter un salon sera créer\n", color= blurple)
            await choice_ctx.send(embed = embed)
        if choice_ctx.values[0] == "3":
            embed = discord.Embed(title= "Ticket",description = f"Bonjour,\nVous avez sélectionner l'option Autre.. Merci de bien vouloir patienter un salon sera créer\n", color= blurple)
            await choice_ctx.send(embed = embed)

@bot.command()
@commands.check(isOwner)
async def dm(ctx):
    user = await bot.fetch_user("727572859727380531")
    dm = await user.create_dm()
    await dm.send("Test Ticket 1")

@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Le ping pong c'est de la merde je préfère utiliser des briques comme raquettes mais en tout cas j'ai {round(bot.latency * 1000)}ms (PY)")
    
@bot.command()
@commands.check(isOwner)
async def channel(ctx):
    channel = await ctx.guild.create_text_channel('cool-channel')


#bouton

@bot.command()
async def choix(ctx):
    buttons = [
        create_button(
            style=ButtonStyle.blue,
            label="Choisissez moi",
            custom_id="oui"
        ),
        create_button(
            style=ButtonStyle.danger,
            label="SURTOUT PAS MOI!!!",
            custom_id="non"
        )
    ]
    action_row = create_actionrow(*buttons)
    fait_choix = await ctx.send("Faites votre choix !", components=[action_row])

    def check(m):
        return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    button_ctx = await wait_for_component(bot, components=action_row, check=check)
    if button_ctx.custom_id == "oui":
        await button_ctx.edit_origin(content="Bon toutou !")
    if button_ctx.custom_id == "non":
        await button_ctx.edit_origin(content="T'es vraiment con toi")




#slash

@slash.slash(name="number", description="Choisi un nombre au hasard pour toi.", options=[
    create_option(name="limite_inferieure", description="Le nombre le plus bas.", option_type=4, required= True),
    create_option(name="limite_superieure", description="Le nombre le plus haut.", option_type=4, required= True)

])
async def number(ctx, limite_inferieure, limite_superieure):
     await ctx.send("Le nombre choisi par moi même est...")
     await asyncio.sleep(1)
     await ctx.send("Roulement de tambours")
     await asyncio.sleep(2)
     await ctx.send("🥁 taratatatatatatatatatatatatatatatatata 🥁")
     await asyncio.sleep(1)
     num = random.randint(limite_inferieure, limite_superieure)
     await ctx.send(f"**{num}**")

@slash.slash(name="infoserver", description="Pour connaitre les informations sur ce serveur")
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


@slash.slash(name="infoserver2", description="Pour connaitre les informations sur ce serveur (Partie 2)")
async def infoserver2(ctx):
    server = ctx.guild
    serverIcon = server.icon_url
    serverName = server.name
    serverListRole = [r.mention for r in server.roles]
    embed = discord.Embed(title = "Commande infoserver suite", description = f"Partie 2 : Information sur le serveur **{serverName}**", color=0x00ffff)
    embed.set_thumbnail(url = serverIcon)
    embed.add_field(name='Liste des rôles :', value=", ".join(serverListRole))    
    await ctx.send(embed = embed)



@slash.slash(name="heberger", description="Pour savoir où est hebergé le code PY")
async def heberger(ctx):
 message = ("Le code python est en ce moment hébergé sur la freebox de Elie (c'est pas une blague)")
 await ctx.send(message)

@slash.slash(name="funfact", description="Pour connaitre une anecdote sur elbot et sa création.")
async def funfact(ctx):
 await ctx.send(random.choice(funFact))


async def getVerifiéRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "👤 Membre 👤":
            return role








 #JAVASCRIPT 

@bot.command()
async def pessi(ctx):
    await ctx.send("")

@bot.command()
async def uno(ctx):
    await ctx.send("")

@bot.command()
async def sondage(ctx):
    await ctx.send("")


@bot.command()
async def restart(ctx):
    await ctx.send("")


@bot.command()
async def clear(ctx):
    await ctx.send("")

@bot.command()
async def invite(ctx):
    await ctx.send("")

@bot.command()
async def github(ctx):
    await ctx.send("")


@bot.command()
async def help(ctx):
    await ctx.send("")


@bot.command()
async def play(ctx):
    await ctx.send("")

@bot.command()
async def stop(ctx):
    await ctx.send("")

@bot.command()
async def brique(ctx):
    await ctx.send("")
@bot.command()
async def rickdetect(ctx):
    await ctx.send("")



bot.run("token")
