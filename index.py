from telegram.ext import Updater, MessageHandler, Filters

# List of profanity words to filter
profanity_list = ['fuck', 'damn', 'ass', 'bitch']  # Add more words as needed

# Function to filter messages
def filter_messages(update, context):
    message_text = update.message.text.lower()  # Convert message text to lowercase for case-insensitive filtering
    for word in profanity_list:
        if word in message_text:
            # If a profanity word is found, delete the message
            update.message.delete()
            return

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater("YOUR_API_TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the message handler with the profanity filter
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), filter_messages))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()

