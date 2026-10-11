from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    jwt_secret: str = "your-secret-key-change-this-in-production-min-32-characters-long"
    jwt_algorithm: str = "HS256"
    jwt_expiration: int = 1
    mongodb_connection_string: str = "mongodb://localhost:27017"
    mongodb_database_name: str = "wedding_list"
    gemini_api_key: str = ""
    openai_api_key: str = ""
    ms_whatsapp_url: str = ""


    rabbitmq_host: str = "localhost"
    rabbitmq_port: str = "5672"
    rabbitmq_user: str = "myuser"
    rabbitmq_password: str = "mypassword"
    google_client_id: str = ""

    # Base URL of the React frontend, used server-side (e.g. for screenshots).
    # Local dev: http://localhost:3000
    # Docker/prod: the frontend service name on the shared network,
    # e.g. http://frontend:3000
    frontend_base_url: str = "http://localhost:3000"

    # Invitation screenshot rendering (Playwright).
    #   concurrency  - number of pooled pages / parallel renders
    #   cache_ttl    - seconds a rendered PNG is reused for the same event
    #   settle_ms    - final paint delay before capturing
    #   host_resolver_rules - optional Chromium rule to resolve the public
    #     hostname to an internal service, e.g. "MAP app.jing.co.il nginx",
    #     which avoids leaving the Docker network to reach our own frontend.
    screenshot_concurrency: int = 4
    screenshot_cache_ttl: int = 300
    screenshot_settle_ms: int = 250
    screenshot_host_resolver_rules: str = ""

    whatsapp_access_token: str = ""
    whatsapp_waba_id: str = ""
    whatsapp_phone_number_id: str = ""
    sms_token: str 
    sms_username: str
    sms_sender: str


    api_secret_key: str = ""
    app_url: str = ""
    base_url: str = ""
    ms_messages_xmlrpc_url: str = "http://localhost:8009"
    ms_notifications_url: str = "http://localhost:8001"
    # Server-side self-requests (screenshot fetch, file validation). In Docker
    # this is the same container, so localhost is correct.
    internal_backend_url: str = "http://127.0.0.1:8000"
    
    class Config:
        # "src/.env" works when running from the backend/ dir (local dev).
        # ".env"     works when running from backend/src/ (Docker WORKDIR=/app/src).
        # Pydantic-settings silently ignores missing files.
        env_file = ("src/.env", ".env")


@lru_cache()
def get_settings():
    settings = Settings()
    return settings
