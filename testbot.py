from telegram.ext import Updater, CommandHandler
from telegram import Bot, Update

def start (bot, update):
	update.message.reply_text("This is a test bot")
	
def spam (bot, update):
	update.message.reply_text("spam"*1000)
	
def id (bot, update):
	update.message.reply_text("{} is your telegram id." .format(update.message.from_user.id))
	
updater = Updater ('673991720:AAE4kB1C3ghJeuhelfJE8HZ_mpSOJS6ZuwE')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('id', id))
updater.dispatcher.add_handler(CommandHandler('spam', spam))

updater.start_polling()
updater.idle()