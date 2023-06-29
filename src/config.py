import os
from dotenv import load_dotenv

# bot token
load_dotenv()
TOKEN = os.getenv("TOKEN")

# embed colors
SUCCESS = 0x44C1FF
WARNING = 0xffc744
ERROR = 0xff4444

# logging
LOGS_CHANNEL = 1123803520890581022
