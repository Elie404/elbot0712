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

function mathRandomInt(a, b) {
    if (a > b) {
        // Swap a and b to ensure a is smaller.
        var c = a;
        a = b;
        b = c;
    }
    return Math.floor(Math.random() * (b - a + 1) + a);
}


s4d.client.login(process.env.TOKEN).catch((e) => {
    s4d.tokenInvalid = true;
    s4d.tokenError = e;
});

s4d.client.on('message', async (s4dmessage) => {
    if ((s4dmessage.content) == 'e!number') {
        s4dmessage.channel.send(String((mathRandomInt(1, 100))));
    }

});

s4d.client.on('message', async (s4dmessage) => {
    if ((s4dmessage.content) == 'e!infoserver') {
        s4dmessage.channel.send({
            embed: {
                title: 'Voici les informations sur ce serveur',
                color: '#33ffff',
                image: {
                    url: ((s4dmessage.guild).iconURL({
                        dynamic: true
                    }))
                },
                description: (['', '\n', 'Nom du seveur:', (s4dmessage.guild).name, '\n', 'Nombre de personnes sur ce serveur', (s4dmessage.guild).memberCount, '\n', (s4dmessage.guild).owner || await (s4dmessage.guild).members.fetch((s4dmessage.guild).ownerID), 'Propriétaire de ce serveur', '\n', (s4dmessage.guild).premiumTier, ''].join(''))
            }
        });
    }

});

s4d;