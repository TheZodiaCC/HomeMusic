import os


class Config:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    FILES_LOCATION = f"{CURRENT_DIR}/files/"
    LOG_FILES_LOCATION = f"{CURRENT_DIR}/logs/"
    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = False
