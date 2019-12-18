# Discord Quote Bot
Discord Quote Bot is a simple discord bot designed to respond to mentions to itself with a random quote.

## How to use
In order to run the bot you must first install [discord.py](https://discordpy.readthedocs.io/en/latest/#). Next, download this repository and go to the [Discord Developer Portal](https://discordapp.com/developers/docs/intro) to register a bot application and add it to a server. Edit the example_config.json to include your bot's token and edit the example_quotes.json to include and quotes you would like the bot to say. Finally, remove the "example_" from both JSON file names and run "quote_bot.py" 

Any time the bot is mentioned directly using the @ symbol it will respond in that same channel with a random quote from quotes.json.

## Voice
In order to have the bot respond with some audio for each quote you must first have [ffmpeg](https://www.ffmpeg.org/) installed. Then you must create a sounds/ directory in the folder containing the script. In that directory, put all of the sound files you wish to use. Finally, for each entry in quotes.json, make the value associated with each quote the audio file name. If there is a quote that does not have an associated audio file, then leave that value as an empty string.