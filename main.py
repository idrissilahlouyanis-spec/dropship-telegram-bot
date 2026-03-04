import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Your Dropshipping Bot is working!")

async def top10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Top 10 dropshipping products coming soon!")

async def validate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send the product link you want to analyze.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("top10", top10))
app.add_handler(CommandHandler("validate", validate))

app.run_polling()
