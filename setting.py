from pydantic_settings import BaseSettings ,SettingsConfigDict

class Setting(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env")


    API_KEY:str
    DB_USERNAME:str
    DB_PASSWORD:str

setting=Setting()
print(setting.API_KEY)
print(setting.DB_USERNAME,setting.DB_PASSWORD)









