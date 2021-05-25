'''
功能描述：读取testData目录下excel文件，获取测试数据，提供给testCase使用
分析：
目标数据存储格式[{'id':1,'url':'....'},{},{}]
1、导入xlrd包
2、打开文件（excel的路径和名称）
3、确定sheet页
4、确定数据的最大行-需要循环的次数
    4.1定义一个空列表保存最终的数据
    4.2读取第一行作为key列表
    4.3迭代读取剩下的所有行
    4.4将key列表和value列表组合成字典
    4.5将组合后的字典追加进列表
5、返回testData-return，别人调用的时候使用
'''
#导入模块
import xlrd
import os
#类：读取excel内容
    #属性：路径（包含文件名）
    #方法：获取数据
class ReadExcel():
    def __init__(self,excel_name):   #跟提供数据没关系的放到初始化属性里
        #寻找文件路径，相对路径，推荐使用，不受部署影响
        #1、获取当前路径
        current_path = os.path.dirname(__file__)
        #2、获取父路径
        father_path = os.path.dirname(current_path)
        #3、拼接测试文件路径
        file_path = father_path+'\\testData\\'+excel_name
        self.file_path = file_path

    def getData(self):    #提供数据，封装的方法放到方法中
        #1、打开文件-可以放入初始方法
        read_excel = xlrd.open_workbook(self.file_path)
        #2、获取sheet页-可以放入初始方法
        sheet1 = read_excel.sheet_by_index(0)
        #3、读取shee页中的数据
        #3.1创建一个空列表，用来存储数据
        content_list = []
        #3.2获取excel第一行的数据作为key
        key_list = sheet1.row_values(0)
        #3.3获取最大行数-可以放入初始方法
        rows = sheet1.nrows
        #3.4循环读取每一行的数据，得到value
        for row in range(1,rows):
            value_list = sheet1.row_values(row)
            #将key与value拼接得到每一行的字典数据
            row_dict = {key_list[i]:value_list[i] for i in range(len(key_list))}
            #将字典添加到列表
            content_list.append(row_dict)

        #3.5返回结果数据
        return content_list


if __name__ == '__main__':
    #实例化读取excel对象
    data = ReadExcel('data.xls')
    print(data.getData())
