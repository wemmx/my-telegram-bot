import telebot
import random

# ВСТАВЬ СЮДА СВОЙ НАСТОЯЩИЙ ТОКЕН!
TOKEN = "8231460140:AAHQCV0G2oxG5NJDQrTl30PHpR9x6-j-J2U"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
    🐉 Лаборатория Хротгара активна
    Используй /quote для мудрости
    """
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['quote'])
def send_quote(message):
    quotes = [
        "Л: Банальность зла — в его повседневности.",
        "Партурнакс: Что есть голос, если не шепот ветра к времени?",
        "Твой инсайт: Я — ружье, которое зарядил Чехов."
    ]
    chosen_quote = random.choice(quotes)
    bot.reply_to(message, chosen_quote)

@bot.message_handler(commands=['iqjoke'])
def iq_joke(message): 
    iqjoke_rules = [
    "Читай 1500 книг в час, пей 20 проливов пуэра"
    "Медитируй на глотке мира"
    "Находи киру каждый день"
    chosen_rule = random.choice(iqjoke_rules)		
    bot.reply_to(message, "chosen_rule")

print("Бот запущен...")
bot.polling()