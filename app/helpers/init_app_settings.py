from dotenv import load_dotenv
import os
import logging


def init_app_settings():
    """
    Initializes the application settings by loading environment variables and configuring logging.

    :return: None
    """
    load_dotenv()

    # logging settings
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
    )
