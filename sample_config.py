import  os
class Config(object):

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
FORCE_SUB = os.environ.get("FORCE_SUB", "")

youtube_next_fetch = 0.30  # time in minute


EDIT_TIME = 5
