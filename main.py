import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'機器人已上線：{bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('pong! 🐢')

@bot.command()
async def 嗨(ctx):
    await ctx.send(f"你好啊 {ctx.author.name}！我是小龜龜 🐢")

@bot.command()
async def 吃什麼(ctx):
    options = ["拉麵 🍜", "滷肉飯 🍚", "火鍋 🍲", "麥當勞 🍔", "牛排 🥩", "炸雞 🍗"]
    await ctx.send(f"🐢 小龜龜建議你吃：**{random.choice(options)}**")

@bot.command()
async def 運勢(ctx):
    fortunes = ["大吉 🌟", "吉 👍", "中吉 ☀️", "末吉 ☁️", "凶 🌧️"]
    await ctx.send(f"🔮 【{ctx.author.name} 的運勢】：**{random.choice(fortunes)}**")

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)
