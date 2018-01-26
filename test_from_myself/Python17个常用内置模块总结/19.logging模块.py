import logging
print(dir(logging))

'''
Logger 记录器，暴露了应用程序代码能直接使用的接口。
Handler 处理器，将（记录器产生的）日志记录发送至合适的目的地。
Filter 过滤器，提供了更好的粒度控制，它可以决定输出哪些日志记录。
Formatter 格式化器，指明了最终输出中日志记录的布局。
'''
# 通过下面的方式进行简单配置输出方式与日志级别

# create logger
logger=logging.getLogger("example")
logger.setLevel(logging.DEBUG)

# create file handler
fh=logging.FileHandler("logger.log")
fh.setLevel(logging.WARN)

# create formatter
fmt="%(asctime)s-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt="%a %d %b %Y %H:%M:%S"
formatter=logging.Formatter(fmt,datefmt)

# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)

# print log info
logger.debug("debug")
logger.info("info")
logger.warn("warn")
logger.error("error")
logger.critical("critical")
input("..")

logg