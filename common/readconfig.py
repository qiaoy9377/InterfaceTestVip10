'''
功能描述：读取config.ini文，获取目标的参数值，供其他模块使用
实现逻辑：
1-导包
2-准备目标文件
3-创建对象，调用read方法读取
4-对外提供读取某个section下的键值对的方法
'''
import configparser,os
from common.logs import logger

class ReadConfig():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        file = os.path.dirname(os.path.dirname(__file__))+'/config.ini'
        logger.info(f'config.ini文件的路径：{file}')
        self.conf.read(file,encoding='utf-8')
    def get_option(self,section):
        try:
            options = self.conf.items(section)
            logger.info(options)
            return options
        except Exception as msg:
            logger.error(f'系统报错，提示：{msg}' )

if __name__ == '__main__':
    rc = ReadConfig()
    rc.get_option('sendEmail')