from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Define a start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm Mohammad Elias's Assistant bot. How can I help you?")
    

async def introduce(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("He is currently studying Govt. City College Chattogram.")
    

async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_location(latitude=23.730658,longitude=90.408653)
    

async def picture(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(photo=open('heart.png','rb'))

# Define a reply handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)
    await update.message.reply_text(f'You said: {text}')

# Main function to start the bot
def main():
    # Replace 'YOUR_TOKEN' with the token from BotFather
    TOKEN = "7589982321:AAEx5z-BZZyqXElVni4oCON1xUGREpzDwWc"

    # Create the application
    application = Application.builder().token(TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("intro", introduce))
    application.add_handler(CommandHandler("location", location))
    application.add_handler(CommandHandler("photo", picture))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
