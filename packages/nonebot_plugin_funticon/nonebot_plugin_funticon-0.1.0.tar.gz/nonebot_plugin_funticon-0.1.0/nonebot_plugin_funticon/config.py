from pydantic import BaseModel


class Config(BaseModel):
    """Plugin Config Here"""
    onebotv11http: str = "http://127.0.0.1:8083"
    openlist_username: str = "admin"
    openlist_password: str = "123456"
    openlist_base_url: str = "http://127.0.0.1:5244"