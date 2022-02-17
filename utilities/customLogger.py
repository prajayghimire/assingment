import logging


class Logger:

    @staticmethod
    def logi():

        logging.basicConfig(filename=".\\logs\\logs.log",
                            format='%(asctime)s: %(levelname)s : %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p'

                            )

        # returns a object
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
