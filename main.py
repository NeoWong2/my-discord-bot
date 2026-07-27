import discord
from discord.ext import commands
from discord import app_commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

game_data = {}

@bot.event
async def on_ready():
    print(f'娛樂小龜龜已在雲端啟動：{bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"成功同步了 {len(synced)} 個斜線指令！")
    except Exception as e:
        print(f"同步錯誤: {e}")

@bot.tree.command(name="嗨", description="讓小龜龜熱情地跟群友打招呼")
async def hello(interaction: discord.Interaction):
    welcomes = ["歡迎來到最讚的聊天群！🎉", "嗨！今天想找小龜龜聊點什麼？🐢", "哈囉！祝你今天在群組玩得開心！✨"]
    await interaction.response.send_message(f"{interaction.user.mention} {random.choice(welcomes)}")

@bot.tree.command(name="吃什麼", description="不知道吃什麼？讓小龜龜幫群友決定")
async def food(interaction: discord.Interaction):
    options = ["拉麵 🍜", "滷肉飯 🍚", "火鍋 🍲", "麥當勞 🍔", "牛排 🥩", "炸雞 🍗", "壽司 🍣", "麻辣燙 🌶️"]
    await interaction.response.send_message(f"🐢 小龜龜幫你決定好了，今天吃：**{random.choice(options)}**！")

@bot.tree.command(name="真心話大冒險", description="派對破冰必備！隨機抽選題目")
@app_commands.choices(類型=[
    app_commands.Choice(name="真心話", value="truth"),
    app_commands.Choice(name="大冒險", value="dare")
])
async def party_game(interaction: discord.Interaction, 類型: app_commands.Choice[str]):
    truths = ["你手機裡最尷尬的照片是什麼？", "你對現場的哪個人印象最好？", "你人生中做過最丟臉的一件事是什麼？"]
    dares = ["用最深情的方式對群組裡的一個人告白 30 秒！", "把頭像換成搞笑迷因圖一天！", "在群組裡用語音訊息唱一首歌！"]
    result = random.choice(truths) if 類型.value == "truth" else random.choice(dares)
    await interaction.response.send_message(f"🎲 **【真心話大冒險 - {類型.name}】** 分配給 {interaction.user.mention}：\n👉 挑戰內容：*{result}*")

@bot.tree.command(name="冷笑話", description="小龜龜講一個超冷乾笑話")
async def joke(interaction: discord.Interaction):
    jokes = [
        "小明不小心吞下了一顆鹽，結果他就被「鹹（閒）」置了。🤣",
        "什麼動物最容易摔倒？答案是：狐狸，因為狐狸狡（腳）猾。🦊",
        "有一天，綠豆撞到牆壁變成什麼？答案是：紅豆，因為它撞出血了。🫘"
    ]
    await interaction.response.send_message(f"💬 {random.choice(jokes)}")

@bot.tree.command(name="終極密碼開始", description="在群組開啟一場猜數字小遊戲（1~100）")
async def start_game(interaction: discord.Interaction):
    channel_id = interaction.channel_id
    secret_num = random.randint(1, 100)
    game_data[channel_id] = {"answer": secret_num, "min": 1, "max": 100}
    await interaction.response.send_message(f"🎮 **終極密碼遊戲開始！**\n數字範圍：**1 ~ 100**，請群友們使用 `/猜數字` 指令開始作答！")

@bot.tree.command(name="猜數字", description="輸入你猜的數字來玩終極密碼")
async def guess_number(interaction: discord.Interaction, 數字: int):
    channel_id = interaction.channel_id
    if channel_id not in game_data:
        await interaction.response.send_message("❌ 本頻道目前沒有正在進行的遊戲，請先輸入 `/終極密碼開始`！", ephemeral=True)
        return
    game = game_data[channel_id]
    ans = game["answer"]
    if 數字 <= game["min"] or 數字 >= game["max"]:
        await interaction.response.send_message(f"⚠️ 超過目前範圍了啦！目前的範圍是 **{game['min']} ~ {game['max']}** 喔！", ephemeral=True)
        return
    if 數字 == ans:
        await interaction.response.send_message(f"💥 **蹦！！！** {interaction.user.mention} 猜中了密碼 **{ans}**！引爆炸彈！💀")
        del game_data[channel_id]
    elif 數字 < ans:
        game["min"] = 數字
        await interaction.response.send_message(f"📉 太小了！目前的最新範圍變更為：**{game['min']} ~ {game['max']}**")
    else:
        game["max"] = 數字
        await interaction.response.send_message(f"📈 太大了！目前的最新範圍變更為：**{game['min']} ~ {game['max']}**")

@bot.tree.command(name="求籤", description="向小龜龜月老/神明求一支今日運勢籤")
async def draw_lots(interaction: discord.Interaction):
    lots = ["【大吉 🌟】運勢如日中天！", "【上吉 👍】平平安安超穩健！", "【下籤 🌧️】今天留在群組聊天取暖吧！"]
    await interaction.response.send_message(f"🔮 {interaction.user.mention} 誠心跪求得一籤：\n📋 **{random.choice(lots)}**")

token = os.environ.get("DISCORD_TOKEN")
bot.run(token)
