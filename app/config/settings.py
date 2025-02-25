from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / ".env"

load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    bnc_api_key: str
    bnc_api_secret: str
    buy_value: float
    sell_value: float
    btc_asset: str

    class Config:
        env_file = str(env_path)
        env_file_encoding = ("utf-8")


settings = Settings()
