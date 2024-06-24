import logging
import sys

class Logger:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)5s - %(message)s',
    encoding="utf-8",
    handlers=[logging.FileHandler("d:/logging.log"), logging.StreamHandler(sys.stdout)
              ])

    @staticmethod
    def info(text):
        logging.info(text)

    @staticmethod
    def error(text):
        logging.error(text)

    @staticmethod
    def debug(text):
        logging.debug(text)


