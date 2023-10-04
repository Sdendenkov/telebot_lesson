# Для подключения библиотеки к проекту ее нужно прописать в блоке импортов:
import telebot
# BotFather – это официальный Telegram бот для создания и настройки других ботов.
MY_TOKEN = '5902676518:AAEGsMDlE9nEoRemyC3N5gg692x5uWMGaBc'

# Задание 3.2. Подключение библиотеки telebot.
# Существует несколько библиотек для создания Telegram ботов. Самая простая из них, с которой вы познакомитесь в первую
# очередь – библиотека telebot.
# Официальную документацию этой библиотеки можно найти на сайте https://pypi.org/project/pyTelegramBotAPI/

# Задание 3.3. Создание бота.
# Далее вам необходимо создать объект класса TeleBot, и в качестве входного значения передать ему тот самый токен:
bot = telebot.TeleBot(MY_TOKEN)

# Задание 3.4. Настройка реакции бота на команду.
# Как правило, первой командой для Telegram ботов является команда start. Именно ее обработку вы напишете первой.
# С помощью метода message_handler() определите команду start, а затем напишите функцию обработки этой команды:


@bot.message_handler(commands=['start'])  # добавление команды старт.
# Функция обработки команды "старт"
def start(message):
    user_name = message.from_user.first_name
    me = bot.get_me().first_name
    bot.send_message(message.chat.id, f'{me}: Привет, {user_name}! я твой первый бот!')


# Задание 3.5. Запуск и тестирование бота.
bot.polling(none_stop=True)

# Когда мы общаемся с ботами, они по умолчанию собирают о нас общедоступную информацию, наш идентификатор, имя,
# и так далее. Поэтому боту необязательно спрашивать, как зовут пользователя, он может сразу обратиться к нему по имени.






