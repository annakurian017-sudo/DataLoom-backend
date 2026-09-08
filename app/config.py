from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str 
    APP_VERSION: str 
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()