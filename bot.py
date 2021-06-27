import telebot
import pyowm
import math

from pyowm.utils.config import get_config_from
config_dict = get_config_from('config.json')

owm = pyowm.OWM('503f69da8f787a39ff9511dfa7d4693c', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("1774755389:AAERE52Afna2Qz-Dkb2HeZAiwUeH_sghl5k")

@bot.message_handler(content_types=["text"])
def send_echo(message):
	observation = mgr.weather_at_place( message.text )
	w = observation.weather

	temp = w.temperature('celsius') ["temp"]
	temp = math.ceil(temp)

	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Текущая температура: " + str(temp) + " градусов по цельсию " + "\n\n"

	if temp < 10:
		answer += "Оденься потеплее, на улице холодно"
	elif temp < 20:
		answer += "Спортивки покатят"
	else:
		answer += "Жарища, сиди-ка ты лучше дома"

	bot.send_message(message.chat.id, answer)

bot.polling ( none_stop = True )