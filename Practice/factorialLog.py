import logging
logging.basicConfig(filename = 'firstLogMessage.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', filemode='w')


logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial({})'.format(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        if i >= 25:
            logging.debug('i is ' + str(i) + ', total is ' + str(total) + '\nit is already very big number, try smaller  0 <= n < 25')
            break
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial({})'.format(n))

    return total


print(factorial(int(input('Enter a number: '))))
logging.debug('End of program\n')


with open('firstLogMessage.txt',  'r') as logFile:
    print(logFile.read())
    print('ok')
