import logging

logging.basicConfig(
    level=logging.DEBUG,  # По умолчанию уровень WARNING
    # name="Имя лога",  # По умолчанию root
    filename='example.log',
    format='%(filename)s:%(lineno)s - %(funcName)20s() %(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger('root')

def log_to_file():
    i = 0
    while i < 10:
        logging.warning(i)
        i += 1


def log():
    logging.debug('Debug')
    logging.info('Info')
    logging.warning('Warning')
    logging.error('Error')
    logging.critical('Critical or Fatal')


if __name__ == '__main__':
    log_to_file()
