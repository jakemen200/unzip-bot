import os

class Config:
    APP_ID = int(os.environ.get("APP_ID", "0") or "0")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "0") or "0")
    MONGODB_DBNAME = os.environ.get("MONGODB_DBNAME", "Unzipper_Bot")
    MONGODB_URL = os.environ.get("MONGODB_URL", "")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "0") or "0")

print(f"Loaded APP_ID: {Config.APP_ID}")
print(f"Loaded BOT_OWNER: {Config.BOT_OWNER}")
print(f"Loaded LOGS_CHANNEL: {Config.LOGS_CHANNEL}")
    )
    MAX_CONCURRENT_TASKS = 75
    MAX_MESSAGE_LENGTH = 4096
    MAX_CPU_CORES_COUNT = psutil.cpu_count(logical=False)
    MAX_CPU_USAGE = 80
    # 512 MB by default for Heroku, unlimited otherwise
    MAX_RAM_AMOUNT_KB = 1024 * 512 if IS_HEROKU else -1
    MAX_RAM_USAGE = 80
    MAX_TASK_DURATION_EXTRACT = 120 * 60  # 2 hours (in seconds)
    MAX_TASK_DURATION_MERGE = 240 * 60  # 4 hours (in seconds)
    # Files under that size will not display a progress bar while uploading
    MIN_SIZE_PROGRESS = 1024 * 1024 * 50  # 50 MB
    MONGODB_URL = os.environ.get("MONGODB_URL")
    MONGODB_DBNAME = os.environ.get("MONGODB_DBNAME", default="Unzipper_Bot")
    TG_MAX_SIZE = 2097152000
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    VERSION = os.environ.get("UNZIPBOT_VERSION", default="7.3.0")
