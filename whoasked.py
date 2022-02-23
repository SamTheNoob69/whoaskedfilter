import discord
from fuzzywuzzy import fuzz
from fuzzywuzzy import requests
import random

@client.event
async def on_message(message):
    RESPONSES = ["Don't mention me!", "Stop mentioning me!", "I won't repeat it, DON'T MENTION ME!!!"]
    CHARACTERS =["Stop spamming characters kid...", "Don't spam characters.", "Can you not?"]
    ASKED = ["I asked.", "Your Mom?", "Dogs don't ask, They listen.", "Excuse me? I DID!", f"?ban {message.author.mention} ???", "Don't need permission...", "If you didn't ask, Then why are you listening?", "Who said you were apart of the conversation?!", "You just asked who asked...", "Your lost dad", "100% Not your dad.", "It's not a Q&A."]
    for word in message.content.split(" "):
        temp_l=""
        i=0
        max_i = 5
        for l in word:
            if i >= max_i:
                return await message.reply(f'{random.choice(CHARACTERS)}')
            if l == temp_l:
                i += 1
            temp_l = l
    print(fuzz.ratio("who asked", message.content))
    if message.author.bot:
        return
    if fuzz.ratio("who asked", message.content) in range(38, 101) or fuzz.ratio("WHO ASKED", message.content) in range(38, 101):
        await message.reply(f'{random.choice(ASKED)}')
        
    await client.process_commands(message)
    if "WhoAsked" in message.content or "Who Asked" in message.content:
        await message.reply(f'{random.choice(ASKED)}')
    if client.user in message.mentions or "Saya" in message.content:
        await message.reply(f'{random.choice(RESPONSES)}')
        
