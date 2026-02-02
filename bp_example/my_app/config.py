class Config:
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    RUN_HOST = "0.0.0.0"
    RUN_PORT = 4444


class DevelopmentConfig(Config):
    DEBUG = True
    RUN_HOST = "0.0.0.0"
    RUN_PORT = 3333

