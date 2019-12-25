import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
import config
from datetime import datetime

from aiowebserver.Server import server


def main():
    server.start()

main()
