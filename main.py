import os
import urllib.parse
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from openai import OpenAI

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_KEY)

def research_links(query: str) -> str:
    q = urllib.parse.quote(query)
    return (
        "🔗 Research links:\n"
        f"• TikTok Creative Center: https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en?search={q}\n"
        f"• Meta Ads Library: https://www.facebook.com/ads/library/?q={q}\n"
        f"• Google Trends: https://trends.google.com/trends/explore?q={q}\n"
        f"• AliExpress search: https://www.aliexpress.com/wholesale?SearchText={q}\n"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Dropshipping AI Bot\n\n"
        "Commands:\n"
        "/top10 <country> <niche> - AI top 10 products + links\n\n"
        "Example:\n"
        "/top10 UAE fitness"
    )

async def top10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get optional arguments
    args = context.args
    country = args[0] if len(args) >= 1 else "US"
    niche = " ".join(args[1:]) if len(args) >= 2 else "general"

    await update.message.reply_text("🔥 Generating AI Top 10…")

    prompt = (
        f"Generate 10 dropshipping product ideas for Country={country}, Niche={niche}.\n"
        "For each product return:\n"
        "1) Product name\n"
        "2) 1-line why it works\n"
        "3) Suggested selling price range\n"
        "4) 2 ad angles\n"
        "Keep it realistic. Avoid branded/trademark items and medical claims.\n"
        "Format as a numbered list 1-10."
    )

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    text = resp.choices[0].message.content.strip()

    # Telegram message limit safety
    await update.message.reply_text(text[:3500])
    await update.message.reply_text(research_links(f"{niche} product"))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("top10", top10))
app.run_polling()
