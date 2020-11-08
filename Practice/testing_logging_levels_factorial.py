import logging

#logging.disable()

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.critical('This is critical logging')
logging.warning('This is warning logging')
logging.error('This is error logging')
logging.info('This is info logging')
logging.debug('This is debug logging')

N = int(input('Factorial number: '))
logging.info('reserved array of factorial numbers up to {} number'.format(N))

array = [0]
prod = 1
force = False

for i in range(1, N + 1):
    prod *= i
    array.append(prod)
    logging.debug('{} * {} = {}'.format(int(prod / i), i, prod))
    logging.debug('append:{}'.format(prod))
    if len(str(array[-1])) > 50:
        limit_number = i
        force = True
        logging.info('The factorial of {} = {} already too big, need stop'.format(i, array[-1]))
        break
    
    
    
logging.debug('arr = {}'.format(array))

if not force:
    n = int(input('Enter a number for checking factorial: '))
else:
    n = int(input('Enter a number for checking factorial in range[{},{}]: '.format(1, limit_number)))
    
try:
    logging.info('the factorial of {} is {}'.format(n, array[n]))
except:
    if force:
        logging.info('the programm reach {} number and stop, becouse the factorial {} too big'.format(limit_number, array[-1]))
    else:
        logging.info('the number is not in range[{},{}]'.format(1, N))
    
logging.info('End of programm')

#logging.disable()

logging.error('This is error logging without disabling')
logging.warning('This is warning logging without disabling')
logging.critical('This is critical logging without disabling')
    
    
    
