import logging

logger = logging.getLogger("biotime")
logger.setLevel(logging.INFO)

# Konsolga chiqishi uchun handler
console = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
console.setFormatter(formatter)
logger.addHandler(console)
