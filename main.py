'''
功能描述：
	1-加载测试用例到套件
	2-运行测试套件并生成报告
	3-报告的自动清理
	查找所有的测试用例，执行测试用例，并生成报告，实现自动清理报告
实现逻辑：
    1、使用loader加指测试用例到测试套件
    2、运行测试套件
    3、生成报告

    1-导入包，unittest、HTMLTestRunner
    2-使用testloader查找测试用例，生成测试套件
    3-使用htmltestrunner执行测试用例并生成报告
    4-实现自动清理报告的功能（1、自动判断报告的数据，2-每次运行前删除以前的旧报告，二者选其一）
        方案1：
            1-获取目录下所有文件
            2-统计filelist文件数量
            3-判断文件数量，是否超过5个：
                3.1不超过5个，pass
                3.2超过5个
                    3.2.1-拿到每个文件的创建时间
                    3.2.2-排序
                    3.2.3-删除文件
    5-自动将生成好的报告添加到附件并发送
'''
import unittest
import os,time
from HTMLTestRunner import HTMLTestRunner
from common.logs import logger
from common.configEmail import SendEmail

# #加载测试用例到测试套件
# test_suit = unittest.defaultTestLoader.discover(start_dir=os.path.dirname(__file__)+'/testCase',pattern='*.py',top_level_dir=None)
# #运行测试套件，生成报告
# #打开文件
# file_name = os.path.dirname(__file__)+'/report/report.html'
# f = open(file_name,'wb')
# #定义测试报告
# runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='interfacetest_report',description='测试用例执行情况如下：')
# #运行测试套件
# runner.run(test_suit)
# #关闭报告文件
# f.close()

cur_path = os.path.dirname(__file__)
def creat_suit():
    #确定用例目录
    case_dir = cur_path+'/testCase'
    #使用testloader方法加载测试套件
    test_suit = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='test*.py',top_level_dir=None)
    return test_suit

def auto_clear():
    #方案2：找到文件直接清空
    # #找到文freporti文件下的所有文件列表
    # file_list = os.listdir(cur_path+'/report')
    # #删除文件
    # for i in file_list:
    #     os.remove(cur_path+'/report/'+i)

    #方案1：判断文件数量大于5个就清报告
    #获取report下的文件数量
    file_list = os.listdir(cur_path+'/report')
    file_num = len(file_list)
    logger.debug(file_num)
    file_dict = {}
    file_ctime_list = []
    if file_num <= 5:
        pass
    else:
        # for i in range(file_num-5):
        #     os.remove(cur_path+'/report/'+file_list[i])

        #根据文件时间戳排序的方法实现
        #获取文件创建时间
        for file in file_list:
            file_ctime = os.path.getctime(cur_path+'/report/'+file)
            #以字典形式存放文件及时间
            file_dict[file_ctime]=file
            file_ctime_list.append(file_ctime)
        logger.debug(file_dict)
        #将时间戳进行排序
        file_ctime_list.sort()
        for i in range(file_num-5):
            os.remove(cur_path+'/report/'+file_dict[file_ctime_list[i]])


if __name__ == '__main__':
    auto_clear()
    suite = creat_suit()
    #执行测试套件生成报告
    #1-创建测试报告文件
    now_time = time.strftime('%Y-%m-%d_%H-%M-%S')
    report = cur_path+f'/report/report{now_time}.html'
    #2-打开报告文件以二进制写入
    fp = open(report,'wb')
    #3-设置生成报告格式
    runner = HTMLTestRunner(stream=fp,title='玩安卓接口测试报告',description='玩安卓接口测试执行情况：')
    #4-执行测试套件
    runner.run(suite)
    #5-关闭报告文件
    fp.close()
    #6-发送邮件
    se = SendEmail()
    se.sendEmail()
