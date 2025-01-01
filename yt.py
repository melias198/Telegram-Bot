from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp
import tempfile

# Function to download video to a temporary file
def download_video(link):
    temp_file = tempfile.NamedTemporaryFile(delete=False)  # Create a temporary file
    ydl_opts = {
        'outtmpl': temp_file.name,  # Save video to the temporary file
        'format': 'best',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)  # Download the video
    return temp_file.name, info['title'], info['ext']

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a YouTube or Facebook link to download!")

# Handle links
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = update.message.text
    try:
        await update.message.reply_text("Downloading your video...")
        filepath, title, ext = download_video(link)

        # Send video to Telegram
        with open(filepath, 'rb') as video:
            await update.message.reply_video(video=video, filename=f"{title}.{ext}")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
    finally:
        import os
        if os.path.exists(filepath):
            os.remove(filepath)  # Clean up the temporary file

# Main function
def main():
    token = "7589982321:AAEx5z-BZZyqXElVni4oCON1xUGREpzDwWc"
    
    # Create the application
    application = Application.builder().token(token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
