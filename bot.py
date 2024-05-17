import os
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Logger setup
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

intents = discord.Intents.default()  # Start with the default intents
intents.messages = True  # Enable the message intent for managing messages
intents.message_content = True  # Add this line to include the message_content intent
intents.guilds = True  # Enable the guilds intent, often necessary for context

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='test')
async def test(ctx):
    logger.info(f""" 
            📌 TEST funciton
    """)

    await ctx.send("test")

@bot.command(name='add_user')
async def quiz(ctx):
    CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")

    msgs = [
        "question 1",
        "question 2",
        "🧨🧨🧨 ALL DONE! \n\n 🦑    Sending a return message will delete this history ...",
    ]
    
    # restrict the bot command to the recruit discord chanel ID
    if str(ctx.channel.id) == CHANNEL_ID:
        channel = bot.get_channel(int(CHANNEL_ID))

        await ctx.send(msgs[0])
        response = await bot.wait_for('message', check=lambda m: m.author == ctx.author)

        logger.info(f""" 
                📌 responce: {response} msg: {msgs[0]}
        """)

        logger.info(f""" 
                🦑 doing some work ...
        """)

        await ctx.send(msgs[1])
        response = await bot.wait_for('message', check=lambda m: m.author == ctx.author)

        logger.info(f""" 
                📌 responce: {response} msg: {msgs[1]}
        """)

        logger.info(f""" 
                🦑 doing some work ...
        """)

        await ctx.send(msgs[2])
        response = await bot.wait_for('message', check=lambda m: m.author == ctx.author)

        logger.info(f""" 
                📌 Deleting messages...
        """)
        async for msg in channel.history(limit=(len(msgs)*2)+1):
            if not msg.pinned:
                try:
                    await msg.delete()
                except discord.Forbidden:
                    print(f'Unable to delete message: {msg.content}')
    else:
        await ctx.send(f"... this bot only work on recruit channels ...")


bot.run(os.getenv("DISCORD_TOKEN")) 
