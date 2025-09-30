from nonebot import get_driver
from pydantic import BaseModel

driver = get_driver()

class Config(BaseModel):
    """Plugin Config Here"""
    tcping_url : str = driver.config.tcping_url
    recal_time: int = driver.config.recal_time