from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    project_name :str 
    database_url :str 
    model_config = SettingsConfigDict(env_file=".env",env_file_encoding="utf-8",extra="ignore")

settings = Settings() #type:ignore 

