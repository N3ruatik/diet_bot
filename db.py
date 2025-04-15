import sqlite3
def init_db():
conn = sqlite3.connect('diet_bot.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY,
height INTEGER,
weight FLOAT,
age INTEGER,
gender TEXT,
calorie_goal FLOAT,
carb_goal FLOAT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
product_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE,
calories FLOAT,
protein FLOAT,
fat FLOAT,
carbs FLOAT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS food_log (
log_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
product_id INTEGER,
amount FLOAT,
log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users(user_id),
FOREIGN KEY (product_id) REFERENCES products(product_id)
)
''')
conn.commit()
conn.close()
print('База данных создана.')
if name == 'main':
init_db()