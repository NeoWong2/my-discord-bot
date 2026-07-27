import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'機器人已上線：{bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)
import discord
from discord.ext import commands
import os
import random

# 設定機器人的指令前綴與權限
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'機器人已上線：{bot.user}')

# 指令 1：基礎測試
@bot.command()
async def ping(ctx):
    await ctx.send('pong! 🐢')

# 指令 2：暖心問候
@bot.command()
async def 嗨(ctx):
    responses = [
        f"你好啊 {ctx.author.name}！今天過得好嗎？🐢",
        f"嗨！我是小龜龜，很高興見到你！✨",
        f"哈囉 {ctx.author.name}，今天又是美好的一天！🎒"
    ]
    await ctx.send(random.choice(responses))

# 指令 3：隨機決定晚餐/午餐
@bot.command()
async def 吃什麼(ctx):
    options = [
        "香噴噴的拉麵 🍜", "經典滷肉飯加蛋 🍚", "熱騰騰的火鍋 🍲", 
        "美味的麥當勞 🍔", "鮮嫩多汁的牛排 🥩", "便利商店簡單吃 🏪",
        "香脆可口的炸雞 🍗", "美味的日式壽司 🍣"
    ]
    choice = random.choice(options)
    await ctx.send(f"🐢 小龜龜掐指一算，建議你今天吃：**{choice}**")

# 指令 4：每日運勢占卜
@bot.command()
async def 運勢(ctx):
    fortunes = ["大吉 🌟 萬事如意，走路都會撿到錢！", "吉 👍 平平安安，會遇到好事情喔！", "中吉 ☀️ 運氣不錯，適合挑戰新事物！", "末吉 ☁️ 普普通通，今天就放鬆度過吧！", "凶 🌧️ 出門記得帶傘，多喝水沒事的！"]
    await ctx.send(f"🔮 【{ctx.author.name} 的今日運勢】\n結果是：**{random.choice(fortunes)}**")

# 指令 5：文字 RPG 擲骰子 (1到100)
@bot.command()
async def 擲骰子(ctx):
    score = random.randint(1, 100)
    if score >= 90:
        result = "大成功！簡直是神之右手！👑"
    elif score >= 50:
        result = "成功！表現得可圈可點。👌"
    else:
        result = "失敗了...下次再接再厲！💪"
    await ctx.send(f"🎲 {ctx.author.name} 擲出了 **{score}** 點！\n判定結果：{result}")

# 指令 6：學人精 (機器人會重複你說的話)
# 使用方法：!重複 大家好啊
@bot.command()
async def 重複(ctx, *, message: str):
    await ctx.send(message)

# 讀取雲端環境變數中的 Token
token = os.environ.get("DISCORD_TOKEN")
bot.run(token
