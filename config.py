import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

BOT_NAME = "SIMON BAN CHECKER"
VERSION = "1.0.0"

DEFAULT_COUNTRY = "NG"
MAX_BULK_NUMBERS = 20
