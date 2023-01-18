import asyncio
import discord
import logging
import coloredlogs
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN          = config['ACCOUNT']['TOKEN']
WORDLIST       = config['BOT']['WORDLIST']
SEPARATOR      = str(config['BOT']['SEPARATOR'])
START_WORD     = config['BOT']['BOT_START']
STOP_WORD      = config['BOT']['BOT_STOP']
DELAY          = int(config['BOT']['DELAY'])
LOOP           = int(config['BOT']['LOOP'])
LOGGING        = config['LOGGING'].getboolean('LOGGING')
LOGGING_LEVEL  = int(config['LOGGING']['LOGGING_LEVEL'])
LOG_FILE       = config['LOGGING']['LOG_FILE']

if LOGGING:
    logger = logging.getLogger('discord')
    logger.setLevel(LOGGING_LEVEL)
    handler = logging.FileHandler(filename=LOG_FILE, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    coloredlogs.install()

def get_sentences():
    with open(f'wordlist/{WORDLIST}', 'r') as f:
        return f.read().split('\n\n')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        counter = 0
        # only respond to ourselves
        if message.author != self.user:
            return

        if message.content == START_WORD:
            while counter < LOOP:
                if message.content == STOP_WORD:
                    break

                for word in get_sentences():
                    try:
                        await message.channel.send(word)
                        await asyncio.sleep(DELAY)
                    except Exception as e:
                        pass
                counter += 1

client = MyClient()
client.run(TOKEN)