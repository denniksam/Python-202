# Логування у Python
import logging
# Діють налаштування, актуальні  на перший лог. Тому
# конфігурувати треба до використання. Конфігурація стає
# актуальною і в інших модулях
logging.basicConfig(
    filename='logs.txt', 
    level=logging.INFO, 
    format='%(asctime)s %(levelname)s [%(filename)s::%(lineno)d] %(message)s %(args)s',
    datefmt='%Y-%m-%d %H:%M:%S')

import i10_module

def main() -> None :
    
    # logging.warning('Warning message')
    logging.error( 'DAO error', { 'sql': 'SELECT *', 
                                  'err': 'Syntax error' } )
    i10_module.log_warning()


if __name__ == "__main__" :
    main()

# https://docs.python.org/3/library/logging.html#logrecord-attributes