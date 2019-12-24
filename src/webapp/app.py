import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from web.Server import server


def main():
    server.start()

main()
