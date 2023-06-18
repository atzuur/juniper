import os
from dotenv import load_dotenv


# bot token
load_dotenv()
TOKEN = os.getenv("TOKEN")

# embed colors!
SUCCESS = 0x4bf288
WARNING = 0xf2d64b
ERROR = 0xf24b4b
