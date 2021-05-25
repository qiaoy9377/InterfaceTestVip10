'''
功能描述：接收testCase传入的接口请求测试数据，根据具体的请求逻辑完成接口测试，将接口返回的关键结果返回给testCase
1-接收testCase传入的测试数据
2-提取测试数据中的请求方式
3、根据methond进行判断
    3.1如果是get方法，则调用get请求
    3.2如果是post方法，则调用post方法
    .....
4、断言：采用errorcode断言，从接口请求的结果中，提取需要断言的字段
'''
import requests
from common.logs import logger
class ConfigHttp():
    #初始化函数
    def __init__(self,url,value,method):
        self.url = url
        self.value = value
        self.method = method
        self.header = {}
        #添加log日志
        logger.info('ConfigHttp文件初始化调试日志')
    #执行函数
    def run(self):
        logger.debug(f'请求方法为{self.method}')
        if self.method.lower() == 'get':
            return self.__get()      #调用run函数时需要返回数据给testcase，所以再加一个return
        elif self.method.lower() == 'post':
            return self.__post()
        elif self.method.lower() == 'put':
            return self.__put()

    def __get(self):
        #发起请求
        response = requests.get(url=self.url,params=eval(self.value),headers=self.header)
        #获取请求的状态码和errorCode
        status_code = response.status_code
        errorCode = response.json()['errorCode']
        #返回结果数据
        return status_code,errorCode
    def __post(self):
        #发起请求
        response = requests.post(url=self.url,data=eval(self.value),headers=self.header)
        #获取请求的状态码和errorCode
        status_code = response.status_code
        errorCode = response.json()['errorCode']
        logger.info(f'status_code是{status_code},errorCode是{errorCode}')
        #返回结果数据
        return status_code,errorCode
    def __put(self):
        #发起请求
        response = requests.put(url=self.url,data=eval(self.value),headers=self.header)
        #获取请求的状态码和errorCode
        status_code = response.status_code
        errorCode = response.json()['errorCode']
        #返回结果数据
        return status_code,errorCode
if __name__ == '__main__':
    #实例化列对象，需要传入参数
    list_data = [{'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'Method': 'post', 'value': "{'username':'liangchao','password':'123456'}", 'expect': '0', 'real': '', 'status': ''}, {'id': '2', 'interfaceUrl': 'https://www.wanandroid.com/user/register', 'name': 'register', 'Method': 'post', 'value': "{'username':'liangchao03','password':'123456','repassword':'123456'}", 'expect': '0', 'real': '', 'status': ''}, {'id': '3', 'interfaceUrl': 'https://www.wanandroid.com/user/logout/json', 'name': 'logout', 'Method': 'get', 'value': "{'username':'liangchao'}", 'expect': '0', 'real': '', 'status': ''}]
    url = list_data[0]['interfaceUrl']
    value = list_data[0]['value']
    method = list_data[0]['Method']
    ch = ConfigHttp(url,value,method)
    #调用执行用例的函数
    logger.debug(f'{ch.run()}')
    #print(ch.run())