import logging
from telebot import TeleBot

from secrets import API_TOKEN, WEATHER_API_KEY

from weather import WeatherApp

bot = TeleBot(token=API_TOKEN)

logging.basicConfig(level=logging.INFO)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    """Отправляет приветственное сообщение"""
    #print(dir(bot))
    bot.reply_to(message, f"Привет, {message.from_user.username}. \n\nВведите название города и я подскажу тебе подгоду")
    
@bot.message_handler()
def send_weather(message):
    weather = WeatherApp(WEATHER_API_KEY)
    #city_weather= weather.get_weather(city=message.text)
    city_weather= weather.get_weather(city=message.text)
    bot.reply_to(message, city_weather)

if __name__ == "__main__":

    bot.polling()
    print("Im running")