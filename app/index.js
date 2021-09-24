// Importer discord.js et crée un client
const Discord = require("discord.js");
const client = new Discord.Client({ intents: ["GUILDS", "GUILD_MESSAGES", "DIRECT_MESSAGES", "GUILD_PRESENCES", "GUILD_MEMBERS", "GUILD_VOICE_STATES"], partials: ["CHANNEL"] });

// Importer chalk, node-fetch, canvas et dotenv
const chalk = require('chalk');
const fetch = require('node-fetch');
const Canvas = require('canvas');
require('dotenv').config();

// Discord-player
	// L'importer et crée un player
	const { Player } = require("discord-player");
	const player = new Player(client, {
		ytdlDownloadOptions: {
			filter: "audioonly"
		}
	})

	// Egalement utiliser les attachements Discord
	const { Attachment } = require("@discord-player/extractor");
	player.use("Attachment", Attachment);

	// Event
	player.on("error", (queue, error) => {
		queue.metadata.channel.send(`❌ | Une erreur inconnu s'est produite\n\n${"```\n"}${error.message}${"\n```"}`)
	});
	player.on("connectionError", (queue, error) => {
		queue.metadata.channel.send(`❌ | Erreur lors de la connexion\n\n${"```\n"}${error.message}${"\n```"}`);
	});
	player.on("trackStart", (queue, track) => {
		queue.metadata.channel.send(`🎶 | Je joue **${track.title.replace("video0.mp4","TITUTUTITI")}**`);
	});
	player.on("botDisconnect", (queue) => {
		queue.metadata.channel.send("❌ | J'ai été déconnecté du vocal : suppression de la queue...");
	});
	player.on("channelEmpty", (queue) => {
		queue.metadata.channel.send("❌ | Tout le monde est parti du vocal :(");
	});
	player.on("queueEnd", (queue) => {
		queue.metadata.channel.send("✅ | J'ai fini de lire l'ensemble des musiques présentes dans la queue");
	});
	
// Préfix du bot
var prefix = "e!";

// Quand le bot est allumé et connecté
client.on('ready', () => {
	// L'afficher dans la console
	log(`Oh tiens je m'appelle ${client.user.username}#${client.user.discriminator}`, "connect")
})

// Fonction pour vérifier si on est dans un salon vocal
async function isVocal(interaction, message){
	// Si c'est une interaction
	if(interaction){
		if(!interaction.guildId) return (await generateErrorEmbed("Vous devez être dans un serveur.","JS_8_1"))
		if(!interaction.member.voice.channelId) return (await generateErrorEmbed("Vous devez être dans un salon vocal.","JS_8_2"))
	}

	// Si c'est un message
	if(message){
		if(message.channel.type !== "dm") return (await generateErrorEmbed("Vous devez être dans un serveur.","JS_8_3"))
		if(!message.member.voice.channel) return (await generateErrorEmbed("Vous devez être dans un salon vocal.","JS_8_4"))
	}

	// Si tout est bon
	return true;
}

// Fonction pour crée un embed d'erreur
function generateErrorEmbed(description, code){
	// Crée un embed (le but même de la fonction)
	var embed = new Discord.MessageEmbed()
	.setTitle("Oh mince, je viens d'avoir une erreur...")
	.setDescription(description)
	.setThumbnail("https://firebasestorage.googleapis.com/v0/b/storage-bf183.appspot.com/o/otherImages%2Felbot-triste.png?alt=media")
	.setColor("#e51c23")
	.setFooter("Code erreur : #" + code)

	// Retourner l'embed
	return embed;
}

// Fonction pour afficher un texte dans la console
function log(text, type){
	if(type === "error" || type === "err") console.log(chalk.red(text))
	if(type === "connect") console.log(chalk.yellow(text))
	if(type === "info") console.log(chalk.blue(text))
	if(!type) console.log(text)
}

// Commande du bot
async function handleCommand(name, args, interaction, message){
	// Commande "ping"
	if(name === "ping"){
		if(interaction) interaction.reply({ content: `Le ping pong c'est de la merde je préfère utiliser des briques comme raquettes, en tout cas j'ai ${client.ws.ping} ms de ping (JS)`, ephemeral: true })
		if(message) message.reply({ content: `Le ping pong c'est de la merde je préfère utiliser des briques comme raquettes, en tout cas j'ai ${client.ws.ping} ms de ping (JS)` })
	}
	// Commande "say"
	if(name === "say"){
		// Obtenir l'argument
		if(interaction) var content = args[0].value
		if(message) var content = args.join(' ')

		// Vérifier si un argument a bien été donné
		if(!content && interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("Aucun argument n'a été donné...","JS_1_0"))], ephemeral: true });
		if(!content && message) return message.reply({ embeds: [(await generateErrorEmbed("Aucun argument n'a été donné...","JS_1_1"))] });

		// Envoyer le message
		if(interaction) client.channels.cache.get(interaction.channelId).send({ content: content.replace(/@/g, "@_ _") }).catch(err => {})
		if(message) message.delete().catch(err => {}) && message.channel.send({ content: content.replace(/@/g, "@_ _") })
	}
	// Commande "sticksay"
	if(name === "sticksay"){
		// Mettre en attente l'interaction
		if(interaction) interaction.deferReply({ ephemeral: true }).catch(err => {})

		// Obtenir l'argument
		if(interaction) var content = args[0].value
		if(message) var content = args.join(' ')

		// Vérifier si un argument a bien été donné
		if(!content && interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("Aucun argument n'a été donné...","JS_10_0"))], ephemeral: true });
		if(!content && message) return message.reply({ embeds: [(await generateErrorEmbed("Aucun argument n'a été donné...","JS_10_1"))] });
	
		// Vérifier si l'argument est trop long
		if(content.length > 34 && interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("L'argument dépasse la limite de 34 caractères.","JS_10_2"))], ephemeral: true });
		if(content.length > 34 && message) return message.reply({ embeds: [(await generateErrorEmbed("L'argument dépasse la limite de 34 caractères.","JS_10_3"))] });

		// Modifier l'argument
		var content = content.match(/.{1,13}/g)
		var content = content.map(c => c).join('\n')

		// Crée un canvas de 1024x1024 pixels
		const canvas = Canvas.createCanvas(1024, 1024);
		const context = canvas.getContext('2d');

		// Ajouter un fond
		const background = await Canvas.loadImage('https://firebasestorage.googleapis.com/v0/b/storage-bf183.appspot.com/o/stickman%2FTemplate%2FSay.png?alt=media');
		context.drawImage(background, 0, 0, canvas.width, canvas.height);
	
		// Choisir la police d'écriture et la couleur
		context.font = '70px sans-serif';
		context.fillStyle = '#000';

		// Ajouter un texte
		const applyText = (canvas, text) => {
			const context = canvas.getContext('2d');

			// Définir la taille de base de l'écriture
			let fontSize = 70;

			do {
				context.font = `${fontSize -= 10}px sans-serif`;
			} while (context.measureText(text).width > canvas.width - 300);

			// Retourner le résultat
			return context.font;
		};

		// Ajouter un texte
		context.font = applyText(canvas, content);	
		context.fillText(content, 416, 240);

		// Crée un attachement
		const attachment = new Discord.MessageAttachment(canvas.toBuffer(), 'sticksay.png');

		// Donner l'image
		if(interaction) return interaction.editReply({ files: [attachment] });
		if(message) return message.channel.send({ files: [attachment] });
	}
	// Commande "removebg"
	if(name === "removebg"){
		// Afficher une erreur
		if(interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("Cette commande n'a pas encore été développé : elle sera bientôt là","JS_3_0"))], ephemeral: true });
		if(message) return message.reply({ embeds: [(await generateErrorEmbed("Cette commande n'a pas encore été développé : elle sera bientôt là","JS_3_1"))] });
	}
	// Commande "translate"
	if(name === "translate"){
		// Afficher une erreur
		if(interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("Cette commande n'a pas encore été développé : elle sera bientôt là","JS_4_0"))], ephemeral: true });
		if(message) return message.reply({ embeds: [(await generateErrorEmbed("Cette commande n'a pas encore été développé : elle sera bientôt là","JS_4_1"))] });
	}
	// Commande "clear"
	if(name === "clear"){
		// Afficher une erreur
		if(interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("Cette commande n'a pas encore été développé : elle sera bientôt là","JS_5_0"))], ephemeral: true });
		if(message) return message.reply({ embeds: [(await generateErrorEmbed("Cette commande n'a pas encore été développé : elle sera bientôt là","JS_5_1"))] });
	}
	// Commande "rickdetect"
	if(name === "rickdetect"){
		// Crée un embed
		var deferEmbed = new Discord.MessageEmbed()
		.setTitle("Rickdetect | Anti-Rickroll")
		.setDescription("Veuillez patienter : vérification du lien en cours...")
		.setColor("#33ff33")
		.setFooter("Rickdetect crée par Johan le stickman   |   johan-perso/rickdetect  @  GitHub")

		// Faire que Elbot réflechisse
		if(interaction) interaction.deferReply({ ephemeral: true })
		if(message) var msg = await message.reply({ embeds: [deferEmbed] })

		// Si le bot est démarré en dev
		if(process.argv.slice(2)[0] === "dev"){
			if(interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("Cette commande est actuellement désactivé : le bot est démarré en mode dev.","JS_7_6"))], ephemeral: true });
			if(msg) return msg.edit({ embeds: [(await generateErrorEmbed("Cette commande est actuellement désactivé : le bot est démarré en mode dev.","JS_7_7"))] });	
		}

		// Obtenir le lien à vérifier
		if(interaction) var link = args[0].value
		if(message) var link = args.join(' ')

        // Enleve les espaces et saut de ligne de l'URL
        var link = link.replace(/ /g, "").replace(/\n/g, "")

        // Vérifier si un argument a été donné
        if(!link){
			if(interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("Veuillez saisir une URL à vérifié","JS_7_0"))], ephemeral: true });
			if(msg) return msg.edit({ embeds: [(await generateErrorEmbed("Veuillez saisir une URL à vérifié","JS_7_1"))] });	
		}

        // Dire si il n'y a pas de domaine
        if(!link.includes(".")){
			if(interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("L'URL donné est invalide : elle ne contient pas d'extension de domaine (.com, .fr, etc)","JS_7_2"))], ephemeral: true });
			if(msg) return msg.edit({ embeds: [(await generateErrorEmbed("L'URL donné est invalide : elle ne contient pas d'extension de domaine (.com, .fr, etc)","JS_7_3"))] });	
		}

        // Ajouter https:// si besoin
        if(!link.startsWith("https://") && !link.startsWith("http://")) var link = "https://" + link
        if(link.startsWith("https://") || link.startsWith("http://")) var link = link

		// Faire que Elbot réflechisse
		deferEmbed.setDescription("Veuillez patienter : vérification Anti-Rickroll de `" + link + "`")
		if(interaction) interaction.editReply({ embeds: [deferEmbed], ephemeral: true })
		if(msg) msg.edit({ embeds: [deferEmbed] })
		
		// Faire une requête pour obtenir le code de la page
		var code = await fetch(link, { method: 'GET', follow: 5, headers: { 'User-Agent': 'Mozilla/4.0 (Windows NT 999.9; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari fait un safari/90.0.0000.000 Safari fait un safari/5301.00' } })
		.then(res => res.text())
		.catch(async err => {
			if(interaction) return interaction.reply({ embeds: [(await generateErrorEmbed("Erreur inconnu lors de la requête.\n```\n" + err + "\n```","JS_7_4"))], ephemeral: true });
			if(msg) return msg.edit({ embeds: [(await generateErrorEmbed("Erreur inconnu lors de la requête.\n```\n" + err + "\n```","JS_7_5"))] });	
		})

		// Vérifier si c'est un rick roll
		if(code.toString().toLowerCase().includes("never","gonna","give","you","up") || code.toString().toLowerCase().includes("rick","roll") || code.toString().toLowerCase().includes("never","gonna","desert","you")){
			deferEmbed.setColor("#259b24")
			deferEmbed.footer = null
			deferEmbed.setDescription("Rick roll trouvé dans le lien : `" + link + "`\n\n[Rickdetect](https://github.com/johan-perso/rickdetect) - l'original")
		} else {
			deferEmbed.setColor("#b0120a")
			deferEmbed.footer = null
			deferEmbed.setDescription("Rick roll **non** trouvé dans le lien : `" + link + "`\n\n[Rickdetect](https://github.com/johan-perso/rickdetect) - l'original")
		}

		// Répondre au message
		if(interaction) interaction.editReply({ embeds: [deferEmbed], ephemeral: true })
		if(msg) msg.edit({ embeds: [deferEmbed] })
	}
	// Commande "watchbot"
	if(name === "watchbot"){
		// Crée une ligne de boutons
		var row = new Discord.MessageActionRow()
		.addComponents(new Discord.MessageButton()
			.setLabel('Elbot')
			.setStyle('LINK')
			.setURL("https://status.watchbot.app/bot/809344905674489866"))
		.addComponents(new Discord.MessageButton()
			.setLabel('Réveilleur')
			.setStyle('LINK')
			.setURL("https://status.watchbot.app/bot/852913553328439339"))
		.addComponents(new Discord.MessageButton()
			.setLabel('Anti Coupable v2')
			.setStyle('LINK')
			.setURL("https://status.watchbot.app/bot/789214685089759253"))
		.addComponents(new Discord.MessageButton()
			.setLabel('OmegaBOT')
			.setStyle('LINK')
			.setURL("https://status.watchbot.app/bot/550404246290563072"))
		.addComponents(new Discord.MessageButton()
			.setLabel('rmxBOT')
			.setStyle('LINK')
			.setDisabled()
			.setURL("https://status.watchbot.app/bot/725455465701572740"))

		// Crée un embed
		var embed = new Discord.MessageEmbed()
		.setTitle("WatchBot")
		.setDescription("Lequel de ces bots souhaitiez vous connaitre les incidents reportés ?")
		.setColor("#33ff33")

		// Envoyer le message
		if(interaction) interaction.reply({ embeds: [embed], components: [row] }).catch(err => {})
		if(message) message.channel.send({ embeds: [embed], components: [row] }).catch(err => {})
	}
	// Commande "help"
	if(name === "help"){
		// Crée un bouton
		var button = new Discord.MessageActionRow()
		.addComponents(new Discord.MessageButton()
			.setLabel('Site d\'Elbot')
			.setStyle('LINK')
			.setURL("https://el2zay.is-a.dev/elbot"))

		// Crée un embed
		var embed = new Discord.MessageEmbed()
		.setTitle("Page d'aide")
		.setDescription("Pour ne pas se compliqué la vie car je ne peux pas h24 mettre à jour la commande (c'est faux il a juste la flemme), je vous invite à regarder [le site d'Elbot](https://el2zay.is-a.dev/elbot).")
		.setColor("#33ff33")

		// Envoyer le message
		if(interaction) interaction.reply({ embeds: [embed], components: [button] }).catch(err => {})
		if(message) message.channel.send({ embeds: [embed], components: [button] }).catch(err => {})
	}
	// Commande "brique"
	if(name === "brique"){
		// Mettre en attente l'interaction
		if(interaction) interaction.deferReply({ ephemeral: true }).catch(err => {})

		// Vérifier si on est dans un salon vocal
			// Faire la vérification
			if(interaction) var is = await isVocal(interaction)
			if(message) var is = await isVocal(message)

			// Donner une erreur
			if(is === true && interaction) interaction.reply({ embeds: [is] }).catch(err => {})
			if(is === true && message) message.channel.send({ embeds: [is] }).catch(err => {})

			// Crée la queue
				// Obtenir le salon où la commande a été faite
				if(interaction) var textChannel = interaction.channel
				if(message) var textChannel = message.channel
				
				// Obtenir le serveur où la commande a été faite
				if(interaction) var guild = interaction.guild
				if(message) var guild = message.guild

				// Et finalement... crée la queue
				const queue = player.createQueue(guild, {
					metadata: {
						channel: textChannel
					}
				});

			// Obtenir le salon vocal à rejoindre
			if(interaction) var vocalChannel = interaction.member.voice.channel
			if(message) var vocalChannel = message.member.voice.channel
	
			// Vérifier la connexion au salon vocal
			try {
				if (!queue.connection) await queue.connect(vocalChannel);
			} catch {
				queue.destroy();
				if(interaction) return await interaction.editReply({ embeds: [(await generateErrorEmbed("Impossible de rejoindre votre salon vocal...","JS_9_0"))] });
				if(message) return await message.channel.send({ embeds: [(await generateErrorEmbed("Impossible de rejoindre votre salon vocal...","JS_9_1"))] });
			}
	
			// Obtenir la musique a joué
				// La chercher
				const track = await player.search("https://cdn.discordapp.com/attachments/794895791248244746/888503721191931934/video0.mp4", {
					requestedBy: interaction.user || message.author
				}).then(x => x.tracks[0]);
				
				// Si on l'a pas trouvé
				if(!track && interaction) return await interaction.followUp({ embeds: [(await generateErrorEmbed("Son introuvable, veuillez contacter le créateur.","JS_9_2"))] });
				if(!track && message) return await message.channel.send({ embeds: [(await generateErrorEmbed("Son introuvable, veuillez contacter le créateur.","JS_9_3"))] });
	
			// Ajouter la musique à la queue
			queue.addTrack(track);
			if(queue.playing === false) queue.play()

			// Dire que bah... ça prépare la musique
			if(interaction) return await interaction.followUp({ content: `⏱️ | Chargement du **TITUTUTITI**` });
			if(message) return await message.channel.send({ content: `⏱️ | Chargement du **TITUTUTITI**` });		
	}
	// Commande "heberger"
	if(name === "heberger"){
		// Envoyer le message
		if(interaction) interaction.reply({ content: `Le code **NodeJS** est en ce moment hébergé sur **${require('os').platform}**`, ephemeral: true }).catch(err => {})
		if(message) message.channel.send({ content: `Le code **NodeJS** est en ce moment hébergé sur **${require('os').platform}**` }).catch(err => {})
	}
	// Commande "info"
	if(name === "info" || name === "lien" || name === "link" || name === "github" || name === "site"){
		// Crée une ligne de boutons
		var row = new Discord.MessageActionRow()
		.addComponents(new Discord.MessageButton()
			.setLabel('WatchBot')
			.setStyle('LINK')
			.setURL("https://status.watchbot.app/bot/809344905674489866"))
		.addComponents(new Discord.MessageButton()
			.setLabel('Mon site')
			.setStyle('LINK')
			.setURL("https://el2zay.is-a.dev/elbot"))
		.addComponents(new Discord.MessageButton()
			.setLabel('GitHub')
			.setStyle('LINK')
			.setURL("https://github.com/el2zay/elbot0712"))
		.addComponents(new Discord.MessageButton()
			.setLabel('Serveur Discord')
			.setStyle('LINK')
			.setURL("https://discord.gg/kQdkqBaE"))

		// Envoyer le message
		if(interaction) interaction.reply({ content: "(Ethan)Lien", components: [row] }).catch(err => {})
		if(message) message.channel.send({ content: "(Ethan)Lien", components: [row] }).catch(err => {})
	}
	// Commande "pessi"
	if(name === "pessi"){
		// Crée une ligne de boutons
		var row = new Discord.MessageActionRow()
		.addComponents(new Discord.MessageButton()
			.setLabel('Liste')
			.setStyle('LINK')
			.setURL("https://hasteb.herokuapp.com/raw/AfMR29mPPMj0RAzmbnGF"))

		// Crée un embed
		var embed = new Discord.MessageEmbed()
		.setTitle("Les mots des pessis (et pas le pepsi)")
		.setDescription("culotté\npleure\nchiale\nchouine\ncouine\naboie\nmiaule\nboude\nbrûle\nhurle\ncrie\ncrève\npleurniche\nricane\njacasse\nagonise\nbeugle\nchuchote\nmurmure\nronfle\nsuffoque\nimplose\nexplose\nrugis\nsiffle\nronronne\ncaquette\nrenifle\nvis\nroucoule\nsouffre\nsoufle\ndort")
		.setColor("#33ff33")

		// Envoyer le message
		if(interaction) interaction.reply({ embeds: [embed], components: [row], ephemeral: true }).catch(err => {})
		if(message) message.channel.send({ embeds: [embed], components: [row] }).catch(err => {})
	}
}

// Quand le bot reçois un message
client.on('messageCreate', message => {
	// Obtenir un argument et le contenu du message en minuscules
	const args = message.content.slice(prefix.length).trim().split(' ');
	const command = args.shift().toLowerCase();
	const content = message.content.toLowerCase()

	// Transférer la commande vers une fonction SI LE MESSAGE COMMENCE PAR LE PREFIX
	if(message.content.startsWith(prefix)) handleCommand(command, args, "", message)

	// Si le message a été fait par moi même
	if(message.author.id !== client.user.id) return;

	// Répondre à quelques messages...
	if(content.includes("je suis suisse") && message.author.id !== "809344905674489866" && content !== "je suis suisse et je suis polie" && content !== "je suis suisse et j'ai les moyens" && content !== "je suis suisse mais suis-je sexy?") return message.reply("Mais quelle heure est-t-il ?")
	if(content === "moi je sais") return message.reply("C'est propre ici, non ?")
	if(content === "bah oui") return message.reply("Et l'or des nazis ?")
	if(content === "steuplait") return message.reply("SUISSE\nAHAHAHAHA")
	if(content === "je suis suisse et je suis polie") return message.reply("C'est bien")
	if(content === "je suis suisse et j'ai les moyens") return message.reply("Youpi")
	if(content === "je suis suisse mais suis-je sexy?") return message.reply("Euh oui mais surtout gentil...")

	if(content.startsWith(prefix) || content.startsWith("elbot")) message.react(":elbot:817423861158510633")
	if(content.startsWith("ubuntu")) message.react(":ubuntu_dans_bassine:819657844940472421") && message.react("<:ubuntu:816654825248915487>")
	if(content.startsWith("merde")) message.react("💩")
	if(content.startsWith("poubelle")) message.react("🚮")
	if(content.startsWith("baldi")) message.react(":baldi:859413939786612756")
	if(content.startsWith("total")) message.react(":total:836981580157026304")
	if(content.startsWith("oof")) message.react(":oof:836989811897532457")

	if(content.startsWith("siri")) return message.reply("Je suis Siri, votre assistant personnel", { tts: true })
	if(content.includes("ubuntu c'est de la merde") || content.includes("linux c'est de la merde")) return message.reply("Regarde cette vidéo et on verra.\nhttps://www.youtube.com/watch?v=jdUXfsMTv7o")
	if(content.includes("jannot gaming")) return message.reply("https://tenor.com/view/potatoz-jano-gaming-nowagifs-gif-18818348")
	if(content.includes("noice")) return message.reply("https://tenor.com/view/noice-nice-click-gif-8843762")

	if(content.startsWith("tu parles de ce bot chiant et inutile là ?")) return message.reply("Va remix tes pantoufles toi")
	if(content.startsWith("ah nan ça c'est mon connard de proprio...")) return message.reply("https://tenor.com/view/ferme-ta-gueule-ta-gueule-tg-julien-lepers-lepers-gif-13251519")
	if(content.startsWith("toi même")) return message.reply("https://tenor.com/view/nou-no-you-uno-uno-reverse-gif-21173861")
	
	if(content.includes("bon")) return message.reply("BONBON :candy:")
	if(content.includes("avira")) return message.reply("PARAPLUIIIIIIIIIIIIIIIIIIIIE") && message.react(":avira:816654625683800074")
	if(content.includes("apple")) return message.reply(" https://tenor.com/view/lisa-simpsons-think-differently-gif-10459041")
	if(content.includes("tutititutu")) return message.reply("https://cdn.discordapp.com/emojis/816728856823201813.png?v=1") && message.react(":Brique_telecom:808798700142460970")
	if(content.includes("bonjoir")) return message.reply("Hachoir")
	if(content.includes("rmxbot")) return message.reply("Ptdr il est plus inutile que moi mais je l'aime bien")
	if(content.includes("courgette")) return message.reply("Counnasse")
	if(content.includes("ouille")) return message.reply("https://pbs.twimg.com/media/ETkK977X0AE3x-x.jpg")

	if (content.includes("<") && content.includes("@") && content.includes(client.user.id) && content.includes(">")) return message.channel.send("euuuh bonjour ? mon prefix c'est `e!`")
})

// Connecter le bot
function connectBot(){ 
client.login(process.env.TOKEN).catch(err => console.log(chalk.red("Impossible de se connecter à Discord : ") + err)) }
connectBot()
