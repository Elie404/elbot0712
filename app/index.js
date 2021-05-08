const Discord = require("discord.js");
const client = new Discord.Client();
const fetch = require("node-fetch");
const ytdl = require("ytdl-core");
var prefix = "e!";
const ReactionRoleManager = require("discord-reaction-role");
const manager = new ReactionRoleManager(client, {
  storage: "./reaction-role.json"
});
client.reactionRoleManager = manager;

client.on("ready", () => {
  console.log(
    `Oh tiens je m'appelle ${client.user.tag} (ID : ${client.user.id})`
  );
  {
  client.user.setActivity("Chante tutititutu tout en changeant pour ubuntu", {
  type: "STREAMING",
  url: "https://www.twitch.tv/eli__zay"
});
    
  }
    // Auto Up
  setInterval(() => {
    fetch("https://ac-v2.glitch.me").catch(err => {});
    fetch("https://achost.tk").catch(err => {});
    fetch("https://rmxbot-test.glitch.me").catch(err => {});
    fetch("https://eliebot.glitch.me").catch(err => {});
  }, 70000);
});

client.on("message", message => {
  const args = message.content
    .slice(prefix.length)
    .trim()
    .split(/ +/);
  const command = args.shift().toLowerCase();

  if (command === "reaction") {
    if (
      message.author.id !== "277825082334773251" &&
      message.author.id !== "727572859727380531"
    )
      return;

    /*
  var embed = new Discord.MessageEmbed()
  .setTitle("Role via réaction")
  .setDescription("**Quel OS utilisez vous ?**\niOS :apple:\nAndroid :robot:\nMacOS :desktop:\nWindows :window:\nLinux :penguin:\n\n**Qui êtes vous ?**\nAnti MEE6 :see_no_evil:\nFan de tutititutu :man_dancing:\nDéveloppeur :man_technologist:\n\n**Vous êtes**\nHomme :man:\nFemme :woman:\nStickman <:Stickman:836992390349979670>\n\n**Vous jouez à**\nAmongUS <:among:817444152307613706>\nMinecraft <:minecraft:836844843559944193>\nRocket league :red_car:\nJeu de course (Asphalt et tout) :race_car:")
  .setColor("BLURPLE")
  .setFooter("(Appuie sur les réactions)")
  message.channel.send(embed)
  */

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "🍎",
      role: message.guild.roles.cache.get("836996246919970817")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "🤖",
      role: message.guild.roles.cache.get("836996422519619606")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "🖥",
      role: message.guild.roles.cache.get("836996521841000459")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "🪟",
      role: message.guild.roles.cache.get("836996621157531689")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "🐧",
      role: message.guild.roles.cache.get("836996726870900736")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "🙈",
      role: message.guild.roles.cache.get("836996962754101299")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "🕺",
      role: message.guild.roles.cache.get("836997066047750264")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "👨‍💻",
      role: message.guild.roles.cache.get("836997155411066912")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "👨",
      role: message.guild.roles.cache.get("836997456779935749")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "👩",
      role: message.guild.roles.cache.get("836997555275563058")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: ":Stickman:836992390349979670",
      role: message.guild.roles.cache.get("836997632802422796")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "<:among:817444152307613706>",
      role: message.guild.roles.cache.get("836997901929676810")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "<:minecraft:836844843559944193>",
      role: message.guild.roles.cache.get("836998003206127687")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "🤮",
      role: message.guild.roles.cache.get("836998089184378890")
    });

    client.reactionRoleManager.create({
      messageID: "836995213452115978",
      channel: message.channel,
      reaction: "🏎️",
      role: message.guild.roles.cache.get("836998154930225202")
    });
  }

  if (message.content.startsWith(prefix))
    message.react(":elbot:817423861158510633");

  if (message.content.startsWith("elbot"))
    message.react(":elbot:817423861158510633");

  if (message.content.toLowerCase().includes("ubuntu"))
    message.react("<:ubuntu:816654825248915487>");
  
  if (message.content.startsWith("Jannot Gaming"))
    message.channel.send(
      "https://tenor.com/view/potatoz-jano-gaming-nowagifs-gif-18818348"
    );

  if (message.content.toLowerCase().includes("ubuntu"))
    message.react(":ubuntu_dans_bassine:819657844940472421");


  if (message.content.toLowerCase().includes("merde"))
    message.react("<:bassinechrotte:816630077038264321>");
 
  if (message.content.toLowerCase().includes("merde"))
    message.react("💩");  
   
  if (message.content.startsWith("poubelle")) message.react("🚮");

  if (message.content.startsWith("Tu parles de ce bot chiant et inutile là ?"))
    message.channel.send("Va remix tes pantoufles toi");

  if (message.content.startsWith("Ah nan ça c'est mon connard de proprio... "))
    message.channel.send(
      "https://tenor.com/view/ferme-ta-gueule-ta-gueule-tg-julien-lepers-lepers-gif-13251519"
    );

  if (message.content.startsWith("Toi même"))
    message.channel.send(
      "https://tenor.com/view/nou-no-you-uno-uno-reverse-gif-21173861"
    );

  if (message.content.startsWith("bon")) message.channel.send("BONBON :candy:");

  if (message.content.startsWith("tutititutu"))
    message.react(":Brique_telecom:808798700142460970");

  if (message.content.startsWith("tutititutu"))
    message.channel.send(
      "https://cdn.discordapp.com/emojis/816728856823201813.png?v=1"
    );

  if (message.content.toLowerCase().includes("crotte"))
    message.react("<:bassinechrotte:816630077038264321>");

  if (message.content.toLowerCase().includes("crotte"))
    message.react("💩");  
  
  if (message.content.toLowerCase().includes("caca"))
    message.react("💩");  
  
  if (message.content.toLowerCase().includes("total"))
    message.react(":total:836981580157026304");

  if (message.content.startsWith("courgette")) message.channel.send("Counasse");

    function play() {
      const channel = client.channels.cache.get("817012298057121852");
      if (!channel)
        return console.log("[BriqueLoop] Variable salon/channel invalide.");

      let nombrelist = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5];
      let nombre = nombrelist[Math.floor(Math.random() * nombrelist.length)];

      let songList = [
        "https://cdn.discordapp.com/attachments/795288700594290698/840260770041823252/FullSizeRender.mp3"
      ];
      let song = songList[Math.floor(Math.random() * songList.length)];

      channel
        .join()
        .then(connection => {
          const dispatcher = connection.play(song, {
            volume: nombre
          });

          dispatcher.on("finish", () => {
            play();
          });
        })
        .catch(e => {
          console.log(
            "[BriqueLoop] Erreur lors de la connexion au salon vocal." + e
          );}
        );}

    if (message.content.toLowerCase().includes("ok")) message.react("🆗");
    
    if (message.content.toLowerCase().includes("parfait")) message.react("✅");

    if (message.content.toLowerCase().includes("juin"))
      message.channel.send("**TG FARÈS**");

      if (message.content.toLowerCase().includes("}"))
      message.channel.send("Connard de caractere de merde ");
      
if (message.content.startsWith("Nice"))
    message.channel.send(
      "https://tenor.com/view/noice-nice-click-gif-8843762")
   
    if (message.content.startsWith("Noice"))
    message.channel.send(
      "https://tenor.com/view/noice-nice-click-gif-8843762")

    if (message.content.toLowerCase().includes("scratch"))
      message.channel.send("Chat orange de merde");

    if (message.content === "oof") message.react(":oof:836989811897532457");

    if (message.content.toLowerCase().includes("bonjoir"))
      message.channel.send("Hachoir");

    if (message.content.toLowerCase().includes("rmxbot"))
      message.channel.send(
        "Ptdr il est plus inutile que moi mais je l'aime bien"
      );

    if (message.content.toLowerCase().includes("chromebook"))
      message.channel.send("Ubuntu>>>>>>>>>>");

    if (message.content === "issou")
      message.channel.send(
        "ISSOU DE SECOURS https://tenor.com/view/issou-de-secours-gif-14359921"
      );

    if (message.content === "Je le répète mais la place de la femme c'est où?")
      message.channel.send("Dans la kouisine ouais cousin");

    if (message.content === "Je le répète mais la place de l'homme c'est où?")
      message.channel.send("Devant le pc entrain de se br****");

    if (command === "say") {
      var contenu = args.join(" ");
      if (!contenu)
        return message.channel.send("T'es con ou quoi? **ECRIT FRÈRE**");
      message.channel.send(contenu);
      message.delete().catch();
    }
    
if (command === "twitter")
var embed = new Discord.MessageEmbed()
.setTitle("**VOICI LE TWITTER PRINCIPAL DU SERVEUR CHANGEZ POUR UBUNTU**")
.setDescription(
"https://twitter.com/ubuntulebest")
.setColor("BLUE")
.setFooter("Abonne toi 👀")
message.channel.send(embed);


    if (command === "uno")
      message.channel.send(
        "https://tenor.com/view/nou-no-you-uno-uno-reverse-gif-21173861"
      );

      if (command === "help") {
        var embed = new Discord.MessageEmbed()
          .setTitle("**VOICI presque TOUTES LES COMMANDES DE ELBOT**")
          .setDescription(


            "`pessi`:Pour connaitre tous les mots de pessis \n`brique` pour que je chante TUTITITUTU\n`help`: Pas besoins de le dire \n`say` Pour me faire dire tout et n'importe quoi \n`uno` Pour avoir la carte changement de sens \n`test` Pour savoir si je fonctionne \n`invite` Pour m'inviter dans un serveur 🙃\n`twitter` Pour connaitre le compte twitter de ce serveur \n`heberger` Pour savoir sur quel hébergeur je suis héberger en ce moment!\n`ping` Pour connaitre mon ping."
          )
          .setColor("BLURPLE")
          .setFooter("(En plus si tu dis mon nom ça enclenchera une guerre de bot 🙃) ah et mon prefix c'est e! mais je pense tu le sais déjà")
        message.channel.send(embed);
        
      }

    if (command === "test")
      message.channel.send("Y'a quoi zbi? Sinon moi je fonctionne.");

    if (command === "brique") {
      play();
      message.channel.send("let's go :bricks:");
    }

if (command === "heberger")
message.channel.send("Je suis en ce moment héberger sur Heroku!")
    


    if (command === "invite") {
      message.channel.send(
        "https://discord.com/api/oauth2/authorize?client_id=809344905674489866&permissions=3152128&scope=bot"
      );
    }

    if (command === "pessi") {
      var embed = new Discord.MessageEmbed()
        .setTitle("**LES MOTS DES PESSI**")
        .setDescription(
          "culotté\npleure\nchiale\nchouine\ncouine\naboie\nmiaule\nboude\nbrûle\nhurle\ncrie\ncrève\npleurniche\nricane\njacasse\nagonise\nbeugle\nchuchote\nmurmure\nronfle\nsuffoque\nimplose\nexplose\nrugis\nsiffle\nronronne\ncaquette\nrenifle\nvis\nroucoule\nsouffre\nsoufle\ndort"
        )
        .setColor("BLURPLE");
      message.channel.send(embed);
    }

    if (message.content.toLowerCase().startsWith("siri"))
      message.channel.send("Je suis Siri votre assistant personnel ", {
        tts: true
      });

  if (command === "play") {
    execute(message, serverQueue);
    return;
  } else if (command === "skip") {
    skip(message, serverQueue);
    return;
  } else if (command === "stop") {
    stop(message, serverQueue);
    return;
  } else {
    message.channel.send("You need to enter a valid command!");
  };

  if (command === "ping") {
    if (message.author.bot === true) return;
    message.channel.send(
      "Le ping pong c'est de la merde je préfère utiliser des briques comme raquettes mais en tout cas j'ai " +
        client.ws.ping +
        " ms"
    );

  const voiceChannel = message.member.voice.channel;
  if (!voiceChannel)
    return message.channel.send(
      "You need to be in a voice channel to play music!"
    );
  const permissions = voiceChannel.permissionsFor(message.client.user);
  if (!permissions.has("CONNECT") || !permissions.has("SPEAK")) {
    return message.channel.send(
      "I need the permissions to join and speak in your voice channel!"
    );
  }

  const songInfo = ytdl.getInfo(args[1]);
  const song = {
        title: songInfo.videoDetails.title,
        url: songInfo.videoDetails.video_url,
   };

  if (!serverQueue) {
    const queueContruct = {
      textChannel: message.channel,
      voiceChannel: voiceChannel,
      connection: null,
      songs: [],
      volume: 5,
      playing: true
    };

    queue.set(message.guild.id, queueContruct);

    queueContruct.songs.push(song);

    try {
      var connection = voiceChannel.join();
      queueContruct.connection = connection;
      play(message.guild, queueContruct.songs[0]);
    } catch (err) {
      console.log(err);
      queue.delete(message.guild.id);
      return message.channel.send(err);
    }
  } else {
    serverQueue.songs.push(song);
    return message.channel.send(`${song.title} has been added to the queue!`);
  }
}

function skip(message, serverQueue) {
  if (!message.member.voice.channel)
    return message.channel.send(
      "You have to be in a voice channel to stop the music!"
    );
  if (!serverQueue)
    return message.channel.send("There is no song that I could skip!");
  serverQueue.connection.dispatcher.end();
}

function stop(message, serverQueue) {
  if (!message.member.voice.channel)
    return message.channel.send(
      "You have to be in a voice channel to stop the music!"
    );
    
  if (!serverQueue)
    return message.channel.send("There is no song that I could stop!");
    
  serverQueue.songs = [];
  serverQueue.connection.dispatcher.end();
}

function play(guild, song) {
  const serverQueue = queue.get(guild.id);
  if (!song) {
    serverQueue.voiceChannel.leave();
    queue.delete(guild.id);
    return;
  }

  const dispatcher = serverQueue.connection
    .play(ytdl(song.url))
    .on("finish", () => {
      serverQueue.songs.shift();
      play(guild, serverQueue.songs[0]);
    })
    .on("error", error => console.error(error));
  dispatcher.setVolumeLogarithmic(serverQueue.volume / 5);
  serverQueue.textChannel.send(`Start playing: **${song.title}**`);
}
});
client.login(process.env.TOKEN);
