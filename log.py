import logging
import time

# function for logging
def log_text(message):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    logging.info(f'{current_time} - {message}')
