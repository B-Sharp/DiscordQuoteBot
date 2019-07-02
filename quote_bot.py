import json
import discord
import random

# loads a list of quotes from quotes.json
with open("quotes.json", "r") as qf:
    quotes_json = json.load(qf)
    quotes = quotes_json["quotes"]

# loads bot token from config.json
with open("config.json", "r") as cf:
    config_json = json.load(cf)
    bot_token = config_json["token"]

# loads a list of sound filenames from sounds.json
with open("sounds.json", "r") as sf:
    sounds_json = json.load(sf)
    sounds = sounds_json["sounds"]

# pairs each quote with its sound filename
mapped_pairs = list(zip(quotes, sounds))

# create a client
client = discord.Client()

# register a message event listener
@client.event
async def on_message(msg):
    # ignore messages from itself and other bots
    if msg.author == client.user or msg.author.bot:
        return
    
    # if the bot is mentioned select a random quote and send it
    for mention in msg.mentions:
        if mention == client.user:
            random_pair = random.choice(mapped_pairs)
            await msg.channel.send(random_pair[0])
            voice_client = await msg.author.voice.channel.connect();
            voice_client.play(discord.FFmpegPCMAudio("sounds\\" + random_pair[1]), after=lambda e: voice_client.loop.create_task(voice_client.disconnect()))

# run the bot
client.run(bot_token)