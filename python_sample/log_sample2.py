# -*- coding: utf-8 -*-
# log_controller.py
import os
import logging

class LogController():

    def __init__(self):
        self.LEVELS = { 'debug':logging.DEBUG,
            'info':logging.INFO,
            'warning':logging.WARNING,
            'error':logging.ERROR,
            'critical':logging.CRITICAL,
            }

        logging.basicConfig(level=logging.INFO, 
            filename="access.log",
            format="%(asctime)s %(levelname)-7s %(message)s")
        self.access_logger = logging.getLogger("access_logger")
        self.access_logger.setLevel(logging.INFO)
        self.access_handler = logging.StreamHandler()
        self.access_handler.setFormatter(logging.Formatter(
            "access, %(asctime)s %(levelname)8s %(message)s"))
        self.access_logger.addHandler(self.access_handler)
        #init
        self.access_logger.info(os.uname()[1])

    def load_logging(self, text):
        logging.basicConfig(level=self.LEVELS.get(text, logging.NOTSET), 
            filename="access.log",
            format="%(asctime)s %(levelname)-7s %(message)s")
        self.access_logger = logging.getLogger("access_logger")
        self.access_logger.setLevel(logging.INFO)
        self.access_handler = logging.StreamHandler()
        self.access_handler.setFormatter(logging.Formatter(
            "access, %(asctime)s %(levelname)8s %(message)s"))
        self.access_logger.addHandler(self.access_handler)
        return self.access_logger

    def info_meg(self, text):
        self.access_logger = self.load_logging("info")
        self.access_logger.info(text)

    def error_meg(self, text):
        self.access_logger = self.load_logging("error")
        self.access_logger.info(text)


if __name__ == '__main__':
    log = LogController()
    log.info_meg("access test")
    log.error_meg("error test")


