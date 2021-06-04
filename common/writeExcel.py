'''
功能描述：将testCast的执行结果写入testdata的excel对应的real，status中
拿到TestCase的断言结果，写入到测试数据data.xls里面
实现逻辑：
1-导包：xlwt
2-打开data.xls文件
3-copy一份文件
4-找到sheet页，get_sheet
5-写入每条用例的real，status的值
5.1获取real，status所在的列
5.2根据id得到写入数据的行
5.3写入数据
6-保存文件

1-导包
2-定义写入数据类
    2.1-定义初始化方法
        准备写入的excel文件
        确定sheet页
    2.2定义写入数据的方法
        准备写入的测试结果
        准备写入的目标单元格的行和列
        开始写入
        保存文件
'''

# import xlrd
# from xlutils.copy import copy
# import os
# from common.logs import logger
#
# class WriteExcel():
#     def __init__(self,excel_name):
#         #求相对路径
#         cur_path = os.path.dirname(__file__)
#         self.fat_path = os.path.dirname(cur_path)
#         #拼接测试数据的路径
#         self.excel_dir = self.fat_path+r'/testData/'+excel_name
#         logger.debug(self.excel_dir)
#         #1、打开文件
#         self.r = xlrd.open_workbook(self.excel_dir)
#         #2、复制文件
#         self.w = copy(self.r)
#
#     def write_excel(self,id,real,status):
#         #3、读取sheet页
#         w_sheet = self.w.get_sheet(0)
#         #4、写入从testcase中得到的real，status值
#         #4.1获取文件的sheet页，读取第一行数据，返回列表，找到real和status的列
#         r_sheet = self.r.sheet_by_index(0)
#         key_list = r_sheet.row_values(0)
#         real_col = key_list.index('real')
#         status_col = key_list.index('status')
#         logger.debug(f'{real_col},{status_col}')
#         #4.2根据id得到每一行测试数据的行下标，写入数据
#         w_sheet.write(int(id),int(real_col),real)
#         w_sheet.write(int(id),int(status_col),status)
#         #保存文件
#         self.w.save(self.fat_path+r'\testData\data-result.xls')
#
# write = WriteExcel('data.xls')
#
# if __name__ == '__main__':
#     w = WriteExcel('data.xls')
#     for i in range(1,4):
#         w.write_excel(i,0,'success')

import xlrd,os
from xlutils.copy import copy

class WriteExcel():
    def __init__(self):
        #确定文件路径
        self.excel_dir = os.path.dirname(os.path.dirname(__file__))+'/testData/data.xls'
        #打开要写入的文件
        re = xlrd.open_workbook(self.excel_dir)
        #复制文件写入
        self.we = copy(re)
        #获取写入文件sheet页
        self.we_sheet = self.we.get_sheet(0)

    #确定写入参数，要写入的内容以参数传入
    def writeExcel(self,x,y,real,status):
        '''
        :param x: 写入数据的x轴，从0开始计数
        :param y: 写入数据的y轴，从0开始计数
        :param real: 写入的real值
        :param status:写入的status值
        :return:
        '''
        #写入数据
        self.we_sheet.write(int(x),y,real)
        self.we_sheet.write(int(x),y+1,status)
        #保存文件
        self.we.save(self.excel_dir)

write = WriteExcel()
if __name__ == '__main__':
    write.writeExcel(1,6,0,'success')


