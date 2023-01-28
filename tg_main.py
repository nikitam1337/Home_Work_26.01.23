import telebot
from telebot import types
import random
bot = telebot.TeleBot("5839553872:AAFi3Z5o1w-LMX3nJzUug3P-5-1X2xgaSwY")
num = 0
start = 0

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id,"Привет! Это Игра с конфетами.\n\
Введи команду: /button")

@bot.message_handler(commands = ["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Узнать правила игры")
    but2 = types.KeyboardButton("Играть!")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id,"Нажми на нужную кнопку",reply_markup=markup)

@bot.message_handler(content_types = "text")
def controller(message):    
    global num
    global start
    start = 221
    print(message.text)
    if message.text == "Узнать правила игры":
        bot.send_message(message.chat.id,"Условия игры следующие:\n\
1) На столе лежит 221 конфета. Вы играете против Меня. Ходим поочередно.\n\
2) Первый ход определяется жеребьёвкой.\n\
3) За один ход можно забрать не более чем 28 конфет, но не меньше 1.\n\
4) Все конфеты оппонента достаются сделавшему последний ход.")
        button(message)
    elif message.text == "Играть!":
        bot.send_message(message.chat.id,'Давай начнём!')
        bot.send_message(message.chat.id,"Происходит жеребьёвка...")
        player_number = random.randint(1, 2)
        if player_number == 1:
            bot.send_message(message.chat.id,"Первым хожу я.")
        else:
            bot.send_message(message.chat.id,"Первым ходите Вы!")
        count = 0
        while start > 28:
            count += 1
            bot.send_message(message.chat.id,f'{count} ход: На столе сейчас лежит {start} конфет(а).')
            if player_number == 1:
                candies = random.randint(1, 28)
                start -= candies
                bot.send_message(message.chat.id,f'Я возьму {candies} конфет(ы).')
                player_number=2
            else:
                bot.send_message(message.chat.id,f'Сколько конфет Вы возьмете со стола: ')   
                bot.register_next_step_handler(message,user_num_step1)
                user_input = num
                start -= user_input
                player_number=1
        while start > 0:
            count += 1
            bot.send_message(message.chat.id,f'{count} ход: На столе сейчас лежит {start} конфет(а).')
            if player_number == 1:
                candies = random.randint(1, start)
                start -= candies
                bot.send_message(message.chat.id,f'Я возьму {candies} конфет(ы).')
                player_number=2
            else:
                bot.send_message(message.chat.id,f'Сколько конфет Вы возьмете со стола: ')   
                bot.register_next_step_handler(message,user_num_step2)
                user_input = num
                start -= user_input
                player_number=1
        if player_number == 1:
            bot.send_message(message.chat.id,f'Поздравляю! Вы победили!')   
        else:
            bot.send_message(message.chat.id,f'Увы, в этот раз не повезло. Я победил :). Попробуйте сыграть снова!')   

def user_num_step1(message):
    global num
    num = int(message.text)
    # user_input = message.text
    # while not user_input.isdigit():
    #     bot.send_message(message.chat.id,f'{user_input} - не число! Попробуйте снова.')   
    #     bot.send_message(message.chat.id,f'Сколько конфет Вы возьмете со стола: ')   
    #     bot.register_next_step_handler(message,user_num_step1)
    #     user_input = num
    # while int(user_input) < 1 or int(user_input) > 28:
    #     bot.send_message(message.chat.id,f'Вы должны взять хотя бы 1 конфету, но не больше 28. Попробуйте снова.')   
    #     bot.send_message(message.chat.id,f'Сколько конфет Вы возьмете со стола: ')   
    #     bot.register_next_step_handler(message,user_num_step1)
    #     user_input = num
    #     while not user_input.isdigit():
    #         bot.send_message(message.chat.id,f'{user_input} - не число! Попробуйте снова.')   
    #         bot.send_message(message.chat.id,f'Сколько конфет Вы возьмете со стола: ')   
    #         bot.register_next_step_handler(message,user_num_step1)
    #         user_input = num
    # user_input = int(user_input)
    # num = user_input

def user_num_step2(message):
    global num
    num = int(message.text)
    # global start
    # user_input = message.text
    # while not user_input.isdigit():
    #     bot.send_message(message.chat.id,f'{user_input} - не число! Попробуйте снова.')   
    #     bot.send_message(message.chat.id,f'Сколько конфет Вы возьмете со стола: ')   
    #     bot.register_next_step_handler(message,user_num_step2)
    #     user_input = num
    # while int(user_input) < 1 or int(user_input) > start:
    #     bot.send_message(message.chat.id,f'Вы должны взять хотя бы 1 конфету, но не больше {start}. Попробуйте снова.')   
    #     bot.send_message(message.chat.id,f'Сколько конфет Вы возьмете со стола: ')   
    #     bot.register_next_step_handler(message,user_num_step2)
    #     user_input = num
    #     while not user_input.isdigit():
    #         bot.send_message(message.chat.id,f'{user_input} - не число! Попробуйте снова.')   
    #         bot.send_message(message.chat.id,f'Сколько конфет Вы возьмете со стола: ')   
    #         bot.register_next_step_handler(message,user_num_step2)
    #         user_input = num
    # user_input = int(user_input)
    # num = user_input


bot.infinity_polling()