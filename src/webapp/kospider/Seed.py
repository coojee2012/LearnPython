class Seed(dict):
    def __init__(self, url,callback, trytimes=0, level=1,data_type="normal",headers=None):
        super(Seed, self).__init__()
        self.url = str(url)
        self.trytimes = int(trytimes)
        self.level = int(level)
        self.data_type = data_type
        self.headers = headers
        self.callback = callback if callable(callback) else self.__callback

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

        # 允许动态设置key的值，不仅仅可以d[k]，也可以d.k
    def __setattr__(self, key, value):
        self[key] = value

    def __callback(self):
        raise AttributeError("callback must be funcation")