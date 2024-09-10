# this file manages parameterization i.e. replacing hardcoded values:

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath

from loguru import logger
import sqlalchemy
import os


print(os.listdir())


class Settings(BaseSettings):  # pydntic is not able to find models folder
    model_config = SettingsConfigDict(
        env_file='src/config/.env',
        env_file_encoding='utf-8'
        )

    data_file_name: FilePath
    model_path: DirectoryPath
    model_name: str
    log_level: str
    db_conn_str: str
    rent_apart_table_name: str


# lets make the object of class which will be used eveywhere else
settings = Settings()

# now lets add  log file to each place
logger.remove()  # to remove logs from our console
logger.add("src/logs/app.log", rotation="1 day", retention="2 days", level=settings.log_level)  # noqa: E501


engine = sqlalchemy.create_engine(settings.db_conn_str)
