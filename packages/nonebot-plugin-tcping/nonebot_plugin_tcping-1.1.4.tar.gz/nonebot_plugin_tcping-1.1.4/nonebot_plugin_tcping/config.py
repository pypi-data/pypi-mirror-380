from nonebot import get_driver
from pydantic import BaseModel

driver = get_driver()

class Config(BaseModel):
    """Plugin Config Here"""
    tcping_url : str = "https://v2.api-m.com/api/tcping"
    recal_time: int = 90