import discord 
from discord.ext.commands import Bot
from dotenv import load_dotenv
import os
from AlwaysRunningServer import StartServer
import asyncio
bot = Bot()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!\nID: {bot.user.id}\nPing: {bot.latency * 1000}ms\nMaking sure the bot will be online if its runing on Replit...')
    if not os.getenv('REPL_ID') == None:
        StartServer()
        print("Server is running,bot will be running")
    await bot.change_presence(activity=discord.Game(name="Making sure no *Ghost Ping!* message will be there..."))

@bot.event
async def on_message(message):
    if message.author.id == 778607630515306497 and message.embeds and message.embeds[0].title.startswith("Ghost Pinged!"):
        await message.delete()
        m = await message.send("Ghost Pinged! message has been deleted")
        await asyncio.sleep(2)
        await m.delete()

bot.run(TOKEN)
    
    

 