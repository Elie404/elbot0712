const Discord = require("discord.js");
const Canvas = require("canvas");

const client = new Discord.Client();

client.once("ready", () => {
  console.log("Ready!");
});

client.on("guildMemberAdd", async member => {
  const channel = member.guild.channels.cache.find(
    ch => ch.id === "865914342545424407"
  );
  if (!channel) return;

  channel.send(`Bienvenue sur le serveur Elbot Test, ${member}!`);
  // ...
  if (!channel) return;

  // Create a 700x250 pixels canvas and get its context
  // The context will be used to modify the canvas
  const canvas = Canvas.createCanvas(700, 250);
  const context = canvas.getContext("2d");
  // ...
  // ...

  // Since the image takes time to load, you should await it
  const background = await Canvas.loadImage("./wallpaper.jpg");
  // This uses the canvas dimensions to stretch the image onto the entire canvas
  context.drawImage(background, 0, 0, canvas.width, canvas.height);
  // Use the helpful Attachment class structure to process the file for you
  const attachment = new Discord.MessageAttachment(
    canvas.toBuffer(),
    "welcome-image.png"
  );

  // ...
  context.drawImage(background, 0, 0, canvas.width, canvas.height);

  // Set the color of the stroke
  context.strokeStyle = "#74037b";
  // Draw a rectangle with the dimensions of the entire canvas
  context.strokeRect(0, 0, canvas.width, canvas.height);
  // ...

  // ...

  // Wait for Canvas to load the image
  const avatar = await Canvas.loadImage(
    member.user.displayAvatarURL({ format: "jpg" })
  );
  // Draw a shape onto the main canvas
  context.drawImage(avatar, 25, 0, 200, canvas.height);
  // ...
  // ...

  // Move the image downwards vertically and constrain its height to 200, so that it's square
  context.drawImage(avatar, 25, 25, 200, 200);
  // ...

  // ...
  context.strokeRect(0, 0, canvas.width, canvas.height);

  // Pick up the pen
  context.beginPath();
  // Start the arc to form a circle
  context.arc(125, 125, 100, 0, Math.PI * 2, true);
  // Put the pen down
  context.closePath();
  // Clip off the region you drew on
  context.clip();
  // ...

  // ...
  context.strokeRect(0, 0, canvas.width, canvas.height);

  // Select the font size and type from one of the natively available fonts
  context.font = "60px sans-serif";
  // Select the style that will be used to fill the text in
  context.fillStyle = "#ffffff";
  // Actually fill the text with a solid color
  context.fillText(member.displayName, canvas.width / 2.5, canvas.height / 1.8);
  // ...

// Pass the entire Canvas object because you'll need access to its width and context
const applyText = (canvas, text) => {
  const context = canvas.getContext("2d");

  // Declare a base size of the font
  let fontSize = 70;

  do {
    // Assign the font to the context and decrement it so it can be measured again
    context.font = `${(fontSize -= 10)}px sans-serif`;
    // Compare pixel width of the text to the canvas minus the approximate avatar size
  } while (context.measureText(text).width > canvas.width - 300);

  // Return the result to use in the actual canvas
  return context.font;
};

// ...
context.strokeRect(0, 0, canvas.width, canvas.height);

// Assign the decided font to the canvas
context.font = applyText(canvas, member.displayName);
context.fillStyle = "#ffffff";
context.fillText(member.displayName, canvas.width / 2.5, canvas.height / 1.8);
// ...
// ...
context.strokeRect(0, 0, canvas.width, canvas.height);

// Slightly smaller text placed above the member's display name
context.font = "28px sans-serif";
context.fillStyle = "#ffffff";
context.fillText(
  "Welcome to the server,",
  canvas.width / 2.5,
  canvas.height / 3.5
);

// Add an exclamation point here and below
context.font = applyText(canvas, `${member.displayName}!`);
context.fillStyle = "#ffffff";
context.fillText(
  `${member.displayName}!`,
  canvas.width / 2.5,
  canvas.height / 1.8
);
// ...

channel.send(`Welcome to the server, ${member}!`, attachment);

  });

client.on("message", message => {
  if (message.content === "!join") {
    client.emit("guildMemberAdd", message.member);
  }
});

client.login("ODA5MzQ0OTA1Njc0NDg5ODY2.YCTvLg.U640p8gdna3OhqFz-pz9rJHdA9o");
