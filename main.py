import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Dropshipping AI Bot\n\nCommands:\n/top10 - Get 10 product ideas"
    )

async def top10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    products = """
🔥 Top 10 Dropshipping Product Ideas

1. Portable Blender
2. LED Sunset Lamp
3. Pet Hair Remover Roller
4. Smart Posture Corrector
5. Magnetic Phone Charger
6. Mini Projector
7. Dog Paw Cleaner
8. Car Interior LED Lights
9. Automatic Soap Dispenser
10. Foldable Laptop Stand
"""
    await update.message.reply_text(products)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("top10", top10))

app.run_polling()
