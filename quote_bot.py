import json
import discord
import random

# loads a list of quotes from quotes.json
quote_file = open("quotes.json", "r")
quote_json = json.load(quote_file)
quotes = quote_json["quotes"]
quote_file.close()

# loads bot token from config.json
config_file = open("config.json", "r")
config_json = json.load(config_file)
bot_token = config_json["token"]
config_file.close()

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
            random_quote = random.choice(quotes)
            await msg.channel.send(random_quote)

# run the bot
client.run(bot_token)