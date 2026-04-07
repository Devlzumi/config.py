import os

class Config(object):
    API_ID = int("31864613")
    API_HASH = "48d0a5b52baef49f1b4c7ab72decb8fa"
    BOT_TOKEN = "8648826778:AAE6vXUcnt4XXQYhh50oaUXS8l8WCty0aiQ"
    
    # Database Settings
    DB_URL = "mongodb+srv://Ly_farhan45:@Farhankhan@00@cluster0.kbdkckc.mongodb.net"
    DB_NAME = "FileStoreBot"
    DB_CHANNEL = int("-1003842171248")
    
    # Admins & Graphics
    ADMINS = [8438792943]
    START_PIC = "https://t.me/c/3432603145/89"
    HELP_PIC = "https://t.me/c/3432603145/88"
    
    # Messages
    START_MSG = "**Hi {user},\n\nMain ek Advance File Store Bot hoon. Aap mujhe koi bhi file bhejein, main uska permanent storage link bana dunga.**"
    HELP_MSG = "**Kaise use karein?**\n\n1. Mujhe koi file forward karein.\n2. Main use database mein save karke link dunga.\n3. Link par click karke koi bhi file download kar sakta hai."
