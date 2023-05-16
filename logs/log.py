"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: log.py
 @DateTime: 2023/4/7 8:29
 @SoftWare: PyCharm
"""
"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: log.py
 @DateTime: 2023/3/29 16:01
 @SoftWare: PyCharm
"""
import logging

class Logger(object):
    _instance = None
    logger = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls.logger = logging.Logger('root')
            handle = logging.FileHandler(r'')
            handle.setLevel(logging.DEBUG)
            format = logging.Formatter("时间是:%(asctime)s --文件名:%(filename)s--行号:[line:%(lineno)d] --等级:%(levelname)s --信息:%(message)s")
            handle.setFormatter(format)
            cls.logger.addHandler(handle)
        return cls._instance

    def info(self,msg):
        self.logger.info(msg)

    def debug(self,msg):
        self.logger.debug(msg)

    def warning(self,msg):
        self.logger.warning(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)