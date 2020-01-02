import sys
import logging
def get_logger(logname):
    Logger = logging.getLogger(logname)
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter  # 也可以直接给formatter赋值

    # 为logger添加的日志处理器
    Logger.addHandler(console_handler)
    Logger.setLevel(logging.INFO)
    return Logger