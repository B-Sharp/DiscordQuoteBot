import json
import discord
import random

def main():
    # loads a list of quotes from quotes.json
    with open("quotes.json", "r") as qf:
        quotes_json = json.load(qf)
        quotes = quotes_json["quotes"]

    # loads bot token from config.json
    with open("config.json", "r") as cf:
        config_json = json.load(cf)
        bot_token = config_json["token"]

    # create a client
    client = discord.Client()

    # register a message event listener
    @client.event
    async def on_message(msg):
        # ignore messages from itself and other bots
        if msg.author == client.user or msg.author.bot:
            return
        
        # if the bot is mentioned select a random quote and send it then play the audio for that quote
        for mention in msg.mentions:
            if mention == client.user:
                random_quote = random.choice(list(quotes))
                
                # check if the user is not in any channel or if the bot is already connected to the channel
                if msg.author.voice is None or client.user not in msg.author.voice.channel.members:
                    await msg.channel.send(random_quote)
                    
                    # check if the quote has a sound file
                    if quotes[random_quote]:
                        voice_client = await msg.author.voice.channel.connect();
                        voice_client.play(discord.FFmpegPCMAudio("sounds\\" + quotes[random_quote]), after=lambda e: voice_client.loop.create_task(voice_client.disconnect()))

    # run the bot
    client.run(bot_token)

if __name__ == "__main__":
    main()