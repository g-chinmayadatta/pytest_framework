# import logging
# import os
#
# def setup_logger():
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)
#
#     # Prevent duplicate handlers
#     if logger.hasHandlers():
#         logger.handlers.clear()
#
#     # Create logs folder if not exists
#     os.makedirs("logs", exist_ok=True)
#
#     # File handler
#     file_handler = logging.FileHandler("logs/test.log", 'w')
#     file_handler.setLevel(logging.INFO)
#
#     # Console handler
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.INFO)
#
#     # Formatter
#     formatter = logging.Formatter(
#         "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s",
#         "%Y-%m-%d %H:%M:%S"
#     )
#
#     file_handler.setFormatter(formatter)
#     console_handler.setFormatter(formatter)
#
#     logger.addHandler(file_handler)
#     logger.addHandler(console_handler)
#     logger.propagate = True
#     return logger
#
# logger = setup_logger()
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.propagate = True   # 🔥 MUST be True

if not logger.handlers:

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)