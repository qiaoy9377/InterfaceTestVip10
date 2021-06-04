'''
功能描述：获取测试数据后，根据时间的请求参数methond，通过对应的方法请求接口
实现逻辑：
1、获取测试数据，调用readexcel内部提供的getdata方法
2、提取测试数据内的methond方法
3、根据methond进行判断
    3.1如果是get方法，则调用get请求
    3.2如果是post方法，则调用post方法
4、断言：采用errorcode断言，从接口请求的结果中，提取需要断言的字段
5、将实际提取的errorcode和excel中预期的进行比较
    5.1相同即通过，success
    5.2不同即失败，fail
6、将接口断言得到的结果写入excel
'''
#导入模块
import unittest,requests
from common.readExcel import ReadExcel
from ddt import ddt,data,unpack
from common.configHttp import ConfigHttp
from common.writeExcel import write

#类：测试用例

#1、从readexcel获取测试数据
#1.1实例化readexcel模块
test_data = ReadExcel('data.xls')
#1.2调用获取数据方法
data_list = test_data.getData()

#使用循环的话所有的测试数据会被作为一条用例执行，所以引入ddt，这样的话数据有多少个参数就会产生多少条用例
@ddt
class TestCase(unittest.TestCase):
    # #初始化函数-setUpClass,创建测试环境,是一个类方法
    # @classmethod
    # def setUpClass(cls) -> None:
    #     #1、从readexcel获取测试数据
    #     #1.1实例化readexcel模块
    #     test_data = ReadExcel('data.xls')
    #     #1.2调用获取数据方法
    #     cls.data_list = test_data.getData()
    #编写测试用例
    # @data(*cls.data_list)   #这种用法不支持，所以把读取数据内容挪到类外
    @data(*data_list)
    @unpack
    def test_request(self,id,interfaceUrl,name,Method,value,expect,real,status):
        #不需要循环
        # #2、循环提取method的值
        # for i in range(len(self.data_list)):
        #     method = self.data_list[i]['Method']
        #     url = self.data_list[i]['interfaceUrl']
        #     expect = self.data_list[i]['expect']
        #     body = eval(self.data_list[i]['value'])
        #2、提取数据信息-这里就不用初始化，直接用self后的参数就可以
        # url = interfaceUrl
        # method = Method
        # body = eval(value)
        # expect = expect
        #将这一块抽离成了ConfigHttp模块
        ch = ConfigHttp(interfaceUrl,value,Method)
        status_code,real = ch.run()
        # #3、判断method是什么方法，然后调用对应的请求
        # if method == 'get':
        #     response = requests.get(url=url,params=body)
        # elif method == 'post':
        #     response = requests.post(url=url,data=body)
        #4、断言errorcode
        try:
            #增加status——code断言
            self.assertEqual(str(status_code),'200')   #这个断言成功继续下一个断言，如果失败就不执行下面的信息了
            #real = response.json()['errorCode']       #这个就不需要自己取了，直接调用confighttp就可以返回结果
            self.assertEqual(str(real),str(expect))
            status = 'success'
        except AssertionError as msg:
            print('错误信息：',msg)
            status = 'fail'
            raise    #抛出异常
        finally:
            #将接口断言得到的结果写入excel
            # write.write_excel(id,real,status)
            write.writeExcel(id,6,real,status)

if __name__ == '__main__':
    unittest.main()