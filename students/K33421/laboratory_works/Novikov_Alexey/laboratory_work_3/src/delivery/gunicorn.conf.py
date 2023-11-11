import multiprocessing

from dotenv import load_dotenv
from starlette.config import Config

load_dotenv()

env = Config(".env")

loglevel = env("LOG_LEVEL")
bind = f"{env('HOST')}:{env('PORT')}"
timeout = 0
workers = multiprocessing.cpu_count() * 2
