import calendar
import logging

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import data
import secret_settings
import mergeimage
import GreetingCard
import effects
from io import BytesIO
global args_chat_id

logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(token=secret_settings.BOT_TOKEN)
dispatcher = updater.dispatcher

project = {}
dicargs = {}
photo_counter = {}
text_dic = {}
image_dic={}

def start(bot, update, args):
   chat_id = update.message.chat_id
   text_dic[chat_id] = ""
   if args:
       dicargs[chat_id] = int(args[0])
   else:
       dicargs[chat_id] = chat_id
       photo_counter[chat_id] = 0
   print(args)
   logger.info(f"> Start chat #{chat_id}")
   bot.send_message(chat_id=chat_id, text="Welcome !!!")
   if dicargs[chat_id] == chat_id:
       keyboard = [[InlineKeyboardButton("Collage", callback_data='Collage'),
                    InlineKeyboardButton("Calendar", callback_data='Calendar'),
                   InlineKeyboardButton("Greeting Card", callback_data='Greeting Card')]]
       reply_markup = InlineKeyboardMarkup(keyboard)
       update.message.reply_text('Please choose what you want to do:', reply_markup=reply_markup)
   else:
       bot.send_message(chat_id=chat_id, text="please apload photos")


def respond(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    logger.info(f"> Respond chat #{chat_id}")


def button(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    logger.info(f"> Button chat #{chat_id}")

    if query.data == 'Collage':
        project[chat_id] = 'Collage'
        keyboard = [[InlineKeyboardButton("Get Link", callback_data='Get Link')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=chat_id, text=f"ok. Ill do a {query.data} for you, Apload photos or press on the button to get a link to send to your friennd, so they will also apload pictures", reply_markup=reply_markup)

    if query.data == 'Calender':
        project[chat_id] = 'Calender'
        keyboard = [[InlineKeyboardButton("Get Link", callback_data='Get Link')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=chat_id, text=f"ok. Ill do a {query.data} for you, Apload photos or press on the button to get a link to send to your friennd, so they will also apload pictures", reply_markup=reply_markup)

    if query.data == 'Greeting Card':
        project[chat_id] = 'Greeting Card'
        keyboard = [[InlineKeyboardButton("Get Link", callback_data='Get Link')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=chat_id, text=f"ok. Ill do a {query.data} for you, Apload photos or press on the button to get a link to send to your friennd, so they will also apload pictures", reply_markup=reply_markup)

    if query.data == 'Get Link':
        logger.info(f"> Share chat #{chat_id}")
        bot.send_message(chat_id=chat_id, text="Send this link to your friends and apload more photos")
        bot.send_message(chat_id=chat_id, text=f" https://telegram.me/{secret_settings.BOT_NAME}?start={chat_id}")

    if query.data == 'Add Text':
        logger.info(f"> AddText chat #{chat_id}")
        bot.send_message(chat_id=chat_id, text="Please write your text:")

    if query.data == 'Finish':
        if project[chat_id] == 'Collage':
            logger.info(f"> end chat #{chat_id}")
            bot.send_message(chat_id=chat_id, text="ok, I will send your collage in few seconds")
            lst = data.load_image(chat_id)
            lst = mergeimage.cut_image(lst)
            im = mergeimage.create_collage(lst)
            img = mergeimage.print_on_image_collage(im, text_dic[chat_id])

            bio = BytesIO()
            bio.name = 'image.jpeg'
            img.save(bio, 'JPEG')
            bio.seek(0)
            bot.send_photo(chat_id, photo=bio)
            bot.send_message(chat_id=chat_id, text="Now you can choose an effect for your collage. (/effect) ")

            BlackWhite = effects.BlackWhite(img)
            Sunny = effects.Sunny(img)
            Shine = effects.Shine(img)
            Old = effects.Old(img)
            # SeaCollor=effects.SeaCollor(img)
            image_dic[chat_id] = {'BlackWhite': BlackWhite, 'Sunny': Sunny, 'Shine': Shine, 'Old': Old}

        if project[chat_id] == 'Greeting Card':
              logger.info(f"> end chat #{chat_id}")
              bot.send_message(chat_id=chat_id, text="ok, I will send your Greeting Card in few seconds")
              lst = data.load_image(chat_id)
              lst = mergeimage.cut_image(lst)
              im = mergeimage.create_collage(lst)
              Greeting =GreetingCard.new_Greeting(im)
              s = text_dic[chat_id].split()
              newtext=" "
              for i in range(len(s)):
                  if i % 3 ==0:
                      newtext += "\n"
                  newtext +=" "+s[i]

              img = mergeimage.print_on_image_geeting(Greeting, newtext)


              bio = BytesIO()
              bio.name = 'image.jpeg'
              img.save(bio, 'JPEG')
              bio.seek(0)
              bot.send_photo(chat_id, photo=bio)

        if project[chat_id] == 'Calender':
            logger.info(f"> end chat #{chat_id}")
            bot.send_message(chat_id=chat_id, text="ok, I will send your Greeting Card in few seconds")
            lst = data.load_image(chat_id)
            im = calendar.print_on_image(lst)
            for i in im:
                bio = BytesIO()
                bio.name = 'image.jpeg'
                i.save(bio, 'JPEG')
                bio.seek(0)
                bot.send_photo(chat_id, photo=bio)


    if query.data == 'BlackWhite':
        bot.send_message(chat_id=chat_id, text=f"ok. Ill do  the {query.data} effect to your collage ")
        bio = BytesIO()
        bio.name = 'BlackWhite.jpeg'
        image_dic[chat_id]['BlackWhite'].save(bio, 'JPEG')
        bio.seek(0)
        bot.send_photo(chat_id, photo=bio)
        bot.send_message(chat_id=chat_id, text="More efects. (/effect) ")

    if query.data == 'Sunny':
        bot.send_message(chat_id=chat_id, text=f"ok. Ill do  the {query.data} effect to your collage ")
        bio = BytesIO()
        bio.name = 'Sunny.jpeg'
        image_dic[chat_id]['Sunny'].save(bio, 'JPEG')
        bio.seek(0)
        bot.send_photo(chat_id, photo=bio)
        bot.send_message(chat_id=chat_id, text="More efects. (/effect) ")

    if query.data == 'Old':
        bot.send_message(chat_id=chat_id, text=f"ok. Ill do  the {query.data} effect to your collage ")
        bio = BytesIO()
        bio.name = 'Old.jpeg'
        image_dic[chat_id]['Old'].save(bio, 'JPEG')
        bio.seek(0)
        bot.send_photo(chat_id, photo=bio)
        bot.send_message(chat_id=chat_id, text="More efects. (/effect) ")

    if query.data == 'Shine':
        bot.send_message(chat_id=chat_id, text=f"ok. Ill do  the {query.data} effect to your collage ")
        bio = BytesIO()
        bio.name = 'Shine.jpeg'
        image_dic[chat_id]['Shine'].save(bio, 'JPEG')
        bio.seek(0)
        bot.send_photo(chat_id, photo=bio)
        bot.send_message(chat_id=chat_id, text="More efects. (/effect) ")

def share(bot, update):
    chat_id = update.message.chat_id
    logger.info(f"> Share chat #{chat_id}")
    bot.send_message(chat_id=chat_id, text="Send this link to your friends")
    bot.send_message(chat_id=chat_id, text=f" https://telegram.me/{secret_settings.BOT_NAME}?start={chat_id}")


def AddText(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    logger.info(f"> AddText chat #{chat_id}")
    bot.send_message(chat_id=chat_id, text="Please write your text:")


def respond(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    text_dic[chat_id]+=text


def photo(bot, update):
    chat_id = update.message.chat_id
    logger.info(f"> Photo chat #{chat_id}")

    chat_id = update.message.chat_id
    file_id = update.message.photo[-1].file_id
    file_path = bot.getFile(file_id)['file_path']
    logger.info(f"= Got on chat #{chat_id}: add photo!")
    if dicargs[chat_id]:
       data.save_image(file_path, dicargs[chat_id], photo_counter[dicargs[chat_id]])
       photo_counter[dicargs[chat_id]] += 1
    else:
       data.save_image(file_path, chat_id, photo_counter[chat_id])
       photo_counter[chat_id] += 1

    if dicargs[chat_id] == chat_id:
       keyboard = [[InlineKeyboardButton("Get Link", callback_data='Get Link'),
                    InlineKeyboardButton("Finish", callback_data='Finish'),
                    InlineKeyboardButton("Add Text", callback_data='Add Text')]]
       reply_markup = InlineKeyboardMarkup(keyboard)
       bot.send_message(chat_id=chat_id,
                        text=f"added succesfull",
                        reply_markup=reply_markup)
    else:
        bot.send_message(chat_id=chat_id,
                         text=f"added succesfull")

def effect(bot, update):
    keyboard = [[InlineKeyboardButton("BlackWhite", callback_data='BlackWhite'),
                 InlineKeyboardButton("Sunny", callback_data='Sunny'),
                 InlineKeyboardButton("Old", callback_data='Old'),
                 InlineKeyboardButton("Shine", callback_data='Shine')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose your effect for your collage.', reply_markup=reply_markup)

photo_handler = MessageHandler(Filters.photo, photo)
dispatcher.add_handler(photo_handler)

start_handler = CommandHandler('start', start, pass_args=True)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

logger.info("Start polling")
updater.start_polling()


updater.dispatcher.add_handler(CallbackQueryHandler(button))

share_handler = CommandHandler('share', share)
dispatcher.add_handler(share_handler)

AddText_handler = CommandHandler('AddText', AddText)
dispatcher.add_handler(AddText_handler)

respond_handler = CommandHandler('respond', respond)
dispatcher.add_handler(respond_handler)

effect_handler = CommandHandler('effect', effect)
dispatcher.add_handler(effect_handler)