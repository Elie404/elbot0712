let Discord;
let Database;
if (typeof window !== "undefined") {
    Discord = DiscordJS;
    Database = EasyDatabase;
} else {
    Discord = require("discord.js");
    Database = require("easy-json-database");
}
const delay = (ms) => new Promise((resolve) => setTimeout(() => resolve(), ms));
const s4d = {
    Discord,
    client: null,
    tokenInvalid: false,
    reply: null,
    joiningMember: null,
    database: new Database("./db.json"),
    checkMessageExists() {
        if (!s4d.client) throw new Error('You cannot perform message operations without a Discord.js client')
        if (!s4d.client.readyTimestamp) throw new Error('You cannot perform message operations while the bot is not connected to the Discord API')
    }
};
s4d.client = new s4d.Discord.Client({
    fetchAllMembers: true
});
s4d.client.on('raw', async (packet) => {
    if (['MESSAGE_REACTION_ADD', 'MESSAGE_REACTION_REMOVE'].includes(packet.t)) {
        const guild = s4d.client.guilds.cache.get(packet.d.guild_id);
        if (!guild) return;
        const member = guild.members.cache.get(packet.d.user_id) || guild.members.fetch(d.user_id).catch(() => {});
        if (!member) return;
        const channel = s4d.client.channels.cache.get(packet.d.channel_id);
        if (!channel) return;
        const message = channel.messages.cache.get(packet.d.message_id) || await channel.messages.fetch(packet.d.message_id).catch(() => {});
        if (!message) return;
        s4d.client.emit(packet.t, guild, channel, message, member, packet.d.emoji.name);
    }
});
var arguments2, command;
var dotenv = require('dotenv')
function mathRandomInt(a, b) {
    if (a > b) {
        // Swap a and b to ensure a is smaller.
        var c = a;
        a = b;
        b = c;
    }
    return Math.floor(Math.random() * (b - a + 1) + a);
}


s4d.client.on('message', async (s4dmessage) => {
    if (((String((s4dmessage.content)).includes(String('tg'))) || (String((s4dmessage.content)).includes(String('ta gueule')))) && ((s4dmessage.author.id) == '670753544416264195' || (s4dmessage.author.id) == '742014652611035166')) {
        s4dmessage.channel.send(String('Toi ta gueule.'));
    }

});

s4d.client.on('message', async (s4dmessage) => {
    arguments2 = (s4dmessage.content).split(' ');
    command = arguments2.splice(0, 1)[0];
    if (command == 'e!say') {
        s4dmessage.channel.send(String('t\'es con ou quoi? **ECRIT** '));
        s4dmessage.channel.send(String((arguments2.join(' '))));
    }

});

s4d.client.login(process.env.TOKEN).catch((e) => {
    s4d.tokenInvalid = true;
    s4d.tokenError = e;
});

s4d.client.on('message', async (s4dmessage) => {
    if (((s4dmessage.content) || '').startsWith('**Profil de el2zay#0364**' || '')) {
        s4dmessage.delete();
    }

});

s4d.client.on('message', async (s4dmessage) => {
    if ((s4dmessage.content) == 'e!number') {
        s4dmessage.channel.send(String((mathRandomInt(1, 100))));
    }

});



s4d.client.on('message', async (s4dmessage) => {
    if ((String((s4dmessage.content)).includes(String('Tu ne peux pas manger tout ca ! Tu va devenir gros ! Prend en moins stp et adapte combien tu prend en fonction de si tu a faim ou pas !'))) && (s4dmessage.author.id) == '550404246290563072') {
        s4dmessage.channel.send(String('JE MANGE CE QUE JE VEUX TU VAS RIEN FAIRE imbecile'));
    }

});

s4d.client.on('message', async (s4dmessage) => {
    if ((s4dmessage.content) == 'e!restart' && (s4dmessage.author.id) == '727572859727380531') {
        s4dmessage.channel.send(String('Je redémarre tkt'));
    } else if ((s4dmessage.content) == 'e!restart' && (s4dmessage.author.id) == '670753544416264195') {
        s4dmessage.channel.send(String('NAN JE REDÉMARRE PAS SALE ARABE '));
    } else if ((s4dmessage.content) == 'e!restart' && (s4dmessage.author.id) != '727572859727380531' || (s4dmessage.content) == 'e!restart' && (s4dmessage.author.id) != '670753544416264195') {
        s4dmessage.channel.send(String('NAN JE REDÉMARRE PAS'));
    }

});

s4d.client.on('message', async (s4dmessage) => {
    if ((s4dmessage.content) == 'e!infoserver') {
        s4dmessage.channel.send({
            embed: {
                title: 'Voici les informations sur ce serveur',
                color: '#33ffff',
                image: {
                    url: null
                },

                description: (['', '\n', 'Nom du seveur: ', (s4dmessage.guild).name, '\n', 'Nombre de personnes sur ce serveur: ', (s4dmessage.guild).memberCount, '\n', 'Propriétaire de ce serveur: ', (s4dmessage.guild).owner || await (s4dmessage.guild).members.fetch((s4dmessage.guild).ownerID), '\n', 'Niveau de boost de ce serveur: ', (s4dmessage.guild).premiumTier, '\n'].join('')),
                footer: {
                    text: null
                },
                thumbnail: {
                    url: ((s4dmessage.guild).iconURL({
                        dynamic: true
                    }))
                }

            }
        });
    }

});

s4d;