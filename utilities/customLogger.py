import logging
class LoggeGen:

    @staticmethod
    def loggegen():
        logging.basicConfig(filename=".\\Logs\\examples.log",
                            format='%(asctime)s: %(levelname)s : %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S  %p'

                            )

        # returns a object
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
