'''
功能描述：定义公共的日志输出模块，供其他模块调试使用
实现逻辑：
1-导包
2-basiconfig定制日志参数
3-获取日志记录器，并返回结果
'''
import logging

def log():
    logging.basicConfig(level=logging.DEBUG,format='%(name)s--%(asctime)s--%(levelname)s--%(message)s')
    logger = logging.getLogger('InterfaceTest')   #log编辑器的名称
    return logger

logger = log()

if __name__ == '__main__':
    logger.info('日志调试')