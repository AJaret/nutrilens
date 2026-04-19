from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "NutriLens API"
    api_v1_prefix: str = "/api/v1"

    postgres_db: str = "nutrilens"
    postgres_user: str = "nutrilens"
    postgres_password: str = "nutrilens"
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    secret_key: str = "change-me-in-dev"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    algorithm: str = "HS256"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
