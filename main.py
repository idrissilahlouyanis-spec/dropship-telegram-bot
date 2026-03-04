import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from openai import OpenAI

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Dropshipping AI Bot\n\n"
        "Commands:\n"
        "/top10 - Find winning dropshipping products"
    )

async def top10(update: Update, context: ContextTypes.DEFAULT_TYPE):

    prompt = "Give me 10 winning dropshipping products in 2026 with short explanation."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content

    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("top10", top10))

app.run_polling()
