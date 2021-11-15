import logging
import logging.handlers

def init_logging_config():
    fmt = '%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s'
    loggger = logging.getLogger()
    loggger.setLevel(logging.DEBUG)
    formater = logging.Formatter(fmt)

    hanlder1 = logging.StreamHandler()
    hanlder1.setFormatter(formater)
    loggger.addHandler(hanlder1)

    file_path = "./log/mhyj.log"
    hanlder2 = logging.handlers.TimedRotatingFileHandler(file_path, when="MIDNIGHT", interval=1, backupCount=3)
    hanlder2.setFormatter(formater)
    loggger.addHandler(hanlder2)

