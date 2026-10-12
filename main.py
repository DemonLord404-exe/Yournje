import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"NC Guard شغال - {bot.user}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 10):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"تم مسح {amount}", delete_after=3)

bot.run(os.getenv("TOKEN"))
