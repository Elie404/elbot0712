from operator import and_, ifloordiv, is_not
import operator
from typing import Text, Tuple
import os
from os import *
from asyncio.futures import _FINISHED
import discord
import io, base64
import json
from discord import channel
import auth
from discord import user
from discord import member
from discord.webhook import Webhook, RequestsWebhookAdapter
from discord import ActionRow, Button, ButtonStyle
from discord import message
from discord.channel import CategoryChannel
from discord.ext import commands, tasks
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import bot_has_permissions, check
from discord.user import User
from discord_slash import ButtonStyle , SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import *
import asyncio
import chalk
from datetime import date
import random
from discord.ext.commands.errors import BotMissingPermissions, BotMissingRole
from discord.utils import get
from discord_slash.utils.manage_commands import create_option, create_choice
import requests
from urllib import parse
from discord import FFmpegPCMAudio
from discord import TextChannel
from requests.api import options
from six import text_type
import youtube_dl
import tweepy

intents = discord.Intents().default()
intents.members = True

bot = commands.Bot(command_prefix = "e!", description = "Tutititutu mais en Python", intents=intents)
slash = SlashCommand(bot, sync_commands=True)
musics = {} 
ytdl = youtube_dl.YoutubeDL()


# Supabase
from supabase import create_client, Client

supabase: Client = create_client(auth.supabase_url, auth.supabase_password)


funFact = ["Elbot était créer de base pour diffuser seulement le tutitititutu sur un Channel du serveur Ubuntu le best",
"Elbot a été créer le jeudi 11 février 2021, 09:47:42", 
"Le saviez-vous, il existe un bot by elbot qui permet de réveiller les projets glitch pour que vos bots soi H24 allumé",
"Le créateur de elbot est el2zay",
"Un prochain bot sous le nom de elwatch online, permettera de surveiller vos bots H24, gratuitement. (il sera codé et mis en ligne prochainement)",
"Elbot est open source. Pour voir son code faites la commande e!github.",
"Le saviez-vous? Elbot a été abondoné quelques semaines, plus tard puis el2zay a commencé à le coder grâce à scratch (oui, oui) puis c'est mis au vrai code.",
"Le saviez-vous? Johan et un peu Azrod ont poussé el2zay à me coder.",
"Elbot est toujours en cours de développement et à chaque semaine des mise à jours.",
"Je suis héberger sur la Freebox Delta de el2zay."]

status = ["Chante tutititutu tout en changeant pour Ubuntu",
"https://el2zay.is-a.dev/elbot",
"Entrain d'être coder en Python",
"Le code est désormais en full Python 🐍👀",
"Les commandes slash sont entrain d'être coder.",
":S"]

pessilist = "culotté\npleure\nchiale\nchouine\ncouine\naboie\nmiaule\nboude\nbrûle\nhurle\ncrie\ncrève\npleurniche\nricane\njacasse\nagonise\nbeugle\nchuchote\nmurmure\nronfle\nsuffoque\nimplose\nexplose\nrugis\nsiffle\nronronne\ncaquette\nrenifle\nvis\nroucoule\nsouffre\nsoufle\ndort"

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

elbot = 809344905674489866

def isOwner(ctx):
 return ctx.message.author.id == 727572859727380531


def elWatchServ(ctx):
 return ctx.guild.id == 881488037979250768

def johan(ctx):
 return ctx.message.author.id == 277825082334773251


#Fin reactroles

@bot.event
async def on_ready():
    print(chalk.green (f"Le code Python est allumé ! {bot.user.name}"))
    changeStatus.start()
@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.idle, activity = game)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(title="Commande inexistante", description="Cette commande n'existe pas. Vérifiez que vous n'avez pas fait d'erreur de frappe. Sinon vous pouvez consultez la page d'aide https://el2zay.is-a.dev/elbot/ ", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        embed.set_footer(text="`e!contact` si vous avez un problème")
        await ctx.message.reply(embed=embed)
        print(chalk.red(f"ERREUR: La commande {ctx.message.content} qui a été faite par {ctx.author} sur le serveur {ctx.guild.name} n'existe pas !"))

    elif isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Erreur", description="Un argument manque (nombre, mot/lettres etc...)\nMerci de réessayer avec un argument.\nCode Erreur :  Erreur N°1", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        embed.set_footer(text="`e!contact` si vous avez un problème")
        await ctx.message.reply(embed=embed)
        print(chalk.red(f"ERREUR: La commande {ctx.message.content} faite par {ctx.author.name} sur le serveur {ctx.guild.name} manquait un argument"))

    elif isinstance(error, commands.ChannelNotReadable):
        embed=discord.Embed(title="Erreur", description="Vous n'êtes pas dans un salon pour jouer la musique", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        embed.set_footer(text="`e!contact` si vous avez un problème")

        await ctx.message.reply(embed=embed)
        print(chalk.red(f"ERREUR: La commande {ctx.message.content} faite par {ctx.author.name} sur le serveur {ctx.guild.name} manquait un argument"))
    elif isinstance(error, commands.MissingPermissions):
        embed=discord.Embed(title="Erreur", description="Vous n'avez pas les permissions requises. Demandez à un administrateur ou au fondateur du serveur.\nCode Erreur : Erreur N°2", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        embed.set_footer(text="`e!contact` si vous avez un problème")
        await ctx.message.reply(embed=embed)
        print(chalk.red(f"ERREUR: {ctx.author.name} a fait la commande {ctx.message.content} qu'il n'avait pas l'autorisation de faire sur le serveur {ctx.guild.name} !"))

    elif isinstance(error, discord.Forbidden):
        embed=discord.Embed(title="Erreur", description="Je n'ai pas l'autorisation pour faire cette commande. \nEssayez de vérifier les paramètres des rôles sur le serveur.\nCode erreur : Erreur N°3", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        embed.set_footer(text="`e!contact` si vous avez un problème")
        await ctx.message.reply(embed=embed)
        print(chalk.red(f"ERREUR: {ctx.author.name} a fait la commande {ctx.message.content} sur le serveur {ctx.guild.name} où je n'avais pas l'autorisation de la faire."))
    
    else:
        embed=discord.Embed(title="Erreur console ", description=f"Erreur de la console: `{error}` ", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        embed.set_footer(text="`e!contact` si vous avez un problème")
        await ctx.reply(embed = embed)
        print(chalk.red(error))

#Message
@bot.listen()
async def on_message(message):
    if message.content.lower()=="c'est pas possible" and message.author.id != 882167050536120340 and message.author.id != elbot and (await checkIfMsgIsDisabled(message.guild.id, 'cpp') == True):
        await message.reply("Mais si c'est possible avec la CARTE **KIWI**")
    if message.content == ":)" or message.content == ":(":
        await message.reply (":S")
    if message.content.startswith("bon") and message.author.id != 882167050536120340 and message.author.id != elbot and message.content != "BONBON 🍬" and (await checkIfMsgIsDisabled(message.guild.id, 'cpp') == True):
        await message.reply("BONBON 🍬")
    #Suisse
    if message.content.lower()=="je suis suisse" and message.author.id != "809344905674489866" and message.content != "Je suis suisse et je suis polie" and message.content != "Je suis suisse et j'ai les moyens" and message.content != "Je suis suisse mais suis-je sexy?":
        await message.reply("Mais quelle heure est il?")
    if (message.content.lower()== "moi je sais"):
          await message.reply("C'est propre ici, non?")
    if (message.content.lower() == "bah oui"):
        await message.reply("Et l'or des nazis?")
    if (message.content.lower() == "steuplait"):
        await message.reply("SUISSE \n AHAHAHAHA")
    if (message.content.lower() == "je suis suisse et je suis polie"):
        await message.reply("C'est bien")
    if (message.content.lower() == "je suis suisse et j'ai les moyens"):
          await message.reply("Youpi")
    if (message.content.lower() == "je suis suisse mais suis-je sexy ?"):
          await message.reply("Euh oui mais surtout gentil...")
    #Fin de suisse

    if message.content == "BONBON 🍬" and message.author.id != 882167050536120340 and message.author.id != elbot:
        await message.add_reaction("❤️")

    if (message.content.lower() == "oof"): await message.add_reaction(":oof:922051930992304159")

    #Lower case


    lowerMessage = message.content.lower()
    if lowerMessage.find("ubuntu") != -1:
        await message.add_reaction(":ubuntu:922047121534906430") #maj
        await message.add_reaction(":ubuntudansbassine:922047737153855550") #maj

    lowerMessage = message.content.lower()
    if lowerMessage.find("linux c'est de la merde") != -1 or lowerMessage.find("ubuntu c'est de la merde") != -1 and message.author.id != 882167050536120340 and message.author.id != elbot:
        if(await checkIfMsgIsDisabled(message.guild.id, 'linuxmerde') == True) and message.author.id != 882167050536120340 and message.author.id != elbot:
            await message.reply("Regarde cette vidéo et on verra. \n https://www.youtube.com/watch?v=jdUXfsMTv7o")

    lowerMessage = message.content.lower()
    if lowerMessage.find("jannot gaming") != -1 and (await checkIfMsgIsDisabled(message.guild.id, 'jannotgaming') == True) and message.author.id != 882167050536120340 and message.author.id != elbot:
        await message.reply("https://tenor.com/view/potatoz-jano-gaming-nowagifs-gif-18818348")

    lowerMessage = message.content.lower()
    if lowerMessage.find("merde") != -1 and message.author.id != 882167050536120340 and message.author.id != elbot:
        await message.add_reaction("💩")
        await message.add_reaction(":bassinechrotte:922048937995677697") #maj
    lowerMessage = message.content.lower()
    if lowerMessage.find("crotte") != -1:
        await message.add_reaction("💩")
        await message.add_reaction(":bassinechrotte:922048937995677697")#maj
    if lowerMessage.find("caca") != -1:
        await message.add_reaction("💩")
        await message.add_reaction(":bassinechrotte:922048937995677697")#maj
    if lowerMessage.find("chrotte") != -1:
        await message.add_reaction("💩")
        await message.add_reaction(":bassinechrotte:922048937995677697")#maj

    lowerMessage = message.content.lower()
    if lowerMessage.find("poubelle") != -1:
        await message.add_reaction("🚮")

    lowerMessage = message.content.lower() 
    if lowerMessage.find("tutititutu") != -1 and message.author.id != 882167050536120340 and message.author.id != elbot:
        await message.add_reaction(":briquetelecom:922049674305740862") #maj
        if (await checkIfMsgIsDisabled(message.guild.id, 'tutititutu') == True) and message.author.id != 882167050536120340 and message.author.id != elbot:
            await message.reply("https://cdn.discordapp.com/emojis/816728856823201813.png?v=1")

    lowerMessage = message.content.lower()
    if lowerMessage.find("avira") != -1:
        await message.add_reaction(":avira:922050319557480481")

    lowerMessage = message.content.lower()
    if lowerMessage.find("changez pour stickman") != -1 and (await checkIfMsgIsDisabled(message.guild.id, 'changezstickman') == True and message.author.id != 882167050536120340 and message.author.id != elbot):
        await message.reply("*Mangez des stickman")

    lowerMessage = message.content.lower()
    if lowerMessage.find("apple") != -1 and message.author.id != 882167050536120340 and message.author.id != elbot:
        await message.reply(" https://tenor.com/view/lisa-simpsons-think-differently-gif-10459041")
        await message.add_reaction("🍎")

    if message.content==":S" and message.author.id != 809344905674489866:
        await message.add_reaction("❤️")
    lowerMessage = message.content.lower()
    if lowerMessage.find("baldi") != -1:
        await message.add_reaction(":baldi:922051105582628864") #maj

    lowerMessage = message.content.lower()
    if lowerMessage.find("total") != -1:
        await message.add_reaction(":total:922051358985707590") #maj

    lowerMessage = message.content.lower()
    if lowerMessage.find("scratch") != -1 and (await checkIfMsgIsDisabled(message.guild.id, 'scratch') == True)and message.author.id != 882167050536120340 and message.author.id != elbot:
        await message.reply("Chat de merde")

    lowerMessage = message.content.lower()
    if lowerMessage.find("bonjoir") != -1 and (await checkIfMsgIsDisabled(message.guild.id, 'bonjoir') == True)and message.author.id != 882167050536120340 and message.author.id != elbot:
        await message.reply("Hachoir")

        lowerMessage = message.content.lower()
    if lowerMessage.find("courgette") != -1 and (await checkIfMsgIsDisabled(message.guild.id, 'courgette') == True)and message.author.id != 882167050536120340 and message.author.id != elbot:
        await message.reply("Counnasse")

        lowerMessage = message.content.lower()
    if lowerMessage.find("ouille") != -1 and (await checkIfMsgIsDisabled(message.guild.id, 'ouille') == True)and message.author.id != 882167050536120340 and message.author.id != elbot:
        await message.reply("https://pbs.twimg.com/media/ETkK977X0AE3x-x.jpg")



#Fin Message

@bot.command(aliases=['serverinfo']) #SLASH OK Site ok
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
async def infoserver2(ctx): #site ok
    server = ctx.guild
    serverIcon = server.icon_url
    serverName = server.name
    serverListRole = [r.mention for r in server.roles]
    embed = discord.Embed(title = "Commande infoserver suite", description = f"Partie 2 : Information sur le serveur **{serverName}**", color=0x00ffff)
    embed.set_thumbnail(url = serverIcon)
    embed.add_field(name='Liste des rôles :', value=", ".join(serverListRole))    
    await ctx.send(embed = embed)

@bot.command(aliases=['infouser','avatar'])
async def userinfo(ctx, *, member: discord.Member=None): #site ok
    if not member:
        member = ctx.message.author
    username = member.name
    userID = member.id
    usercreation = member.created_at.strftime("%d/%m/%Y à %H:%M")
    rolelist = [r.mention for r in member.roles if r != ctx.guild.default_role]
    userjoin = member.joined_at.strftime("%d/%m/%Y à %H:%M")
    embed=discord.Embed(title=f'**Voici les infos de {username} !**', color=0x00ff00)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nom d'utilisateur :", value=member, inline=False)
    embed.add_field(name="ID :", value=userID, inline=False)
    embed.add_field(name="Date de création :", value=usercreation, inline=False)
    embed.add_field(name="Date d'arrivée :", value=userjoin, inline=False)
    embed.add_field(name="Rôle(s) :", value=", ".join(rolelist), inline=False)
    await ctx.message.reply(embed=embed)

    
@bot.command() #ok site ok 
async def heberger(ctx):
    # Obtenir le nom de la plateforme
    platform = os.name
    # Si la plateforme est linux
    if platform == 'linux':
        await ctx.reply("Le code python est en ce moment hébergé sur la freebox de Elie (c'est pas une blague)")
    #Si la plateforme est mac
    if platform == "darwin" or "macOS" or "mac" or 'macintosh': 
        await ctx.reply("Le code python est en ce moment hébergé sur le macbook d'Elie")
    else:
        await ctx.reply("OS inconnu.")




@bot.command() #fait en slash
async def funfact(ctx):#site ok
 await ctx.send(random.choice(funFact))

@bot.command()
async def count(ctx, *texte): #site ok
    texte = " ".join(texte)
    a = len(texte)
    await ctx.reply(f"{texte} contient {a} caractères")


@bot.command()
async def embed(ctx, *,args): #site ok
    if args.split("§")[3].lower() != "blurple" and args.split("§")[3].lower() != "red" and args.split("§")[3].lower() != "rouge" and args.split("§")[3].lower() != "blue" and args.split("§")[3].lower() != "bleu" and  args.split("§")[3].lower() != "twitter" and args.split("§")[3].lower() != "cyan" and args.split("§")[3].lower() != "turquoise" and args.split("§")[3].lower() != "corail" and args.split("§")[3].lower() != "lime" and args.split("§")[3].lower() != "citron" and args.split("§")[3].lower() != "green" and args.split("§")[3].lower() != "vert" and args.split("§")[3].lower() != "yellow" and args.split("§")[3].lower() != "jaune" and args.split("§")[3].lower() != "black" and args.split("§")[3].lower() != "noir" and args.split("§")[3].lower() != "grey" and args.split("§")[3].lower() != "gris" and args.split("§")[3].lower() != "brown" and args.split("§")[3].lower() != "marron" and args.split("§")[3].lower() != "orange":
        embed=discord.Embed(title="Couleur inexistante", description=f"Cette couleur n'existe pas. Vérifiez que vous n'avez pas fait d'erreur de frappe. Sinon n'hésitez pas à faire la commande e!list_color ou à consulter la page d'aide.https://el2zay.is-a.dev/elbot/", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        await ctx.reply(embed=embed)
        print(chalk.red(f"ERREUR: La couleur choisie par {ctx.author} sur le serveur {ctx.guild.name} n'existe pas !"))
        return
    elif "blurple" in args.split("§")[3].lower():
        color = blurple
    elif "red"in args.split("§")[3].lower():
        color = red
    elif "rouge"in args.split("§")[3].lower():
        color = red
    elif "blue"in args.split("§")[3].lower():
        color = blue
    elif "bleu"in args.split("§")[3].lower():
        color = blue
    elif "twitter" in args.split("§")[3].lower():
        color = 0x2986cc
    elif "cyan"in args.split("§")[3].lower():
        color = cyan
    elif "turquoise"in args.split("§")[3].lower():
        color = cyan
    elif "corail" in args.split("§")[3].lower():
        color = corail
    elif "lime" in args.split("§")[3].lower():
        color = 0x00ff23
    elif "citron" in args.split("§")[3].lower():
        color = 0x00ff23
    elif "green"in args.split("§")[3].lower():
        color = 0x008000
    elif "vert"in args.split("§")[3].lower():
        color = 0x008000
    elif "yellow" in args.split("§")[3].lower():
        color = 0xffff00
    elif "jaune" in args.split("§")[3].lower():
        color = 0xffff00
    elif "black" in args.split("§")[3].lower():
        color = 0x000000
    elif "noir" in args.split("§")[3].lower():
        color = 0x000000
    elif "grey" in args.split("§")[3].lower():
        color = 0x808080
    elif "gris" in args.split("§")[3].lower():
        color = 0x808080
    elif "brown" in args.split("§")[3].lower():
        color = 0x660000
    elif "marron" in args.split("§")[3].lower():
        color = 0x660000
    elif "orange" in args.split("§")[3].lower():
        color = 0xffa500
    
    embed = discord.Embed(title = args.split("§")[0], description = args.split("§")[1], color = color)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url) #url = "lien" 
    embed.set_footer(text = args.split("§")[2])
    await ctx.send (embed = embed)
    

@bot.command() #site ok
async def list_color(ctx):
    embed = discord.Embed(title = "Liste des couleurs embed", description = "blurple\nred/rouge\nblue/bleu\ntwitter\ncyan/turquoise\ncorail\nlime/citron\ngreen-vert\nyellow-jaune\nblack/noir\ngrey/gris\nbrown/marron\norange\n\nLa couleur que vous soihaitez n'est pas disponible? Pas de panique faites la commande e!contact et dites la couleur que vous voulez que j'ajoute.\nVous serez prévenu quand elle sera ajoutée.", color = cyan)
    await ctx.reply(embed = embed)


@bot.command() #site ok
async def say(ctx, *texte):
    if not texte:
        await ctx.send("T'es con ou quoi? DIS UN MOT FRÈRE")
    if ctx.author.id != 727572859727380531:
        texte = " ".join(texte)
        texte = texte.replace("@everyone", "everyone")
        texte = texte.replace("@here", "here")
        texte = texte.replace("chromebook","chrottebook")
        texte = texte.replace("stickman","stickmerde")
        texte = texte.replace("rmxbot","Merde inutile")
        texte = texte.replace("AC","MEE6")
        texte = texte.replace("Anti Coupable","MEE6")
        texte = texte.replace("el2zay","maître bien-aimé")
        texte = texte.replace("elie","Ô grand maitre bien aimé")
        texte = texte.replace("Elie","Ô grand maitre bien aimé")
        texte = texte.replace("pute","Ta mère")
        texte = texte.replace("Pute","Ta mère")
        texte = texte.replace(":(",":S")
        texte = texte.replace(":)",":S")
        await ctx.message.delete()
        await ctx.send(texte)
    if ctx.author.id == 727572859727380531:
        texte = " ".join(texte)
        await ctx.message.delete()
        await ctx.send(texte)

@bot.command()
async def sondage(ctx, *, texte = None): #site ok
    if texte is None:
        texte = "."
        texte = " ".join(texte)
    embed = discord.Embed(title = f"Sondage de {ctx.message.author} ", description = f"{texte}", color=red)
    message = await ctx.send(embed = embed)
    await ctx.message.delete()
    await message.add_reaction("👍")
    await message.add_reaction("👎")
    await message.add_reaction("❌")



@bot.command(pass_context = True)
async def contact(ctx, *text): #site ok
    user = bot.get_user(727572859727380531)
    await user.send(f"{ctx.author} vous a dit sur le serveur {ctx.guild.name} \n" + (" ".join (text)))

@bot.command(pass_context = True)
async def dm(id : int, *text): #site ok
    user = bot.get_user(id)
    await user.send(" ".join(text))


@bot.command() #site ok
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


#Commande musique

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@bot.command(aliases=['stop']) #site ok 
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []
    await ctx.reply("J'ai arrêté la musique et quitté le salon vocal ⏹")

@bot.command()
async def resume(ctx): #site ok
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()
    await ctx.reply("Je reprend la musique ⏯")


@bot.command()
async def pause(ctx): #site ok
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()
    await ctx.reply("La musique est en pause ⏸")


@bot.command()
async def skip(ctx): #site ok
    client = ctx.guild.voice_client
    client.stop()
    await ctx.reply("J'ai passé la musique ⏭")

loopGuild = []
@bot.command() 
async def loop(ctx): #site ok
    if ctx.guild in loopGuild:
        loopGuild.remove(ctx.guild)
        await ctx.reply("La musique n'est plus en boucle 🔁")
    else:
        loopGuild.append(ctx.guild)
        await ctx.reply("La musique est maintenant en boucle 🔁")


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            if(client.guild in loopGuild):
                play_song(client, queue, song)
            else:
                asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url): #site ok
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Je joue : {video.url} ▶️")
        play_song(client, musics[ctx.guild], video)

@bot.command()
async def brique(ctx):
    # Fonction pour lancer une musique
    async def startMusic(ctx,vc):
        channel = ctx.author.voice.channel
        video = Video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        musics[ctx.guild] = []
        client = await channel.connect()
        play_song(client, musics[ctx.guild], video)

        # Une fois que la musique commence à se jouer, envoyer un message
        await ctx.send(f"{ctx.author.mention} je joue la musique !")

        # Une fois la musique terminé, la recommencer
        vc.on('end', lambda: startMusic())

    # Vérifier si l'auteur du message est dans un salon vocal
    if(ctx.message.author.voice is None):
        return await ctx.send(f"{ctx.message.author.mention}, vous devez être dans un salon vocal pour jouer la musique !")

    # Envoyer un message pour dire que la musique va se lancer.. 
    await ctx.send(f"Lancement de Tutititutu 🧱")

    # Charger la musique dans le salon vocal
    vc = await ctx.author.voice.channel.connect()
    startMusic(ctx,vc)

#fin commande musique

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *, reason = None): #site ok
    if reason is None:
        reason = "aucune raison"
        reason = "".join(reason)
    await ctx.guild.kick(user, reason = reason) 
    embed = discord.Embed(title = "Kick", description = "Un modérateur a frappé !", color=0xff2812)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url) #url = "lien" 
    embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/795288700594290698/879044070255759410/pngaaa.com-1429166.png")
    embed.add_field(name = "Membre kick", value= user.name, inline = True)
    embed.add_field(name = "Raison", value = reason, inline = True)
    embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
    await ctx.send(embed = embed)
    embed = discord.Embed(title = "Bannissement", description = f"Un modérateur a frappé !\nVous avez été banni par {ctx.author.name} pour la raison {reason}", color=0xff2812)
    await user.send(embed = embed)


@bot.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx): #site ok
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(title = "Lock", description = f"Le salon, {ctx.message.channel} est désormais verouillé 🔒", color=0x0000ff)
    await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_channels = True)
async def unlock(ctx): #site ok
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(title = "Unlock", description = f"Le salon, {ctx.message.channel} est désormais déverouillé 🔓", color=0x0000ff)
    await ctx.send(embed = embed)


	
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *, reason = None): #site ok
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
    user = bot.get_user(user.id)
    await user.send('https://tenor.com/view/blob-banned-ban-hammer-blob-ban-emoji-gif-16021044')
    embed = discord.Embed(title = "Bannissement", description = f"Un modérateur a frappé !\nVous avez été banni par {ctx.author.name} pour la raison {reason}", color=0xff2812)
    await user.send(embed = embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user, *reason): #site ok
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
 


#Jeux

@bot.command()
async def roulette(ctx): #site ok 
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
async def pfc(ctx, texte : str): #site ok
    if texte != "pierre" and texte != "p" and texte != "feuille" and texte != "f" and texte != "ciseaux" and texte != "ciseau" and texte != "c" and texte !="puit" and texte !="puits":
        await ctx.reply("T'es con? (combre)")
    pfclist = ["pierre","feuille","ciseaux"]
    
    if texte == "pierre" or texte == "p":
        reponse = random.choice(pfclist)
        if reponse == "feuille":
            await ctx.reply(f"J'ai gagné j'ai choisi {reponse} :S")
        elif reponse == "pierre": 
            await ctx.reply(f"Égalité j'ai choisi {reponse}")
        elif reponse == "ciseaux":
            await ctx.reply(f"Onon tu as gagné j'ai choisi {reponse} :(")

    elif texte == "feuille" or texte == "f":
        reponse = random.choice(pfclist)
        if reponse == "ciseaux":
            await ctx.reply(f"J'ai gagné j'ai choisi ciseaux :S")
        elif reponse == "feuille":
            await ctx.reply(f"Égalité j'ai choisi feuille")
        elif reponse == "pierre":
            await ctx.reply(f"Onon tu as gagné j'ai choisi pierre :(")

    elif texte == "ciseaux" or texte == "ciseau" or texte == "c":
        reponse = random.choice(pfclist)
        if reponse == "feuille":
            await ctx.reply(f"Onon tu as gagné j'ai choisi {reponse} :(")
        elif reponse == "pierre":
            await ctx.reply(f"J'ai gagné j'ai choisi {reponse} :S")
        elif reponse == "ciseaux":
            await ctx.reply(f"Égalité j'ai choisi {reponse}")

    elif texte == "puit" or texte == "puits":
        await ctx.reply("Mais ptn c'est mathématique, les ciseaux ils coupent la feuille, la feuille elle recouvre la pierre, la pierre elle éclate les ciseaux, qu'est ce qui ce passe si tu mets un putain de puits. Les ciseaux ils tombent dedans, la pierre elle tombe dedans, donc statistiquement t'as plus de chances de gagner avec le puits qu'est ce qui va se passer?! On va tous les deux faire le puits! Ça va devenir le jeu du puits. Puits puits puits puits, oh qu'elle suprise t'as fait un puits aussi fils de pute on est encore à égalité. Bravo.")


@bot.command()
async def qi(ctx, *,member : discord.Member=None): #site ok
    if not member:
        member = ctx.message.author
    limite_inferieure=60
    limite_superieure=250
    num = random.randint(limite_inferieure, limite_superieure)
    if num > 59 and num < 81:
        await ctx.reply(f"Le qi de {member} est de {num} AHAHAHA T CON PUTAIN")
    if num > 80 and num < 95:
        await ctx.reply(f"Le qi de {member} est de {num} t'es un peu con mais trkl")
    if num > 94 and num < 116:
        await ctx.reply(f"Le qi de {member} est de {num}, ça va t'es normal")
    if num > 115 and num < 131:
        await ctx.reply(f"Le qi de {member} est de {num}, Oooooh c'est pas mal en vrai")
    if num > 129 and num < 151:
        await ctx.reply(f"Le qi de {member} est de {num}, T'es vraiment intelligent")
    if num > 149 and num < 160:
        await ctx.reply(f"Le qi de {member} est de {num}, Preque-Génie")
    if num > 159 and num < 171:
        await ctx.reply(f"Le qi de {member} est de {num}, Steve Jobs, Bill Gates, Einstein")
    if num > 170 and num < 225:
        await ctx.reply(f"Le qi de {member} est de {num}, T'ES PLUS INTELLIGENT QUE STEVE JOBS, BILL GATES ET MÊME DE EINSTEIN")
    if num == 225:
        await ctx.reply(f"Le qi de {member} est de {num}, T'ES AUSSI INTELLIGENT QUE TERENCE TAO aka le mec le plus intelligent au monde")
    if num > 225:
        await ctx.reply(f"Le qi de {member} est de {num}, t'es le mec le plus intelligent gg")

#Fin jeux

@bot.command()
async def cuisiner(ctx): #site ok
    await ctx.send ("Envoyez le plat que vous voulez cuisiner")

    def checkMessage(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel
    
    try:
       recette = await bot.wait_for("message", timeout = 10, check = checkMessage)
    except:
        embed=discord.Embed(title="Erreur: TIMEOUUUUUUUUT", description="Cela fait plus de 10 secondes que la commade a été lancé et que vous n'avez pas répondu à cette commande. \nVous pouvez réessayer en recommençant la commande.\n Erreur N°5 ", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
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
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        await ctx.message.reply(embed=embed)


@bot.command(aliases=['code'])
async def github(ctx): #site ok
    buttons = [
        create_button(url='https://github.com/el2zay/elbot',
                label="Github",
                style=ButtonStyle.URL,
        ),
        create_button(url='https://el2zay.is-a.dev/elbot',
                label="Site",
                style=ButtonStyle.URL,
        )
        ]
    action_row = create_actionrow(*buttons)
    fait_choix = await ctx.send("Voici le Github et le site", components=[action_row])


@bot.command() #site ok
async def pessi(ctx):
    embed = discord.Embed(title= "LES MOTS DES PESSI",description=(pessilist) ,color = blurple)
    await ctx.reply(embed = embed)
    

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
@commands.has_permissions(manage_messages = True) 
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"): #site ok
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été mute !")


@bot.command()
@commands.has_permissions(manage_messages = True)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"): #site ok
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute !")
 

async def getVerifiéRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "👤 Membre 👤":
            return role

@bot.command()
@commands.check(isOwner)
async def stop_bot(ctx):
    await ctx.send("⚡️ D'accord je m'éteins ! ⚡️")
    await bot.logout()
    os.kill(os.getpid())
    os.kill(os.getpid())

@bot.command()
@commands.check(isOwner)
async def verified(ctx, member : discord.Member):
    verifiérole = await getVerifiéRole(ctx)
    await member.add_roles(verifiérole)
    await ctx.send(f"{member.mention} a été vérifié !")


@bot.command()
@commands.check(isOwner)
async def verify(ctx):
    message = await ctx.send(f"> Bienvenue à vous sur le serveur **{ctx.guild.name}**\n> \n> Vous devez lire les règles pour avoir un accès complet au serveur.\n> **Règle N°1**: Surveillez votre language, interdiction aux insultes et mot innaproprié qui pourraient blessé des personnes. Cependant les mots du style merde, putain... sont autorisés mais doivent être utilisés avec modération. \n> **Règles N°2** Interdiction de everyone\n> **Règles N°3** Vous avez totalement le droit de mentionner les fondateurs sans abus pour par exemple une relance au cas où nous avons oublié de rajouter votre bot (PS: Promis ça sera très rare)\n> **Règle N°4** Vous devez avoir un pseudo sans caractères illisibles afin de vous mentionner facilement. Si vous en avez un votre pseudo sera modifié.\n> **Règles N°5** On essayera de rendre aussi ce serveur communautaire et pas seulement pour la surveillance de bot donc si vous le souhaitiez vous pouvez parler dans le général de ce serveur.\n> Des question? Vous pourrez trouver plusieurs réponses dans le prochain salon ou sinon vous pouvez demander au staff ou aux fondateurs.\n \n Tout est ok pour vous? Parfait. Vous pouvez appuyer sur la réaction ✅")
    await message.add_reaction("✅")
    reaction, user = await bot.wait_for("reaction_add")       
    if reaction.emoji == "✅":
        await ctx.send("La recette a démarré")
@bot.command()
@commands.check(isOwner)
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
async def ticket(ctx, user: discord.Member=False): #site ok
    if ctx.guild.id != 881488037979250768:
        embed=discord.Embed(title="Erreur", description="Cette commande n'existe pas sur ce serveur.\nMerci de réessayer sur un serveur où la commande e!ticket est disponible.\nCode Erreur:  Erreur N°6", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        await ctx.message.reply(embed=embed)
    elif ctx.guild.id == 881488037979250768:
        select = create_select(
        options=[
                create_select_option("Surveiller votre bot", value="1"),
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
            # Obtenir la catégorie
            category = discord.utils.get(ctx.guild.categories, name='ticket')
            #permissions
            perms = { 'read_messages': True, 'send_messages': True, 'connect': True, 'speak': True }
            overwrites = {ctx.message.author: discord.PermissionOverwrite(**perms), 
    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
    ctx.guild.me: discord.PermissionOverwrite(read_messages=False)
}
            # Crée le salon
            channel = await ctx.guild.create_text_channel(name =  f"ticket-{ctx.message.author.name}-1", category = category, overwrites=overwrites)
            #Envoyer un message d'information dans le ticket
        embed=discord.Embed(title="Ticket \"Ajouter son bot\"", description="Merci de bien vouloir mettre ces informations pour éviter toute perte de temps.\n-Nom du bot\n-ID du bot\n-Lien d'invitation du bot **SANS** les autorisations admin.\n\nNous vous recontacterons dès que votre bot a été ajouter à la base de données.", color=0xff0000)
        await channel.send(embed = embed)
        #Envoyer un MP à el2zay 
        user = bot.get_user(727572859727380531)
        await user.send(f"{ctx.author} a envoyé une demande d'ajout de son bot.\nticket-{ctx.message.author.name}-1")

        if choice_ctx.values[0] == "2":
            embed = discord.Embed(title= "Ticket",description = f"Bonjour,\nVous avez sélectionner l'option Question/Renseignement... Merci de bien vouloir patienter un salon sera créer\n", color= blurple)
            await choice_ctx.send(embed = embed)
            # Obtenir la catégorie
            category = discord.utils.get(ctx.guild.categories, name='ticket')
            perms = { 'read_messages': True, 'send_messages': True, 'connect': True, 'speak': True }
            overwrites = {ctx.message.author: discord.PermissionOverwrite(**perms), 
    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
    ctx.guild.me: discord.PermissionOverwrite(read_messages=False)
}           
            #Créer le salon
            await ctx.guild.create_text_channel(name =  f"ticket-{ctx.message.author.name}-2", category = category, overwrites=overwrites)
            user = bot.get_user(727572859727380531)
            await user.send(f"{ctx.author} souhaite se renseigner ou a des questions.\nticket-{ctx.message.author.name}-2")
        if choice_ctx.values[0] == "3":
            embed = discord.Embed(title= "Ticket",description = f"Bonjour,\nVous avez sélectionner l'option Autre.. Merci de bien vouloir patienter un salon sera créer\n", color= blurple)
            await choice_ctx.send(embed = embed)
            # Obtenir la catégorie
            category = discord.utils.get(ctx.guild.categories, name='ticket')
            #permissions
            perms = { 'read_messages': True, 'send_messages': True, 'connect': True, 'speak': True }
            overwrites = {ctx.message.author: discord.PermissionOverwrite(**perms), 
    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
    ctx.guild.me: discord.PermissionOverwrite(read_messages=False)
}
            #Créer le salon
            await ctx.guild.create_text_channel(name =  f"ticket-{ctx.message.author.name}-3", category = category, overwrites=overwrites)
            user = bot.get_user(727572859727380531)
            await user.send(f"{ctx.author} a créé un ticket Autre\nticket-{ctx.message.author.name}-3")


@bot.command()
async def close(ctx): #site ok
    if ctx.guild.id == 881488037979250768 and ctx.channel.category_id == 901452596638789634:
        return await ctx.channel.delete()
    else:
        return await ctx.send(content=f"Ce salon n'est pas un ticket et ne peut être fermé")

    
@bot.command() 
async def reverse(ctx): #site ok
    await ctx.send("https://tenor.com/view/power-legendary-reverse-card-econowise-reverse-card-legendary-uno-reverse-card-uno-legendary-reverse-card-gif-23531292")


@bot.command()
async def ping(ctx): #site ok 
    await ctx.send(f"Le ping pong c'est de la merde je préfère utiliser des briques comme raquettes mais en tout cas j'ai {round(bot.latency * 1000)}ms (PY)")

@bot.command(aliases=['minuteur'])
async def timer(ctx, secondes : int): #site ok
    await ctx.reply(f"Votre minuteur de {secondes} secondes est lancé vous serez prévenu par MP lorsque le temps s'écoulera ⏲")
    await asyncio.sleep(secondes)
    user = bot.get_user(ctx.author.id)
    await user.send(f"Votre minuteur de {secondes} secondes est terminé! ⏲")


@bot.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, nombre : int): #site ok
    if (nombre == 1):
        await ctx.channel.purge(limit = nombre + 1) and await ctx.send(f"{ctx.author.name} a supprimé 1 message.")

    if (nombre > 1 and nombre and nombre < 20 or nombre == 20):
        await ctx.channel.purge(limit = nombre + 1) and await ctx.send(f"{ctx.author.name} a supprimé {nombre} messages.")
    if (nombre > 20):
        buttons = [
            create_button(
                style=ButtonStyle.blue,
                label="Oui",
                custom_id="oui"
                        ),
            create_button(
                style=ButtonStyle.danger,
                label="Non",
                custom_id="non"
            )
        ]
        action_row = create_actionrow(*buttons)
        fait_choix = await ctx.send(f"ATTENTION!!! Souhaites-tu vraiment clear {nombre} de message?", components=[action_row])

        def check(m):
            return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

        button_ctx = await wait_for_component(bot, components=action_row, check=check)
        if button_ctx.custom_id == "oui":
            await ctx.channel.purge(limit = nombre + 1)
        if button_ctx.custom_id == "non":
            await button_ctx.edit_origin(content="Aucun message n'a été clear.")

@bot.command()
async def help(ctx):
    select = create_select(
        options=[
            create_select_option("🤖 Commande de base 🤖", value="1"),
            create_select_option("🧠 Administration 🧠", value="2"),
            create_select_option("🎵 Musique 🎵", value="3"),
            create_select_option("💻 Database 💻", value="4"),
            create_select_option("🎮 Jeux 🎮", value="5"),
            create_select_option("👾 Autre 👾", value="6")
        ],
        placeholder="Veuillez sélectionner le type de votre demande.",
        min_values=1,
        max_values=1
    )
    fait_choix = await ctx.send("Commande help", components=[create_actionrow(select)])

    def check(m):
        return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    choice_ctx = await wait_for_component(bot, components=select, check=check)

    if choice_ctx.values[0] == "1":
        embed = discord.Embed(title= "🤖 Commande de base 🤖",description = f"", color= cyan)
        embed.add_field(name = "say <texte>", value= "Pour me faire dire tout et n'importe quoi\nAttention Vous ne pouvez pas mentionner @here/@everyone.", inline = True)
        embed.add_field(name = "chinese <texte>", value= "Pour me faire dire tout et n'importe quoi mais où les caractères sont transformés en caractères chinois.\nAttention Vous ne pouvez pas mentionner @here/@everyone.", inline = True)
        embed.add_field(name = "embed <titre>§<description>§<footer>§<couleur>", value = "Créer un embed à partir de elbot\ne!embed Ça c'est le titre§ça c'est la description§ça c'est le footer§et là, la couleur. (voir commande list_color)", inline = True)
        embed.add_field(name="list_color", value= "Connaitre les couleurs disponibles pour elbot\nSi vous souhaitez faire la proposition d'une couleur n'hésitez pas contacter el2zay à l'aide de la commande e!contact.", inline=True)
        embed.add_field(name = "ping", value= "Affiche le temps de latence du bot en ms.", inline = True)
        embed.add_field(name = "heberger", value= "Pour savoir sur quel hébergeur je suis héberger en ce moment !", inline = True)
        embed.add_field(name = "invite", value= "Donne un lien d'invitation pour inviter le bot sur votre serveur.", inline = True)
        embed.add_field(name = "contact <texte>", value = "Pour contacter le créateur du bot en cas de problème.", inline = True)	
        embed.add_field(name = "count <texte>", value = "Compter le nombre de caractères dans un mot ou une phrase.", inline = True)
        embed.add_field(name = "sondage <texte> (argument facultatif)", value = "Créer un sondage avec les choix \"oui\" et \"non\" grâce aux réactions.", inline = True)
        embed.add_field(name="infoserver/serverinfo", value= "Pour connaitre les informations importantes sur ce serveur", inline=True)
        embed.add_field(name = "infoserver2/serverinfo2", value = "Suite de la commande infoserver/serverinfo", inline = True)	
        embed.add_field(name = "infouser / avatar <user> (argument facultatif)", value = "Pour connaitre les informations sur un utilisateur", inline = True)	
        embed.set_footer(text="https://el2zay.is-a.dev/elbot")
        await choice_ctx.send(embed = embed)
    if choice_ctx.values[0] == "2":
        embed = discord.Embed(title= "🧠 Administration 🧠",description = f"", color=red)
        embed.add_field(name = "clear <nombre> ❌**COMMANDE AYANT DES PROBLÈMES**❌", value= "Pour clear le nombre de message que vous souhaitiez", inline = True)
        embed.add_field(name = "kick <membre>", value= "Pour expulser un membre sur un serveur.", inline = True)
        embed.add_field(name = "ban <membre>", value = "Pour bannir un membre sur un serveur", inline = True)
        embed.add_field(name = "unban <membre>", value= "Pour débannir un membre sur un serveur\n`e!unban el2zay#1234`", inline=True)
        embed.add_field(name = "lock", value= "Verouiller un salon.", inline = True)
        embed.add_field(name = "unlock", value= "Déverouiller un salon.", inline = True)
        embed.add_field(name = "mute <membre>", value = "Pour muter un membre du serveur.", inline = True)
        embed.add_field(name = "unmute <membre>", value= "Pour unmute un membre du serveur.", inline=True)
        embed.set_footer(text="https://el2zay.is-a.dev/elbot")
        await choice_ctx.send(embed = embed)
    if choice_ctx.values[0] == "3":
        embed = discord.Embed(title= "🎵 Musique 🎵",description = f"", color=red)
        embed.add_field(name = "play <lien>", value= "Joue de la musique grâce à un lien youtube", inline = True)
        embed.add_field(name = "stop", value = "Arrête la musique.", inline = True)
        embed.add_field(name = "pause", value= "Met en pause la musique.", inline = True)
        embed.add_field(name = "resume", value= "Reprend la musique.", inline=True)
        embed.add_field(name = "loop", value= "Lis la musique en boucle", inline = True)
        embed.add_field(name = "skip", value= "Passe la musique.", inline = True)
        embed.add_field(name = "brique", value = "**❌COMMANDE NON FONCTIONNELLE❌**. Pour que elbot chante tutititutu", inline = True)
        embed.set_footer(text="https://el2zay.is-a.dev/elbot")
        await choice_ctx.send(embed = embed)
    if choice_ctx.values[0] == "4":
        embed = discord.Embed(title= "💻 Database 💻",description = f"Les commandes database utilisent Supabase.", color=red)
        embed.add_field(name = "set_birthday / add_birthday <JJ mois AAAA> (AAAA est facultatif)", value= "Ajouter ou modifier la date de son anniversaire.\nVotre anniversaire est affiché sur tous les serveurs où vous êtes et où est Elbot. Pas besoin de mettre plein de fois son anniversaire sur plein de serveurs.C'est cool hein :S", inline = True)
        embed.add_field(name = "birthday <membre> (argument facultatif)", value= "Voir la liste des anniversaires. Vous pouvez aussi voir la liste d'un seul membre en le mentionnant.", inline = True)
        embed.set_footer(text="https://el2zay.is-a.dev/elbot")
        await choice_ctx.send(embed = embed)
    if choice_ctx.values[0] == "5":
        embed = discord.Embed(title= "🎮 Jeux 🎮",description = f"", color=red)
        embed.add_field(name = "roulette", value= "Pour tirer au hasard qui gagnera des participants un ban ou kick ou rôle personnalisé un mute ou un gage.", inline = True)
        embed.add_field(name = "pfc <texte>", value= "Faire un pierre feuille ciseaux", inline = True)
        embed.add_field(name = "qi <membre> (argument facultatif)", value = "Connaitre son QI ou celui d'un autre membre/bot du serveur.", inline = True)
        embed.add_field(name = "number ", value= "**CETTE COMMANDE N'EST DISPONIBLE QU'EN SLASH** Pour avoir un nombre au hasard.", inline=True)
        embed.set_footer(text="https://el2zay.is-a.dev/elbot")
        await choice_ctx.send(embed = embed)
    if choice_ctx.values[0] == "6":
        embed = discord.Embed(title= "👾 Autre 👾",description = f"", color=red)
        embed.add_field(name = "pessi", value= "Pour connaitre tous les mots de pessis", inline = True)
        embed.add_field(name = "github", value= "Pour afficher le code github", inline = True)
        embed.add_field(name = "funfact", value = "Pour connaitre une anecdote sur Elbot.", inline = True)
        embed.add_field(name = "timer/minuteur <secondes>", value= "Pour lancer un minuteur à la fin de ce minuteur vous serez averti par MP", inline=True)
        embed.add_field(name = "removebg <lien>", value= "Enlever l'arrière plan d'un image.\nPowered by removebg", inline = True)
        embed.add_field(name = "watchbot", value= "Voir le statut des bots amis à Elbot au fil du temps à l'aide de Watchbot", inline = True)
        embed.add_field(name = "choix", value = "Commande pour test les boutons que j'ai laissé...", inline = True)
        embed.add_field(name = "cuisiner <texte>", value= "Ça sert à rien mais ça m'aide beaucoup.", inline=True)
        embed.add_field(name = "reverse", value= "Lance un reverse", inline=True)
        embed.add_field(name = "dm <id>", value= "Pour me faire dire tout et n'importe quoi en mp a des personnes grâce à leurs ID's", inline=True)
        embed.set_footer(text="https://el2zay.is-a.dev/elbot")
        await choice_ctx.send(embed = embed)


@bot.command()
async def invite(ctx): #site ok
    buttons = [
        create_button(url='https://discord.com/api/oauth2/authorize?client_id=809344905674489866&permissions=8&scope=applications.commands%20bot',
                label="Admin",
                style=ButtonStyle.URL,
        ),
        create_button(url='https://discord.com/api/oauth2/authorize?client_id=809344905674489866&permissions=139858407030&scope=applications.commands%20bot',
                label="Basique",
                style=ButtonStyle.URL,
        )
        ]
    action_row = create_actionrow(*buttons)
    fait_choix = await ctx.send("Veuillez choisir.", components=[action_row])



@bot.command()
async def watchbot(ctx): #site ok
    buttons = [
        create_button(url='https://status.watchbot.app/bot/809344905674489866',
                label="Elbot",
                style=ButtonStyle.URL,
        ),
        create_button(url='https://status.watchbot.app/bot/789214685089759253',
                label="AC V3",
                style=ButtonStyle.URL,
        ),
        create_button(url='https://status.watchbot.app/bot/789214685089759253',
                label="AC V2",
                style=ButtonStyle.URL,
        ),
        create_button(url='https://status.watchbot.app/bot/550404246290563072',
                label="OmegaBOT",
                style=ButtonStyle.URL,
        ),
        create_button(url='https://status.watchbot.app/bot/725455465701572740',
                label="rmxbot",
                style=ButtonStyle.URL,
        )
        ]
    action_row = create_actionrow(*buttons)
    fait_choix = await ctx.send("Lequel de ces bots souhaitiez vous connaitre les incidents reportés ?", components=[action_row])



@bot.command()
async def choix(ctx): #site ok
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
#guild_ids = [id du serv] pour test
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



guild_ids = [865914342041714700]
@slash.slash(name="infoserver", description="Pour connaitre les informations sur ce serveur")
async def infoserver(ctx): #site ok
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
    # Obtenir le nom de la plateforme
    platform = os.name
    # Si la plateforme est linux
    if platform == 'linux':
        await ctx.reply("Le code python est en ce moment hébergé sur la freebox de Elie (c'est pas une blague)")
    #Si la plateforme est mac
    if platform == "darwin" or "macOS" or "mac" or 'macintosh': 
        await ctx.reply("Le code python est en ce moment hébergé sur le macbook d'Elie")
    else:
        await ctx.reply("OS inconnu.")

@slash.slash(name="funfact", description="Pour connaitre une anecdote sur elbot et sa création.")
async def funfact(ctx): #site ok
 await ctx.send(random.choice(funFact))


#Twitter
#Envoyer un tweet

@bot.command(aliases=["twitter"])
@commands.check(isOwner)
async def tweet(ctx, *texte):
    import auth
    api, auth = auth.auth()
    texte = " ".join(texte)
    api.update_status(status=f"{texte}")
    embed = discord.Embed(title = "Tweet envoyé", description = "Votre tweet a été envoyé!", color=0x2986cc)
    embed.set_author(name = "ubuntulebest", icon_url = "https://pbs.twimg.com/profile_images/1390336237039403008/45vvjcIo_400x400.jpg", url = "https://twitter.com/ubuntulebest" )
    await ctx.send(embed = embed)


#fin twitter
#Removebg
@bot.command()
async def removebg(ctx, text): #site ok
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data = {
            'image_url': (text),
            'size': 'auto'
        },
        headers = { 'X-Api-Key': auth.removebg , 'Accept': 'application/json' },
    )
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        file = discord.File(io.BytesIO(base64.b64decode(data["data"]["result_b64"])), 'withoutBg.png')
        await ctx.send(file=file)
    else:
        print(chalk.red(f"Error:, {response.status_code, response.text}"))
        embed=discord.Embed(title="Erreur inconnue", description=f"Erreur console {response.status_code, response.text}", color=0xff0000)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
        embed.set_footer(text="`e!contact` si vous avez un problème")
        await ctx.message.reply(embed=embed)


#Fin de removebg
#Database    
ancien = ["Highest ça va ?","Waaaaaah le dinosaure","Même Highest est moins vieux","T'es vivant?????", "Starfoullah comment t'as fait pour vivre aussi longtemps????"]
futuriste = ["Tu es dans le futur.", "Wahahaha Baby Bosse","Même Steve Jobs il était moins dans le turfu que toi","Imagine je suis ton futur daron ptdrrrrrrr"]
@bot.command(aliases=['add_birthday','set_birthday','birthday_set']) #site ok
async def birthday_add(ctx, day : int, month : str, year : int = None):
    # Vérifier si la date est valide - jour de naissance
    if day < 1:
        return await ctx.reply("Erreur : le jour doit être compris entre 1 et 31")

    # Vérifier si la date est valide - jour de naissance
    if day > 31:
        return await ctx.reply("Erreur : " + random.choice(futuriste))

    # Si le mois contient une majuscule, mettre le mois en minuscule
    if month.isupper():
        month = month.lower()

    # Vérifier si la date est valide - mois de naissance
    if month != "janvier" and month != "février" and month != "mars" and month != "avril" and month != "mai" and month != "juin" and month != "juillet" and month != "août" and month != "septembre" and month != "octobre" and month != "novembre" and month != "décembre" and month != "decembre":
        return await ctx.reply("Erreur vous n'avez pas sélectionner un mois valide")

    # Vérifier si la date est valide - année de naissance
    if year:
        if year > 2021:
            return await ctx.reply("Erreur : " + random.choice(futuriste))
        if year < 1900:
            return await ctx.reply("Erreur : " + random.choice(ancien))

    # Modifier l'argument si il n'y a pas d'année
    if not year:
        args = f"{day} {month}" 
    else:
        args = f"{day} {month} {year}"

    # Dire que la vérification est en cours
    msg = await ctx.reply(f'<a:chargement:922054172734550027> Vérification en cours... veuillez patienter. <a:chargement:922054172734550027>')

    # Vérifier une date impossible/invalide
    if args.startswith("30 janvier") or args.startswith ("30 février") or args.startswith ("31 février") or args.startswith("31 avril") or args.startswith ("31 juin") or args.startswith ("31 septembre") or args.startswith ("31 novembre"):
        return await msg.edit(content="Erreur vous n'avez pas saisi une date invalide.")

    # Vérifier si une date est déjà entré dans la BDD
    birthday = supabase.table('birthday').select('user_id, birthday_date_ddmmyyyy').eq('user_id', str(ctx.message.author.id)).execute()

    # Obtenir la date au format DD/MM/YYYY
    birthday_date_ddmmyyyy = args.split(" ")
    birthday_date_ddmmyyyy = "/".join(birthday_date_ddmmyyyy)
    birthday_date_ddmmyyyy = birthday_date_ddmmyyyy.replace("janvier","01").replace("février","02").replace("fevrier","02").replace("mars","03").replace("avril","04").replace("mai","05").replace("juin","06").replace("juillet","07").replace("aout","08").replace("août","08").replace("septembre","09").replace("octobre","10").replace("novembre","11").replace("décembre","12").replace("decembre","12")

    # Si une date est déjà enregistré (oui oui le "not" est voulu)
    if(not str(birthday['data']) == "[]"):
        # Dire que la modification est en cours...
        await msg.edit(content=f'<a:chargement:922054172734550027> Veuillez patienter pendant la modification de votre date de naissance... <a:chargement:922054172734550027>')
        
        # Modifier dans Supabase la date de naissance
        supabase.table('birthday').update({ 'birthday_date_france': args, 'birthday_date_ddmmyyyy': birthday_date_ddmmyyyy }).eq('user_id', str(ctx.message.author.id)).execute()
        
        # Dire que la modification est terminé
        return await msg.edit(content=f'Votre date de naissance a été modifié avec succès ✅ !')
    else:
        # Dire que l'ajout est en cours
        await msg.edit(content=f'<a:chargement:922054172734550027> Veuillez patienter pendant l\'ajout de votre date de naissance... <a:chargement:922054172734550027>')
        
        # Ajouter dans Supabase dans la date de naissance
        setBirthday = supabase.table('birthday').insert({ 'user_id': ctx.message.author.id, 'username': ctx.author.name, 'birthday_date_france': args, 'birthday_date_ddmmyyyy': birthday_date_ddmmyyyy }).execute()
        
        # Une fois l'ajout dans Supabase terminé
        if(setBirthday['status_code'] == 201):
            await msg.edit(content=f'Ajout de votre date de naissance effectué ✅ !')
        else:
            await msg.edit(content=f"Impossible d\'ajouter votre date de naissance ❌ !\n```\n{setBirthday['data']['message']}\n```")
        return

@bot.command(aliases=['birthdays','list_birthday']) #site ok
async def birthday(ctx, member : discord.Member = None):
    # Si aucune personne n'est mentionnée
    if (not member):
        # Obtenir la liste des anniversaires sur le serveur
        birthdayListSupabase = supabase.table('birthday').select('user_id, birthday_date_france').execute()

        # Si aucun anniversaire
        if(str(birthdayListSupabase['data']) == "[]"):
            embed=discord.Embed(title="Aucun anniversaire", description="Aucun anniversaire n'est enregistrer.\nFaites la commande `e!set_birthday <date>` pour enregistrer la votre !\nSinon vous pouvez consultez la page d'aide https://el2zay.is-a.dev/elbot/", color=0xff0000)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/795288700594290698/909889058212311061/Sans_titre_1.jpeg")
            await ctx.message.reply(embed=embed)
            return print(chalk.red(f"ERREUR: {ctx.author} a essayé de faire la commande birthday sur le serveur {ctx.guild.name} alors que personne n'a enregistrer sa date d'anniversaire !"))

        # Modifier la liste pour avoir uniquement les anniversaires des personnes sur ce serveur
        birthdayList = []
        for birthday in birthdayListSupabase['data']:
            if ctx.guild.get_member(int(birthday['user_id'])) is not None:
                birthdayList.append(birthday)

        # A chaque anniversaire dans la liste
        allBirthdayMsg = ""
        for birthday in birthdayList:
            allBirthdayMsg += f'🎉 **{bot.get_user(int(birthday["user_id"]))}** est né le **{birthday["birthday_date_france"]}** 🎉\n' 

        # Crée un embed
        embed=discord.Embed(title=f"Liste des anniversaires", description=allBirthdayMsg, color=cyan)

        # Si aucune date n'a été enregistrer pour l'auteur du message, ajouter un footer
        birthdayExist = supabase.table('birthday').select('user_id, birthday_date_ddmmyyyy').eq('user_id', str(ctx.message.author.id)).execute()
        if(len(birthdayExist['data']) == 0):
            embed.set_footer(text=f"Ajouter le votre : `e!set_birthday`")
        else:
            embed.set_footer(text=f"{len(birthdayList)} anniversaire(s) enregistré(s)")

        # Envoyer l'embed
        return await ctx.send(embed=embed)
    #Si une personne est mentionné
    else:
        # Obtenir la date de naissance de la personne mentionné
        birthday = supabase.table('birthday').select('user_id, birthday_date_france, birthday_date_ddmmyyyy').eq('user_id', str(member.id)).execute()
        birthday = birthday["data"]

        # Vérifier si une date de naissance a été enregistré
        if(str(birthday) == "[]"):
            return await ctx.reply(f"{member.mention} n'a pas enregistrer sa date de naissance ! ❌")

        
        # Générer le message/la description de l'embed
        birthdayMessage = f"{member.mention} est né le **{birthday[0]['birthday_date_france']}** 🎉"

        if(date.today().strftime('%d/%m') == f"{birthday[0]['birthday_date_ddmmyyyy'].split('/')[0]}/{birthday[0]['birthday_date_ddmmyyyy'].split('/')[1]}"):
            birthdayMessage += f"\n\n(pssh, c'est aujourd'hui)"

        # Crée un embed
        embed=discord.Embed(title=f"{member.name}#{member.discriminator}", description=birthdayMessage, color=cyan)
        embed.set_thumbnail(url=member.avatar_url)
        
        # Envoyer l'embed
        return await ctx.send(embed=embed)

@bot.command(aliases=['set_reply'])
async def set_rep(ctx, *args):
    # Vérifier si l'utilisateur a les permissions
    if(not ctx.author.guild_permissions.administrator):
        return await ctx.reply("Vous n'avez pas les permissions pour faire cette commande ! Vous devez être administrateur sur ce serveur")

    # Vérifier si l'utilisateur a bien entré un argument
    if(len(args) == 0):
        return await ctx.reply("Vous devez entrer un argument !\n\nListe des arguments possible :\n> `cpp` (c'est pas possible)\n> `bonbon` (BONBON :candy:)\n> `linuxmerde` (linux c'est de la merde)\n> `jannotgaming` (Jannot Gaming)\n> `tutititutu`\n> `changezstickman` (changez pour stickman)\n> `apple`\n> `scratch`\n> `bonjoir`\n> `courgette`\n> `ouille`\n\n*vous pouvez faire `e!set_reply all` pour tout activer/désactiver*")

    # Vérifier si l'argument ne fais pas parti d'une certaine liste
    if(args[0] not in ["cpp","bonbon","linuxmerde","jannotgaming","tutititutu","changezstickman","apple","noice","scratch","bonjoir","courgette","ouille","all"]):
        return await ctx.reply("Vous devez entrer un argument valide !\n\nListe des arguments possible :\n> `cpp` (c'est pas possible)\n> `bonbon` (BONBON :candy:)\n> `linuxmerde` (linux c'est de la merde)\n> `jannotgaming` (Jannot Gaming)\n> `tutititutu`\n> `changezstickman` (changez pour stickman)\n> `apple`\n> `scratch`\n> `bonjoir`\n> `courgette`\n> `ouille`\n\n*vous pouvez faire `e!set_reply all` pour tout activer/désactiver*")

    # Vérifier si l'argument est "all"
    if(args[0] == "all"):
        print(str(ctx.guild.id))
        needToDisable = supabase.table('disabledAutoMessage').select('cpp').eq('guild_id', str(ctx.guild.id)).execute()['data']

        # Si la taille de la liste est 0, activer tout
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "cpp": False, "bonbon": False, "linuxmerde": False, "jannotgaming": False, "tutititutu": False, "changezstickman": False, "apple": False, "scratch": False, "bonjoir": False, "courgette": False, "ouille": False}).execute()
            return await ctx.reply("Tout les messages automatiques ont été activé !")

        needToDisable = needToDisable[0]['cpp']
        # Vérifier si cpp est sur True
        if(needToDisable == True):
            # Tout désactiver
            print(supabase.table('disabledAutoMessage').update({"cpp": False, "bonbon": False, "linuxmerde": False, "jannotgaming": False, "tutititutu": False, "changezstickman": False, "apple": False, "scratch": False, "bonjoir": False, "courgette": False, "ouille": False}).eq('guild_id', str(ctx.guild.id)).execute())
            await ctx.send("Désactivation de tout les messages automatique...")

        # Vérifier si cpp est sur False
        if(needToDisable == False):
            # Tout activer
            print(supabase.table('disabledAutoMessage').update({"cpp": True, "bonbon": True, "linuxmerde": True, "jannotgaming": True, "tutititutu": True, "changezstickman": True, "apple": True, "scratch": True, "bonjoir": True, "courgette": True, "ouille": True}).eq('guild_id', str(ctx.guild.id)).execute())
            await ctx.send("Activation de tout les messages automatique...")
        return

    # Si l'argument n'est pas "all"
    if args[0] == "cpp":
        needToDisable = supabase.table('disabledAutoMessage').select('cpp').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "cpp": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "bonbon":
        needToDisable = supabase.table('disabledAutoMessage').select('bonbon').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "bonbon": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "linuxmerde":
        needToDisable = supabase.table('disabledAutoMessage').select('linuxmerde').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "linuxmerde": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "jannotgaming":
        needToDisable = supabase.table('disabledAutoMessage').select('jannotgaming').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "jannotgaming": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "tutititutu":
        needToDisable = supabase.table('disabledAutoMessage').select('tutititutu').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "tutititutu": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "changezstickman":
        needToDisable = supabase.table('disabledAutoMessage').select('changezstickman').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "changezstickman": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "apple":
        needToDisable = supabase.table('disabledAutoMessage').select('apple').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "apple": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "scratch":
        needToDisable = supabase.table('disabledAutoMessage').select('scratch').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "scratch": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "bonjoir":
        needToDisable = supabase.table('disabledAutoMessage').select('bonjoir').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "bonjoir": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "courgette":
        needToDisable = supabase.table('disabledAutoMessage').select('courgette').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "courgette": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    if args[0] == "ouille":
        needToDisable = supabase.table('disabledAutoMessage').select('ouille').execute()['data']
        if(len(needToDisable) == 0):
            supabase.table('disabledAutoMessage').insert({"guild_id": str(ctx.guild.id), "ouille": False}).execute()
            return await ctx.send(f"Activation de {args[0]}...")

    # Activer/désactiver l'argument
    if(needToDisable == True):
        print(supabase.table('disabledAutoMessage').update({ args[0]: False }).execute())
        await ctx.send(f"Désactivation de {args[0]}...")
    if(needToDisable == False):
        print(supabase.table('disabledAutoMessage').update({ args[0]: True }).execute())
        await ctx.send(f"Activation de {args[0]}...")

    return

@bot.command()
async def chat(ctx, *text):
    text = " ".join(text)

    # Appeller l'API pour obtenir la réponse
    response = requests.get(f"https://anticoupable.johanstickman.com/api/ac-chat", data={"message": text})
    print(response.json())
    # Faire un embed affichant la réponse
    embed = discord.Embed(title="Selon un quelqu'un", description=(response.json()['response']).replace("{username}",f'{ctx.author.name}'), footer='"e!set-chat" bientôt dispo', color=0x00ff00)
    await ctx.send(embed = embed)





#Fin Database


bot.run(auth.token)
