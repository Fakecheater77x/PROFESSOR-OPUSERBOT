from os import getenv, path
from dotenv import load_dotenv
from data import THE_PROFESSOR


if path.exists(".env"):
    load_dotenv(".env")
    
#----------------------------------- REQUIRED --------------------------------------#


API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
SESSION1 = getenv("SESSION1", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = list(map(int, getenv("OWNER_ID", "7463345743").split()))


#-------------------------------- OPTIONAL -------------------------------------#

SESSION2 = getenv("SESSION2")
SESSION3 = getenv("SESSION3")
SESSION4 = getenv("SESSION4")
SESSION5 = getenv("SESSION5")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Fakecheater77x/PROFESSOR-OPUSERBOT")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", None)

EXTRA_IMG = getenv("EXTRA_IMG", "https://telegra.ph/file/a37d283f3f1e9712dc7de.jpg")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7463345743").split()))

for y in OWNER_ID:
    SUDO_USERS.append(y)

for x in THE_SHUKLA:
    SUDO_USERS.append(x)

LOAD = []

NO_LOAD = []

HELPABLE = {}
