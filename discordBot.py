import discord
from discord.ext import commands
from telegram import Bot as TelegramBot

DISCORD_BOT_TOKEN = 'MTQwNTE0NDg1MjEyMjgyODg4MQ.GImYfp.eOBJ6zw2u863ylDjBH0PswfJ3IZ0kCurf9eltg'
TELEGRAM_BOT_TOKEN = '7541525260:AAFg8JsT10hZN5aW7wrwBZyoLwz5AWBve8c'
TELEGRAM_CHAT_ID = '-1002595889450' 

telegram_bot = TelegramBot(token=TELEGRAM_BOT_TOKEN)

intents = discord.Intents.default()
intents.presences = True
intents.members = True

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı.')

@bot.event
async def on_presence_update(before, after):
    if before.activities == after.activities:
        return

    for activity in after.activities:
        if isinstance(activity, discord.Game):
            message = f"{after.name} adlı kullanıcı şimdi '{activity.name}' oynuyor!"
            print(message)  
            telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

bot.run(DISCORD_BOT_TOKEN)
