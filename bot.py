import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {🫧⋆｡˚}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello from Railway!")

bot.run(os.getenv("MTM3Njg4NjcxMDg1OTcyNjkzMA.G5hgm1.ENLdfQjugpahZO-2EhlBkOXBkjwwn_ZrUxouvw"))
