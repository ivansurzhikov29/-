import telebot
from telebot import types 

token = '5770372832:AAFWxF7Nc2-uIbVdkZ9jnNiLhL_Qpi9DUWk'
bot = telebot.TeleBot(token)
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row("нормально", "можно спросить кое что?)","Как тебя зовут?","Что я могу?","Вернуться в главное меню")
@bot.message_handler(commands=['start'])
def start1(message):
    bot.send_message(message.chat.id, "Привет я бот Ви",reply_markup=keyboard1)
    bot.send_message(message.chat.id, 'Пока что я ничего не умею но обязательно научусь ')
    bot.send_message(message.chat.id, 'как твои дела? ')
@bot.message_handler(content_types=['text'])
def start3(message):
    if(message.text == "нормально"):
        bot.send_message(message.chat.id, text="крутяк, надеюсь дальше будет лучше)))")
    elif(message.text == "можно спросить кое что?)"): 
      bot.send_message(message.chat.id, 'да, о чём?')    
 
    elif(message.text == "Как тебя зовут?"):
        bot.send_message(message.chat.id, "Я Ви, кавбой)")
    
    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id,  "Пока моло чего")
    
    elif (message.text == "Вернуться в главное меню"):
        bot.send_message(message.chat.id,  "*Вы  типа  вернулись в главное меню" )
        
        
    else:bot.send_message(message.chat.id, text="не понял тебя")    

if __name__ == '__main__':
          bot.polling(none_stop=True)
