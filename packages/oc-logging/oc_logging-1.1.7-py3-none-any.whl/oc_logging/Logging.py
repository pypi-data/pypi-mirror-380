import os
from logging.config import dictConfig
import urllib3



def setup_logging():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    console_level = os.getenv("LOG_LEVEL")
    if not console_level:
        console_level = "DEBUG"

    if console_level not in ["DEBUG", "WARNING", "INFO", "ERROR", "CRITICAL"]:
        raise EnvironmentError("LOG_LEVEL must be DEBUG, WARNING, INFO, ERROR, or CRITICAL")

    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] [%(levelname)s] %(message)s",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "default",
                    "level": console_level,
                },
            },
            "root": {
                "level": "DEBUG",
                "handlers": ["console"],
            },
            "loggers": {
                "werkzeug": {
                    "level": console_level,
                    "propagate": False
                },
                "py.warnings": {
                    "level": "ERROR",
                    "propagate": False
                }
            }
        }
    )