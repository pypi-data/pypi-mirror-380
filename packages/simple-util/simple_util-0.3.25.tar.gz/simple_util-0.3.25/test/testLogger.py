import logging
import random
import sys
import os
import time

# 正确添加项目根路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from simple_util.slogger import create_logger

logger,handler = create_logger(logging.DEBUG,'appName','production',filename='log/app',file_type='log',backupCount=5,maxBytes=10485760,mutiple_process=False)


logger.info('hello world1',extra={"logCategory":'http'})
for i in range(10):
    time.sleep(random.randint(2,5))
    logger.info(f'hello world {i}')
    logger.info(f'hello world {i}',extra={"logCategory":'grpc'})