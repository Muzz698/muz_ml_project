import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(os.path.dirname(logs_path), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO
)