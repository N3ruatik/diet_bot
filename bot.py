import sqlite3
>> from aiogram import Bot, Dispatcher, types
>> from aiogram.utils import executor
>> from dotenv import load_dotenv
>> import os
>> load_dotenv()
>> API_TOKEN = os.getenv('BOT_TOKEN')
>> bot = Bot(token=API_TOKEN)
>> dp = Dispatcher(bot)
>> def get_db_connection():
>> conn = sqlite3.connect('diet_bot.db')
>> conn.row_factory = sqlite3.Row
>> return conn
>> @dp.message_handler(commands=['start'])
>> async def send_welcome(message: types.Message):
>> user_id = message.from_user.id
>> username = message.from_user.username or 'Unknown'
>> conn = get_db_connection()
>> cursor = conn.cursor()
>> cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
>> conn.commit()
>> conn.close()
>> await message.reply(f'Привет, {username}! Бот для низкоуглеводной диеты. Используй /help.')
>> @dp.message_handler(commands=['help'])
>> async def send_help(message: types.Message):
>> await message.reply('Команды:\n/start - Начать\n/help - Справка\n/add_food - Добавить еду (скоро)\n/report - Отчет (скоро)')
>> if name == 'main':
>> executor.start_polling(dp, skip_updates=True)