import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "12581928")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "9bd003806267466f904f91aa035d8991") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5825162076:AAFai4cjdfN_XMi6wz4wytY1DiQi2Cz_ZYg") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1002059261530') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://freakboy:freakboy@cluster0.qhvex0i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","EncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "1621366244")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001787919806')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
