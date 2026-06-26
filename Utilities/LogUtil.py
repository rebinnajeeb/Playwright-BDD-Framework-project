import logging
import os
import time


class Logger:
    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter(
            "%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s"
        )

        # Always create the Logs folder relative to the project root so the
        # framework never crashes on first run if the folder is missing.
        logs_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Logs"
        )
        os.makedirs(logs_dir, exist_ok=True)

        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = os.path.join(logs_dir, f"log{curr_time}.txt")

        # Guard against adding a duplicate handler every time a Logger is built
        # (otherwise each log line gets written multiple times).
        if not self.logger.handlers:
            fh = logging.FileHandler(self.LogFileName, mode="a")
            fh.setFormatter(fmt)
            fh.setLevel(file_level)
            self.logger.addHandler(fh)
