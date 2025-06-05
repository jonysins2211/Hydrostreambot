# This file is a part of FileStreamBot
from urllib import request
from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID", "27258953"))
    API_HASH = str(environ.get("API_HASH", "0add43fc460daca0a86077989cfc414f"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "7"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL", "-1002005906539")
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(environ.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(environ.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(environ.get("FQDN", BIND_ADDRESS))
    URL = "https://movie-loverzz2-1c5653e626a6.herokuapp.com/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )

    DATABASE_URL = str(environ.get('DATABASE_URL', 'mongodb+srv://batmann:saBVJFEqhb3rk5KQ@cluster0.az5fg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(environ.get('UPDATES_CHANNEL', "MovieEntertainment4u"))
    OWNER_ID = int(environ.get('OWNER_ID', '949657126'))
    SESSION_NAME = str(environ.get('SESSION_NAME', 'Mlfiletolinkbot'))
    FORCE_UPDATES_CHANNEL = environ.get('FORCE_UPDATES_CHANNEL', True)
    FORCE_UPDATES_CHANNEL = True if str(FORCE_UPDATES_CHANNEL).lower() == "true" else False
    ALLOWED_USERS = [x.strip("@ ") for x in str(environ.get("ALLOWED_USERS") or "").split(",") if x.strip("@ ")]

    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "1").lower()) in  ("1", "true", "t", "yes", "y")
    IMAGE_FILEID = environ.get('IMAGE_FILEID', "https://graph.org/file/a319f6b9ce3b993c6e22f.jpg")
    TOS = environ.get("TOS", None)
    if TOS:
        response = request.urlopen(TOS)
        data = response.read().decode('utf-8')
        TOS = data.strip()

    MODE = environ.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    LINK_LIMIT = int(environ.get("LINK_LIMIT")) if "LINK_LIMIT" in environ else None
