from kospider.logger import get_logger

class Spider:
    name = ''
    async def start(self):
        self.logger = get_logger('Spider')