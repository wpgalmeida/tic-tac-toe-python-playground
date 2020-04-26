from logging import Formatter

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "std-formatter": {"()": Formatter, "format": "%(asctime)s - level=%(levelname)s - %(name)s - %(message)s"},
    },
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "std-formatter"}},
    "loggers": {"": {"level": "INFO", "handlers": ["console"]},},
}
