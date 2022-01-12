import os
import telebot

from telebot.types import BotCommand
from backend.storage.database import session
from backend.logic.mahjong_logic import MahjongGame
from backend.logic.blackjack_logic import BlackjackGame
from backend.info.help_info import blackjack_info, mahjong_info, generic_info
from keys import API_KEY

# HackNRollFruitStoreBot
# API_KEY = os.getenv('API_KEY') 
bot = telebot.TeleBot(API_KEY)


# bot.set_my_commands([])
bot.set_my_commands([
  BotCommand('start', 'Starts the bot'),
  BotCommand('startmahjong', 'Starts a Mahjong tracking session'),
  BotCommand('endmahjong', 'Ends the current Mahjong session'),
  #Link to Mahjong scoring/ rules
  BotCommand('startblackjack', 'Starts a BlackJack card counter'),
  BotCommand('endblackjack', 'Ends the current Blackjack session'),
  BotCommand('help', 'Lists instructions for the bot'),
  BotCommand('helpblackjack', 'Information on commands related to blackjack'),
  BotCommand('helpmahjong', 'Information on commands related to blackjack')
])
 
def request_start(chat_id):
  if chat_id not in session:
    bot.send_message(chat_id=chat_id, text='Please start the bot by using the command `/start`')

 
@bot.message_handler(commands=['parrot'])
def parrot(message):
  """
  command that replies the user with the text message it receives
  """
  message_text = message.text
  print("received message: ", message_text)
  bot.reply_to(message, "parrot" + message_text)

 
@bot.message_handler(commands=['start'])
def start(message):
  """
  Command that welcomes the user and configures the initial setup.

  Can initialise database here in this init method

  port settings, history etc
  """
  chat_id = message.chat.id
  if chat_id not in session:   
    session[chat_id] = {}
    session[chat_id]["mahjong"] = None
    session[chat_id]["blackjack"] = None

  if message.chat.type == "private":
    #chat_user = message.chat.first_name
    bot.reply_to(message, "Hi! I am Jack Ma(h)")
  """  
  else:
    chat_user = message.id
    bot.reply_to(message, message_text)
  """
  # TODO: BOT TO SHOW ALL USER ALL COMMANDS AND A BRIEF DESCRIPTION

@bot.message_handler(commands=['startmahjong'])
def startmahjong(message):
  chat_id = message.chat.id
  if chat_id not in session:
    bot.reply_to(message, "Kindly do the first time initial setup by using /start first")
    return
  if session[chat_id]["mahjong"] != None:
    bot.reply_to(message, "Please end your current mahjong session using the command `/endmahjong`")
  else:
    session[chat_id]["mahjong"] = MahjongGame()
    bot.reply_to(message, "Kindly enter your wind direction in the following format: Mahjong <Wind>\n where <Wind is either N, S, E, W>")


@bot.message_handler(commands=['endmahjong'])
def endmahjong(message):
  chat_id = message.chat.id
  session[chat_id]["mahjong"] = None
  bot.reply_to(message, "Your previous mahjong game has been cleared!")


@bot.message_handler(commands=['endblackjack'])
def endblackjack(message):
  chat_id = message.chat.id
  session[chat_id]["blackjack"] = None
  bot.reply_to(message, "Your previous blackjack game has been cleared!")


@bot.message_handler(commands=['startblackjack'])
def startblackjack(message):
  chat_id = message.chat.id
  if chat_id not in session:
    bot.reply_to(message, "Kindly do the first time initial setup by using /start first")
    return
  if session[chat_id]["blackjack"] != None:
    bot.reply_to(message, "Please end your current blackjack session using the command `/endblackjack`")
  else:
    session[chat_id]["blackjack"] = BlackjackGame()
    bot.reply_to(message, "Blackjack session started!")

@bot.message_handler(commands=['helpblackjack'])
def helpblackjack(message):
  bot.reply_to(message, blackjack_info)
  pass


@bot.message_handler(commands=['helpmahjong'])
def helpmahjong(message):
  bot.reply_to(message, mahjong_info)
  pass


@bot.message_handler(commands=['help'])
def generic_help(message):
  bot.reply_to(message, generic_info)
  pass


def blackjackGameLogic(message, msg_lst):
  chat_id = message.chat.id
  commands = set(["discard", "stats"])
  command = msg_lst[0]

  if command not in commands:
    bot.reply_to(message, "Please enter a valid command. If you need help, please type `/helpblackjack for more information`")
  
  if command == "discard":
    cards = msg_lst[1:]
    reply_message = session[chat_id]["blackjack"].discard(cards)
    bot.reply_to(message, reply_message)
  elif command == "stats":
    print(f"msg_lst is: {msg_lst}")
    house_card = [msg_lst[1], ]
    your_cards = msg_lst[2: ]
    reply_message = session[chat_id]["blackjack"].get_stats(house_card, your_cards)
    bot.reply_to(message, reply_message)

  print(msg_lst)
  pass


'''
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
  print('hit')
  """
  Handles the execution of the respective functions upon receipt of the callback query
  """
  bot.reply_to(call.message, "Hi, callback handler here")

  chat_id = call.message.chat.id
  data = call.data
  # 'player-action-tile'
  # callback data 'view detail Apple'
  # intent = 'view'
  # data = 'detail Apple'
  intent, data = data.split()[0], data.split()[1:]
  
  if intent == 'view':
    print('lol')

  pass



@bot.message_handler(commands=['items'])
def items(message):
    """
 Cmmand that lists all available items for sale
  """
    chat_id = message.chat.id
 
  if chat_id not in session:
      request_start(chat_ 
    return

    chat_text = "Select the item you would like to view ind detail"

    buttons = []

    for fruit_name in fruits:
      row = []
    button = InlineKeyboardButton(fruit_name,
                                  
      callback_data='view details of ' +
      fruit_name)e
    )
    buttons.append(row)

  
                   
    text=ch a t_text,
    repl y _markup=InlineKeyboardMarkup(buttons))
)
'''


'''
def view_item_details(chat_id, data):
    """
  splays the item details and an inline keyboard to add the item
  """

    subintent, fruit_name = data
  description = fruits[fruit_name]['description']
  price = fruits[fruit_name]['price']
  img_url = fruits[fruit_name]['img']

    caption = (f'Item: {fruit_name}\n'
             f'Description: {description}\n'
  f'Price: {price:.2f}\n\n'
  f'How many would you like to add?')

    buttons = []
  count = 0
  for _ in range(3):
      row = []

        for _ in range(3):
        count += 1
      quantity = str(count)
      button = InlineKeyboardButton(
          text=quantity, callback_data=f'add {quantity} {fruit_name}')

         
      )

      buttons.append(row)
    pass
'''


 
'''
@bot.message_handler(commands=['clear'])
def clear_cart(message):
  """
  Command that removes all items in the cart
  """

     chat_id = message.chat.id
  if chat_id not in cart:
      request_start(chat_ id)
      return
    
  pass
'''
 
@bot.message_handler(content_types=['text'])
def text_handler(message):
  '''
  Format: Game Input1 Input2 Input3
  '''

  chat_id = message.chat.id
  user_input_arr = message.text.split(' ')
  
  if user_input_arr[0].lower() == 'mahjong' and session[chat_id]["mahjong"] != None:
    msg = session[chat_id]["mahjong"].inputHandler(user_input_arr[1:])
    #msg = session[chat_id]["mahjong"].printAllInformation2()
    bot.reply_to(message, msg)
  
  elif user_input_arr[0].lower() == 'blackjack' and session[chat_id]["blackjack"] != None:
    blackjackGameLogic(message, user_input_arr[1:])
  else:
    bot.reply_to(message, "Please input a valid command. For more information, checkout `/help`!")

 
bot.infinity_polling()
