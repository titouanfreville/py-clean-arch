from os import path
from environs import Env
from app.depencies import Dependencies
from app import http


env = Env()
basedir = path.dirname(__file__)

# Read variables from .env && constant configs
env.read_env()

# Load environment and config from ENV_TYPE variable name
app_env = env.str("ENV_TYPE", "local")

# Prepare dependencies
inject = Dependencies()
inject.config.from_ini(path.join(basedir, app_env + ".ini"), required=True)


api = http.api
