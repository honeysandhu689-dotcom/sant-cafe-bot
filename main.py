import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# आपका टेलीग्राम टोकन
TOKEN = '8416473312:AAF7PqDkqJC5xK9i_eD9sQMWTyp6bqKZ14c'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_url = "https://i.ibb.co/v4m0Yv8/SANT-CAFE.jpg"
    keyboard = [
        [InlineKeyboardButton("🆔 आधार/पैन कार्ड जानकारी", callback_data='docs')],
        [InlineKeyboardButton("📱 नए मोबाइल के ताज़ा रेट", callback_data='phones')],
        [InlineKeyboardButton("💬 व्हाट्सएप पर बात करें", url='https://wa.me/919815096000')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    msg = (
        "🏪 **SANT INTERNET CAFÉ & MOBILE STORE** 🙏\n"
        "संचालक: **Manjot Singh**\n"
        "-------------------------------------\n"
        "नमस्ते! हमारे यहाँ आधार, पैन कार्ड और सभी नए मोबाइल मिलते हैं।\n\n"
        "📍 **पता:** दोराहा (Doraha), भूतवाला लोकेशन के पास।\n"
        "📞 **संपर्क:** 9815096000\n"
        "-------------------------------------\n"
        "मदद के लिए नीचे दिए गए बटन दबाएं 👇"
    )
    try:
        await update.message.reply_photo(photo=photo_url, caption=msg, reply_markup=reply_markup, parse_mode='Markdown')
    except:
        await update.message.reply_text(msg, reply_markup=reply_markup, parse_mode='Markdown')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'docs':
        text = "📄 **दस्तावेज़:** नया पैन कार्ड (आधार + 2 फोटो), आधार अपडेट (पुराना आधार लाएँ)।"
    else:
        text = "📱 **मोबाइल:** सभी ब्रांड उपलब्ध हैं। रेट के लिए व्हाट्सएप करें।"
    await query.message.reply_text(text, parse_mode='Markdown')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling(drop_pending_updates=True)
