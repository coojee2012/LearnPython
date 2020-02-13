import os

class Conf:
    def __init__(self):

        self.app = type("app", (object,), {
            "host": os.getenv("APP_HOST", "0.0.0.0"),
            "port": os.getenv("APP_PORT", "8000"),
            "static":os.path.join(os.path.dirname(os.path.abspath(__file__)),'www', 'static'),
            "routedir": os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aiowebserver','routers'),
            "templetdir":os.path.join(os.path.dirname(os.path.abspath(__file__)),'www', 'templates'),
            "uploaddir":os.path.join(os.path.dirname(os.path.abspath(__file__)),'www', 'static','uploads'),
        })
        self.redis = type("redis", (object,), {
            "host": os.getenv("REDIS_HOST", "127.0.0.1"),
            "port": int(os.getenv("REDIS_PORT", "6379")),
            "password": os.getenv("REDIS_PASSWORD", "test"), # 空位None
            "db": os.getenv("REDIS_DB", None),
            "maxsize": int(os.getenv("REDIS_MAXSIZE", "10")),
            "minsize": int(os.getenv("REDIS_MINSIZE", "1")),
        })
        self.mysql = type("mysql", (object,), {
            "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
            "port": int(os.getenv("MYSQL_PORT", "3307")),
            "password": os.getenv("MYSQL_PASSWORD", "1234"),
            "user": os.getenv("MYSQL_USER", "root"),
            "database": os.getenv("MYSQL_DATABASE", "awesome"),
            "charset": os.getenv("MYSQL_CHARSET", "utf8"),
            "autocommit": os.getenv("MYSQL_AUTOCOMMIT", "True"),
            "maxsize": int(os.getenv("MYSQL_MAXSIZE", "10")),
            "minsize": int(os.getenv("MYSQL_MINSIZE", "1")),
        })

config = Conf()