import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env")


# Replace TOKEN with your bot token
TOKEN = os.getenv("DISCORD_TOKEN") 

# Replace CHANNEL_ID with the ID of the channel you want to monitor
CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID") 

# Replace WEBHOOK_MESSAGE with the specific message from the webhook that triggers the deletion
WEBHOOK_MESSAGE = 'leaderboard'

intents = discord.Intents.default()  # Start with the default intents
intents.messages = True  # Enable the message intent for managing messages
intents.message_content = True  # Add this line to include the message_content intent
intents.guilds = True  # Enable the guilds intent, often necessary for context

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
        
    # if message.content == WEBHOOK_MESSAGE:
    if message.content == "leaderboard":
        channel = bot.get_channel(int(CHANNEL_ID))
        await delete_all_messages(channel)
        # resend the message w/o content so leaderbord does not get deleted
        await channel.send(embed=message.embeds[0])
        
async def delete_all_messages(channel):
    print("Deleting messages...")
    async for msg in channel.history(limit=None):
        if not msg.pinned:
            try:
                await msg.delete()
            except discord.Forbidden:
                print(f'Unable to delete message: {msg.content}')


bot.run(TOKEN)
