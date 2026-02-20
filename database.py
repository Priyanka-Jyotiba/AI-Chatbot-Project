import sqlite3

def init_db():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT
    )
    """)
    
    conn.commit()
    conn.close()

def save_chat(user_message, bot_response):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO chats (user_message, bot_response) VALUES (?, ?)",
        (user_message, bot_response)
    )
    
    conn.commit()
    conn.close()
