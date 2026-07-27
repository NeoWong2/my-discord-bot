import discord
from discord.ext import commands
from discord import app_commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 當機器人準備好時，同步斜線指令到 Discord
@bot.event
async def on_ready():
    print(f'機器人已上線：{bot.user}')
    try:
        # 同步全球指令（通常需要幾分鐘生效）
        synced = await bot.tree.sync()
        print(f"成功同步了 {len(synced)} 個斜線指令！")
    except Exception as e:
        print(f"同步指令時發生錯誤: {e}")

# 指令 1：/ping
@bot.tree.command(name="ping", description="測試機器人延遲")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('pong! 🐢')

# 指令 2：/嗨
@bot.tree.command(name="嗨", description="讓小龜龜跟你打招呼")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"你好啊 {interaction.user.name}！我是小龜龜 🐢")

# 指令 3：/吃什麼
@bot.tree.command(name="吃什麼", description="讓小龜龜決定你今天吃什麼")
async def food(interaction: discord.Interaction):
    options = ["拉麵 🍜", "滷肉飯 🍚", "火鍋 🍲", "麥當勞 🍔", "牛排 🥩", "炸雞 🍗", "壽司 🍣"]
    await interaction.response.send_message(f"🐢 小龜龜建議你今天吃：**{random.choice(options)}**")

# 指令 4：/運勢
@bot.tree.command(name="運勢", description="占卜你今天的運勢")
async def fortune(interaction: discord.Interaction):
    fortunes = ["大吉 🌟", "吉 👍", "中吉 ☀️", "末吉 ☁️", "凶 🌧️"]
    await interaction.response.send_message(f"🔮 【{interaction.user.name} 的運勢】：**{random.choice(fortunes)}**")

# 指令 5：/擲骰子
@bot.tree.command(name="擲骰子", description="文字 RPG 擲骰子 (1到100)")
async def dice(interaction: discord.Interaction):
    score = random.randint(1, 100)
    result = "大成功！👑" if score >= 90 else "成功！👌" if score >= 50 else "失敗了...💪"
    await interaction.response.send_message(f"🎲 {interaction.user.name} 擲出了 **{score}** 點！\n判定結果：{result}")

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)
