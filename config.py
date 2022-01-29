import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "pikachu01001")
ALIVE_NAME = getenv("ALIVE_NAME", "YOUR DAD")
BOT_USERNAME = getenv("BOT_USERNAME", "MAMBAX_GBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MAMBA_MUSIC")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "PIKKUMUSIC_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "PIKKUMUSIC_SUPPORT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Pikachu01001/PIKKU")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/8ab6f1047e168e034bc14.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/8ab6f1047e168e034bc14.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/8ab6f1047e168e034bc14.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/8ab6f1047e168e034bc14.jpg")
