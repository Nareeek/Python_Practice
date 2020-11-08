import logging

#logging.disable()

file_obj = 'first_logging_messages.txt'
logging.basicConfig(filename = file_obj, level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.critical('This is critical logging')
logging.warning('This is warning logging')
logging.error('This is error logging')
logging.info('This is info logging')
logging.debug('This is debug logging')


def fibonachi(n):
    if n <= 1:
        logging.info('*****')
    logging.info('check {}'.format(n))
    if n <= 1:
        return n
    return fibonachi(n - 1) + fibonachi(n - 2)


n = int(input("Enter a number: "))
print(fibonachi(n))

logging.disable()
for i in range(n):
    logging.debug('fibonachi[{}] = {}'.format(i, fibonachi(i)))

file_obj = open(file_obj).close()
logging.info('end of program')



