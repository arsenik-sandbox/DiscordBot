import discord
from discord.ext import commands
from telegram import Bot as TelegramBot

DISCORD_BOT_TOKEN = 'DISCORD_BOT_TOKENİN'
TELEGRAM_BOT_TOKEN = 'TELEGRAM_BOT_TOKENİN'
TELEGRAM_CHAT_ID = 'TELEGRAM_CHAT_ID'

telegram_bot = TelegramBot(token=TELEGRAM_BOT_TOKEN)

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı.')

@bot.event
async def on_presence_update(before, after):
    if before.activities == after.activities:
        return

    for activity in after.activities:
        if isinstance(activity, discord.Game):  # Oyun aktivitesi
            message = f"{after.name} adlı kullanıcı şimdi '{activity.name}' oynuyor!"
            telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

bot.run(DISCORD_BOT_TOKEN)
