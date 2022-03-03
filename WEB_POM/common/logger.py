import logging
import os
import datetime

# create logger
def getlog():
    a = os.path.basename(__file__).split(".")[0]
    b = datetime.datetime.now()

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)




    fh = logging.FileHandler("./logs/{}.log".format(a), encoding="utf-8")
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(funcName)s- %(message)s')
    # if not logger.handlers:

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger



    # logger.removeHandler(fh)
    # logger.removeHandler(ch)




    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warn message')
    # logger.error('error message')
    # logger.critical('critical message')
#
# if __name__ == '__main__':
#     getlog()
#     getlog()
#     getlog()
