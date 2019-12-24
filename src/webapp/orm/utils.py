import logging; logging.basicConfig(level=logging.INFO)

def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)

def log(sql, args=()):
    logging.info('SQL: %s' % sql)
