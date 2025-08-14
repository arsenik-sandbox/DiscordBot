import discord
from telegram import Bot as TelegramBot

DISCORD_BOT_TOKEN = ""
TELEGRAM_BOT_TOKEN = ""
TELEGRAM_CHAT_ID = ""

telegram_bot=TelegramBot (token=TELEGRAM_BOT_TOKEN)
intents = discord.intents.default()
intents.presences = True
intents.members = True

@bot.event

async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı.'}

@bot.event
async def on_presence_update(before, after):

if before.activities == after.activities:
    return

for activity in after.activities:
    if instance(activity, discord.Game):
        message = f"{after.name} adlı kullanıcı şimdi '{activity.name}' oynuyor!"
        print(message)
        telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
