const Discord = require("discord.js");
const client = new Discord.Client();
require("discord-buttons")(client);
const disbut = require("discord-buttons");
const fetch = require("node-fetch");
const ytdl = require ("ytdl-core");
var prefix = "e!";
const ReactionRoleManager = require("discord-reaction-role");
var request = require('request');
var fs = require('fs');
const { mainModule } = require("process");
const manager = new ReactionRoleManager(client, {
  storage: "./reaction-role.json"
});
client.reactionRoleManager = manager;

// NOUVEAU
const queue = new Map();

client.reactionRoleManager = manager;

client.on("ready", () => {
  console.log(
    `Oh tiens je m'appelle ${client.user.tag} (ID : ${client.user.id})`
  );

  // Auto Up
  setInterval(() => {
    fetch("https://ac-v2.glitch.me").catch(err => {});
    fetch("https://achost.tk").catch(err => {});
    fetch("https://rmxbot-test.glitch.me").catch(err => {});
    fetch("https://elbot-test.glitch.me").catch(err => {});
  }, 70000);
});

let Database;
if (typeof window !== "undefined") {
  Discord = DiscordJS;
  Database = EasyDatabase;
} else {
  Database = require("easy-json-database");

  function mathRandomInt(a, b) {
    if (a > b) {
      // Swap a and b to ensure a is smaller.
      var c = a;
      a = b;
      b = c;
    }
    return Math.floor(Math.random() * (b - a + 1) + a);
  }

  async function execute(message, serverQueue) {
    const args = message.content.split(" "); // On récupère les arguments dans le message pour la suite

    const voiceChannel = message.member.voice.channel;
    if (!voiceChannel) {
      // Si l'utilisateur n'est pas dans un salon vocal
      return message.channel.send("Vous devez être dans un salon vocal!");
    }
    const permissions = voiceChannel.permissionsFor(message.client.user); // On récupère les permissions du bot pour le salon vocal
    if (!permissions.has("CONNECT") || !permissions.has("SPEAK")) {
      // Si le bot n'a pas les permissions
      return message.channel.send(
        "J'ai besoin des permissions pour rejoindre le salon et pour y jouer de la musique!"
      );
    }

    const songInfo = await ytdl.getInfo(args[1]);
    const song = {
      title: songInfo.videoDetails.title,
      url: songInfo.videoDetails.video_url
    };

    if (!serverQueue) {
      const queueConstruct = {
        textChannel: message.channel,
        voiceChannel: voiceChannel,
        connection: null,
        songs: [],
        volume: 1,
        playing: true
      };

      // On ajoute la queue du serveur dans la queue globale:
      queue.set(message.guild.id, queueConstruct);
      // On y ajoute la musique
      queueConstruct.songs.push(song);

      try {
        // On connecte le bot au salon vocal et on sauvegarde l'objet connection
        var connection = await voiceChannel.join();
        queueConstruct.connection = connection;
        // On lance la musique
        play(message.guild, queueConstruct.songs[0]);
      } catch (err) {
        //On affiche les messages d'erreur si le bot ne réussi pas à se connecter, on supprime également la queue de lecture
        console.log(err);
        queue.delete(message.guild.id);
        return message.channel.send(err);
      }
    } else {
      serverQueue.songs.push(song);
      console.log(serverQueue.songs);
      return message.channel.send(`${song.title} has been added to the queue!`);
    }
  }

  function skip(message, serverQueue) {
    if (!message.member.voice.channel) {
      // on vérifie que l'utilisateur est bien dans un salon vocal pour skip
      return message.channel.send(
        "Vous devez être dans un salon vocal pour passer une musique!"
      );
    }
    if (!serverQueue) {
      // On vérifie si une musique est en cours
      return message.channel.send("Aucune lecture de musique en cours !");
    }
    serverQueue.connection.dispatcher.end(); // On termine la musique courante, ce qui lance la suivante grâce à l'écoute d'événement
    // finish
  }

  function stop(message, serverQueue) {
    if (!message.member.voice.channel) {
      // on vérifie que l'utilisateur est bien dans un salon vocal pour skip
      return message.channel.send(
        "Vous devez être dans un salon vocal pour stopper la lecture!"
      );
    }
    if (!serverQueue) {
      // On vérifie si une musique est en cours
      return message.channel.send("Aucune lecture de musique en cours !");
    }
    serverQueue.songs = [];
    serverQueue.connection.dispatcher.end();
  }
  function loop(message, serverQueue) {
    if (!message.member.voice.channel) {
      // on vérifie que l'utilisateur est bien dans un salon vocal pour skip
      return message.channel.send(
        "Vous devez être dans un salon vocal pour répéter la lecture!"
      );
    }
    if (!serverQueue) {
      // On vérifie si une musique est en cours
      return message.channel.send("Aucune lecture de musique en cours !");
    }
    serverQueue.songs = [];
    serverQueue.connection.dispatcher.loop();
  }

  function play(guild, song) {
    console.log(song);
    const serverQueue = queue.get(guild.id); // On récupère la queue de lecture
    if (!song) {
      // Si la musique que l'utilisateur veux lancer n'existe pas on annule tout et on supprime la queue de lecture
      serverQueue.voiceChannel.leave();
      queue.delete(guild.id);
      return;
    }
    // On lance la musique
    const dispatcher = serverQueue.connection
      .play(ytdl(song.url, { filter: "audioonly" }))
      .on("finish", () => {
        // On écoute l'événement de fin de musique
        serverQueue.songs.shift(); // On passe à la musique suivante quand la courante se termine
        play(guild, serverQueue.songs[0]);
      })
      .on("error", error => console.error(error));
    dispatcher.setVolume(1); // On définie le volume
    serverQueue.textChannel.send(`Démarrage de la musique: **${song.title}**`);
  }

  client.on("message", async message => {
    if (message.author.bot) {
      return;
    }
    if (!message.content.startsWith(prefix)) {
      return;
    }

    if (message.channel.type !== "dm")
      var serverQueue = queue.get(message.guild.id);

    if (message.content.startsWith(`e!play`)) {
      execute(message, serverQueue); // On appel execute qui soit initialise et lance la musique soit ajoute à la queue la musique
      return;
    } else if (message.content.startsWith(`e!skip`)) {
      skip(message, serverQueue); // Permettra de passer à la musique suivante
      return;
    } else if (message.content.startsWith(`e!stop`)) {
      stop(message, serverQueue); // Permettra de stopper la lecture
      return;
    } else if (message.content.startsWith(`e!loop`)) {
      loop(message, serverQueue); // Permettra de répéter la lecture
      return;
    }
  });

  
  client.on("message", async message => {
    const args = message.content
      .slice(prefix.length)
      .trim()
      .split(/ +/);
    const command = args.shift().toLowerCase();
    if (command === "say") {
      if (!message.content.startsWith(prefix)) return;
      var contenu = args.join(" ");
      if (!contenu)
        return message.channel.send("T'es con ou quoi? **ECRIT FRÈRE**");
      message.channel.send(
        args
          .join(" ")
          .replace(/@everyone/g, "everyone")
          .replace(/@here/g, "here")
      );
      message.delete().catch();
    }
    
    
    if(command === "sticksay"){
        if (!message.content.startsWith(prefix)) return;
      
        var text = args.join('\n')
        
        
const Canvas = canvas.createCanvas(1024, 1024);
const context = Canvas.getContext("2d");
        
        	const background = await canvas.loadImage('./Say.png');
	// This uses the canvas dimensions to stretch the image onto the entire canvas
	context.drawImage(background, 0, 0, Canvas.width, Canvas.height);

	// Set the color of the stroke
	context.strokeStyle = '#74037b';
	// Draw a rectangle with the dimensions of the entire Canvas
	context.strokeRect(0, 0, Canvas.width, Canvas.height);
	// Select the font size and type from one of the natively available fonts
	context.font = '42px sans-serif';
	// Select the style that will be used to fill the text in
	context.fillStyle = '#000000';
	// Actually fill the text with a solid color
	context.fillText(text, 420, 250);

      const attachment = new Discord.MessageAttachment(Canvas.toBuffer(), 'stickman.png');

	message.channel.send(attachment);
    }

   if (command === "removebg")
   request.post({
    url: 'https://api.remove.bg/v1.0/removebg',
    formData: {
      image_url: args [1],
      size: 'auto',
    },
    headers: {
      'X-Api-Key': process.env.REMOVEBG
    },
    encoding: null
  }, function(error, response, body) {
    if(error) return message.channel.send('Request failed:', error);
    if(response.statusCode != 200) return console.error('Error:', response.statusCode, body.toString('utf8'));
    fs.writeFileSync("no-bg.png", body);
  });  





    //Début de la commande clear
if (command === "clear") {
    if (!message.content.startsWith(prefix)) return;
    
    var nombre = args[0];
    message.channel.bulkDelete(nombre);

    if (!nombre) return message.channel.send("T'es con ou quoi???? **DIS UN CHIFFRE FRÈRE**");
    
    if (nombre > 20) {
        var embed = new Discord.MessageEmbed()
        .setTitle("WARN Commande clear")
        .setDescription(`ATTENTION!!! ES-TU SÛR DE VOULOIR CLEAR ${nombre} MESSAGES???`)
        .setColor("#ff0000")
        .setFooter("Oui=✅        Non=❌")
        message.channel.send(embed);
    }
    if (message.content.toLowerCase().includes(embed = new Discord.MessageEmbed()
        .setTitle("WARN Commande clear")
        .setDescription(`ATTENTION!!! ES-TU SÛR DE VOULOIR CLEAR ${nombre} MESSAGES???`)
        .setColor("#ff0000")
        .setFooter("Oui=✅        Non=❌")
        (message.react('❌').then(r => {
            message.react('✅');
          }))));
        
        
        message.awaitReactions((reaction, user) => user.id == message.author.id && (reaction.emoji.name == '❌' || reaction.emoji.name == '✅'),
            { max: 1, time: 30000 }).then(collected => {
            if (collected.first().emoji.name == '✅') {
                message.channel.bulkDelete(nombre)
            } else {
                message.channel.send("Bon bah du coup t'as annulé")
            }
            }).catch(() => {
                message.channel.send('T\'as pas répondu je suppose que t\'as annulé');
            });
    ;

    if (nombre > 100) {
        return message.channel.send("Vous ne pouvez pas clear plus de 100 messages.");
    }

    if (isNaN(nombre)) return message.channel.send("Es tu au courant du fait que ton nombre, n'est pas un nombre ?");
    
    if (nombre > 1) {
        var embed = new Discord.MessageEmbed()
        .setTitle("Commande clear")
        .setDescription(`Salut! ${nombre} messages ont été clear dont ta commande clear!`)
        .setColor("RED")
        message.channel.send(embed);
    }

    if (nombre < 2) {
        var embed = new Discord.MessageEmbed()
        .setTitle("Commande clear")
        .setDescription(`Salut! 1 message a été clear dont ta commande clear!`)
        .setColor("RED")
        message.channel.send(embed);
    }
}
//Fin de la commande clear

   
//Début du rick detect 
if (command === "rickdetect"){
  // Dépendences
const fetch = require('node-fetch'); // https://www.npmjs.com/package/node-fetch

var linkA = args.join(' ')



// Chercher un rick roll
    // Fonction pour fetch le site (et change l'user agent pour empêcher certains site de croire que c'est un robot)
    async function fetchSite(url){
        // Fetch
        var code = await fetch(url, { method: 'GET', follow: 20, size: 500000000})
            .then(res => res.text())
            .catch(err => {
                // En cas d'erreur
                if(err.code === "ENOTFOUND"){
                
                var embed = new Discord.MessageEmbed()
                .setTitle("Commande rickdetect")
                .setDescription("Il est impossible d'accèder a la page : Erreur de réseau ou problème venant du site.")
                .setColor("RED")
                .setImage("https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
                .setFooter("Powered by Rickdetect https://github.com/johan-perso/rickdetect");
                return message.channel.send(embed);
                  }})
              
                var embed = new Discord.MessageEmbed()
            .setTitle(
            "Commande rickdetect"
          )
          .setDescription("Une erreur c'est produite ")
          .setColor("RED")
          .setImage("https://cdn.discordapp.com/attachments/795288700594290698/879752415400837120/elbot-triste.png")
          .setFooter("Powered by Rickdetect https://github.com/johan-perso/rickdetect");
          message.channel.send(embed);
            }
        
        // Retourner le code
        return code
    }})

    // Enleve les espaces et saut de lignede l'URL
    if(linkA.includes(" ") && linkA.includes("\n")) var linkB = linkA.replace(/ /g, "").replace(/\n/g, "")
    if(linkA.includes(" ") && !linkA.includes("\n")) var linkB = linkA.replace(/ /g, "")
    if(!linkA.includes(" ") && linkA.includes("\n")) var linkB = linkA.replace(/\n/g, "")
    if(!linkA.includes(" ") && !linkA.includes("\n")) var linkB = linkA

    // Ajoute https:// si besoin
    if(!linkB.startsWith("https://") && !linkB.startsWith("http://")) var link = "https://" + linkB
    if(linkB.startsWith("https://") || linkB.startsWith("http://")) var link = linkB

    // Dit si il n'y a pas de domaine
    if(!link.includes(".")) return message.channel.send("\"" + link + "\"") + (" n'est pas une adresse valide, il manque une extension de domaine (.com, .fr, etc).")

    // Regarder si le code de la page contient certains éléments
    fetchSite(link).then(code => {
        if(code.toLowerCase().includes("never","gonna","give","you","up") || code.toLowerCase().includes("rick","roll") || code.toLowerCase().includes("never","gonna","desert","you")){
          var embed = new Discord.MessageEmbed()
          .setTitle(
          "Commande rickdetect"
        )
        .setDescription("Ce lien est suspect...")
        .setColor("RED")
        .setImage("https://images.emojiterra.com/twitter/v13.0/512px/26a0.png")
        .setFooter("Powered by Rickdetect https://github.com/johan-perso/rickdetect");
        message.channel.send(embed);
          
        } else {
          var embed = new Discord.MessageEmbed()
          .setTitle(
          "Commande rickdetect"
        )
        .setDescription("Ce lien n'a pas l'air très suspect...")
        .setColor("GREEN")
        .setImage("https://assets.wprock.fr/emoji/joypixels/512/2705.png")
        .setFooter("Powered by Rickdetect https://github.com/johan-perso/rickdetect");
        message.channel.send(embed);
          
        }
    })

}

      client.on("message", async message => {
      if (message.content === "e!twitter")
        var embed = new Discord.MessageEmbed()
          .setTitle(
            "**VOICI LE TWITTER PRINCIPAL DU SERVEUR CHANGEZ POUR UBUNTU**"
          )
          .setDescription("https://twitter.com/ubuntulebest")
          .setColor("BLUE")
          .setFooter("Abonne toi 👀");
      message.channel.send(embed);

      if (message.content.toLowerCase() === "e!watchbot") {
        let button = new disbut.MessageButton()
          .setLabel("Elbot")
          .setURL("https://status.watchbot.app/bot/809344905674489866")
          .setStyle("url");
        let button2 = new disbut.MessageButton()
          .setLabel("Reveilleur")
          .setURL("https://status.watchbot.app/bot/852913553328439339")
          .setStyle("url");
        let button3 = new disbut.MessageButton()
          .setLabel("Anti-Coupable v2 ")
          .setURL("https://status.watchbot.app/bot/789214685089759253")
          .setStyle("url");
        let button4 = new disbut.MessageButton()
          .setLabel("Rmxbot")
          .setURL("https://status.watchbot.app/bot/725455465701572740")
          .setDisabled()
          .setStyle("url");
        let button5 = new disbut.MessageButton()
          .setLabel("OmegaBOT")
          .setURL("https://status.watchbot.app/bot/550404246290563072")
          .setStyle("url");

        var embed = new Discord.MessageEmbed()
          .setTitle(
            "Lequel de ces bots souhaitiez vous connaitre les incidents reportés?"
          )
          .setDescription(
            "1️⃣ Elbot \n 2️⃣ Reveilleur \n 3️⃣ Anti-Coupable v2 \n 4️⃣ Rmxbot (non surveiller pour le moment) \n 5️⃣ OmegaBOT"
          )
          .setColor("33ff33")
          .setFooter("Sélectionnez un bouton");
        let row = new disbut.MessageActionRow()
          .addComponent(button)
          .addComponent(button2)
          .addComponent(button3)
          .addComponent(button4)
          .addComponent(button5);
        message.channel.send(embed, row);
      }

      if (message.content === "e!uno")
        message.channel.send(
          "https://tenor.com/view/nou-no-you-uno-uno-reverse-gif-21173861"
        );

      if (message.content === "e!help") {
        var embed = new Discord.MessageEmbed()
          .setTitle("**Help**")
          .setDescription(
            "Pour ne pas se compliqué la vie car je ne peux pas H24 mettre la commande help à jour je vous invite à regarder le site de elbot où vous trouverez tout ce que vous avez besoin. https://el2zay.is-a.dev/elbot"
          )
          .setColor("BLURPLE")
          .setFooter(
            "(Mais si tu dis mon nom ça enclenchera une guerre de bot 🙃) ah et mon prefix c'est e! mais je pense tu le sais déjà"
          );
        message.channel.send(embed);
      }

      if (message.content === "e!test")
        message.channel.send("Y'a quoi zbi? Sinon moi je fonctionne.");

      if (message.content === "e!brique") {
        play();
        message.channel.send("let's go :bricks:");
      }

      if (message.content === "e!version")
        message.channel.send("En ce moment je tourne sur la version 1.1.1");

      if (message.content === "e!heberger")
        message.channel.send("Le code JS est en ce moment hébergé sur Glitch");

      if (message.content === "e!github")
        message.channel.send(
          "Voici le lien de mon Github\nhttps://bit.ly/33sfsMv \n Attention le repo n'a pas été mise à jour depuis longtemps suite à un changement d'hébergeur"
        );

      if (message.content === "e!invite") {
        message.channel.send(
          "https://discord.com/api/oauth2/authorize?client_id=809344905674489866&permissions=8&scope=bot \n N'oubliez pas d'autoriser la permission admin."
        );
      }

      if (message.content === "e!pessi") {
        var embed = new Discord.MessageEmbed()
          .setTitle("**LES MOTS DES PESSI**")
          .setDescription(
            "culotté\npleure\nchiale\nchouine\ncouine\naboie\nmiaule\nboude\nbrûle\nhurle\ncrie\ncrève\npleurniche\nricane\njacasse\nagonise\nbeugle\nchuchote\nmurmure\nronfle\nsuffoque\nimplose\nexplose\nrugis\nsiffle\nronronne\ncaquette\nrenifle\nvis\nroucoule\nsouffre\nsoufle\ndort"
          )
          .setColor("BLURPLE");
        message.channel.send(embed);
      }
      {
        if (
          message.content.toLowerCase().includes("je suis suisse") &&
          message.author.id !== "809344905674489866" &&
          message.content !== "Je suis suisse et je suis polie" &&
          message.content !== "Je suis suisse et j'ai les moyens" &&
          message.content !== "Je suis suisse mais suis-je sexy?"
        )
          message.channel.send("Mais quelle heure est il?");

        if (message.content === "Moi je sais")
          message.channel.send("C'est propre ici, non?");

        if (message.content === "Bah oui")
          message.channel.send("Et l'or des nazis?");

        if (message.content === "Steuplait")
          message.channel.send("SUISSE \n AHAHAHAHA");

        if (message.content === "Je suis suisse et je suis polie")
          message.channel.send("C'est bien");

        if (message.content === "Je suis suisse et j'ai les moyens")
          message.channel.send("Youpi");

        if (message.content === "Je suis suisse mais suis-je sexy?")
          message.channel.send("Euh oui mais surtout gentil...");
      }
      if (message.content.toLowerCase().startsWith("siri"))
        message.channel.send("Je suis Siri votre assistant personnel ", {
          tts: true
        });

      if (message.content.startsWith(prefix))
        message.react(":elbot:817423861158510633");

      if (message.content.startsWith("elbot"))
        message.react(":elbot:817423861158510633");

      if (message.content.toLowerCase().includes("ubuntu"))
        message.react("<:ubuntu:816654825248915487>");

      if (message.content.toLowerCase().includes("linux c'est de la merde"))
        message.channel.send(
          "Regarde cette vidéo et on verra. \n https://www.youtube.com/watch?v=jdUXfsMTv7o"
        );

         if (message.content.toLowerCase().includes("de"))
        message.channel.send(
          "3, **SOLEIL**"
        );
        
         if (message.content.toLowerCase().includes("2"))
        message.channel.send(
          "3, **SOLEIL**"
        );
           
        if (message.content.toLowerCase().includes("deux"))
        message.channel.send(
          "3, **SOLEIL**"
        );
        
        
      if (message.content.toLowerCase().includes("ubuntu c'est de la merde"))
        message.channel.send(
          "Regarde cette vidéo et on verra. \n https://www.youtube.com/watch?v=jdUXfsMTv7o"
        );

      if (message.content.toLowerCase().includes("Jannot Gaming"))
        message.channel.send(
          "https://tenor.com/view/potatoz-jano-gaming-nowagifs-gif-18818348"
        );

      if (message.content.toLowerCase().includes("ubuntu"))
        message.react(":ubuntu_dans_bassine:819657844940472421");

      if (message.content.toLowerCase().includes("merde"))
        message.react("<:bassinechrotte:816630077038264321>");

      if (message.content.toLowerCase().includes("merde")) message.react("💩");

      if (message.content.startsWith("poubelle")) message.react("🚮");

      if (
        message.content.startsWith("Tu parles de ce bot chiant et inutile là ?")
      )
        message.channel.send("Va remix tes pantoufles toi");

      if (
        message.content.startsWith("Ah nan ça c'est mon connard de proprio... ")
      )
        message.channel.send(
          "https://tenor.com/view/ferme-ta-gueule-ta-gueule-tg-julien-lepers-lepers-gif-13251519"
        );

      if (message.content.startsWith("Toi même"))
        message.channel.send(
          "https://tenor.com/view/nou-no-you-uno-uno-reverse-gif-21173861"
        );

      if (message.content.startsWith("bon"))
        message.channel.send("BONBON :candy:");

      if (message.content.startsWith("tutititutu"))
        message.react(":Brique_telecom:808798700142460970");

      if (message.content.startsWith("tutititutu"))
        message.channel.send(
          "https://cdn.discordapp.com/emojis/816728856823201813.png?v=1"
        );

      if (message.content.toLowerCase().includes("crotte"))
        message.react("<:bassinechrotte:816630077038264321>");

      if (message.content.toLowerCase().includes("avira"))
        message.channel.send("PARAPLUIIIIIIIIIIIIIIIIIIIIE @Johan");

      if (message.content.toLowerCase().includes("changez pour stickman"))
        message.channel.send("*Mangez des stickmans");

      if (message.content.toLowerCase().includes("apple"))
        message.channel.send(
          " https://tenor.com/view/lisa-simpsons-think-differently-gif-10459041"
        );

      if (message.content.toLowerCase().includes("avira"))
        message.react(":avira:816654625683800074");

      if (message.content.toLowerCase().includes("crotte")) message.react("💩");

      if (message.content.toLowerCase().includes("caca")) message.react("💩");

      if (message.content.toLowerCase().includes("baldi"))
        message.react(":baldi:859413939786612756");

      if (message.content.toLowerCase().includes("total"))
        message.react(":total:836981580157026304");

      if (message.content.startsWith("Noice"))
        message.channel.send(
          "https://tenor.com/view/noice-nice-click-gif-8843762"
        );

      if (
        message.content.toLowerCase().includes("scratch") &&
        message.content !== "Le code scratch fonctionne"
      )
        message.channel.send("Chat de merde");

      if (message.content === "oof") message.react(":oof:836989811897532457");

      if (message.content.toLowerCase().includes("bonjoir"))
        message.channel.send("Hachoir");

      if (message.content.toLowerCase().includes("rmxbot"))
        message.channel.send(
          "Ptdr il est plus inutile que moi mais je l'aime bien"
        );

      if (message.content.toLowerCase().includes("courgette"))
        message.channel.send("Counnasse");

      if (message.content.toLowerCase().includes("ouille"))
        message.channel.send("https://pbs.twimg.com/media/ETkK977X0AE3x-x.jpg");

        if (message.content === "e!ping") {
          if (message.author.bot === true) return;
          message.channel.send(
            "Le ping pong c'est de la merde je préfère utiliser des briques comme raquettes mais en tout cas j'ai " +
              client.ws.ping +
              " ms (JS)"
          );
        }

      })
    client.login(process.env.TOKEN);
