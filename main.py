



import telebot
from telebot import types


bot = telebot.TeleBot("2112306268:AAHUSJz8bHkM9a7zvgTRcBzYjb0PiCHIH8w")
print("start")

# # button
# boardbtn = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True) #Создаем поле для кнопок
# # Создаём кнопки
# btn1 = types.KeyboardButton("да") 
# btn2 = types.KeyboardButton("нет")
# # Добавляем кнопки в поле
# boardbtn.add(btn1, btn2)


#inline button
inline_btn = types.InlineKeyboardMarkup()#Создаем поле для кнопок
# Создаём кнопки
yes = types.InlineKeyboardButton(text="да", callback_data="yes")
no = types.InlineKeyboardButton(text="нет", callback_data="no")
# Добавляем кнопки в поле
inline_btn.add(yes, no)

@bot.message_handler(commands=["start"])
def start_func(message):
    bot.send_message(message.chat.id, "как тебя зовут?")

@bot.message_handler(content_types=["text"])
def hello(message):
    bot.send_message(message.chat.id, f"Привет, {message.text}")
    msg = bot.send_message(message.chat.id, f"ты сейчас читаешь какой нибудь фф?", reply_markup=inline_btn) # reply_markup - добавляет созданную нами клавиатура у с кнопками
    bot.register_next_step_handler(msg, next) # Переносит нас в следующую функцию

# @bot.message_handler(content_types=["text"])
# def computer(message):
#     if message.text.lower() == "да": # Проверка на ответ пользователя
#         msg = bot.send_message(message.chat.id, f"Долго не сиди", reply_markup=inline_btn) #reply_markup=None)
#         bot.register_next_step_handler(msg, next)
#     elif message.text.lower() == "нет":
#         msg = bot.send_message(message.chat.id, f"в телефоне?", reply_markup=inline_btn) # Прикрепление inline клавиатуры к нашему сообщению
#         bot.register_next_step_handler(msg, next)
#     else:
#         bot.send_message(message.chat.id, f"я тебя не понимаю, введи 'да' или 'нет'")


# функция ответа на inline кнопку (callback)
@bot.callback_query_handler(func=lambda call: True)
def next(call):
    if call.data == "yes":
        bot.edit_message_text(text="какой?", chat_id=call.message.chat.id, message_id=call.message.id) # редактируем сообщение
    elif call.data == "no":
        bot.edit_message_text(text="подсказать?", chat_id=call.message.chat.id, message_id=call.message.id)
        def computer(message):
            if message.text.lower() == "да": # Проверка на ответ пользователя
                msg = bot.send_message(message.chat.id, f"Незаменимая", reply_markup=inline_btn) #reply_markup=None)
                bot.register_next_step_handler(msg, next1)
            elif message.text.lower() == "нет":
                msg = bot.send_message(message.chat.id, f"ок", reply_markup=inline_btn) # Прикрепление inline клавиатуры к нашему сообщению
                bot.register_next_step_handler(msg, next)
            else:
                bot.send_message(message.chat.id, f"я тебя не понимаю, введи 'да' или 'нет'")

if __name__ == '__main__':
    bot.polling(none_stop=True)