from pyhwlib import load_config,hello
import os
from loguru import logger

@load_config()
def get_config(MYSQL_HOST: str,
            MYSQL_PORT: int,
            MYSQL_USER: str = None,
            MYSQL_PASSWORD: str = None,
            MYSQL_DATABASE: str = None,
            EXTRA_INFO=111):
    logger.info(f"MYSQL_HOST: {MYSQL_HOST}, MYSQL_PORT: {MYSQL_PORT}, MYSQL_USER: {MYSQL_USER}, MYSQL_PASSWORD: {MYSQL_PASSWORD}, MYSQL_DATABASE: {MYSQL_DATABASE}, EXTRA_INFO: {EXTRA_INFO}")
    
    
def main():
    print("Hello, World!")
    
    
    
if __name__ == "__main__":
    get_config()
    print(hello())