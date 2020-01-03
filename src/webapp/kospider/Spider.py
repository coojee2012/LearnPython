from kospider.logger import get_logger

class Spider:
    name = ''
    def __init__(self):
        self.logger = get_logger('Spider')
    async def start(self):
        self.logger.error('Need Overload Start Function In Your Spider')