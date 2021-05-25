'''
功能描述：将testCast的执行结果写入testdata的excel对应的real，status中
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
'''

import xlwt
import xlrd
from xlutils.copy import copy
import os
from common.logs import logger

class WriteExcel():
    def __init__(self,excel_name):
        #求相对路径
        cur_path = os.path.dirname(__file__)
        self.fat_path = os.path.dirname(cur_path)
        #拼接测试数据的路径
        self.excel_dir = self.fat_path+r'/testData/'+excel_name
        logger.debug(self.excel_dir)
        #1、打开文件
        self.r = xlrd.open_workbook(self.excel_dir)
        #2、复制文件
        self.w = copy(self.r)

    def write_excel(self,id,real,status):
        #3、读取sheet页
        w_sheet = self.w.get_sheet(0)
        #4、写入从testcase中得到的real，status值
        #4.1获取文件的sheet页，读取第一行数据，返回列表，找到real和status的列
        r_sheet = self.r.sheet_by_index(0)
        key_list = r_sheet.row_values(0)
        real_col = key_list.index('real')
        status_col = key_list.index('status')
        logger.debug(f'{real_col},{status_col}')
        #4.2根据id得到每一行测试数据的行下标，写入数据
        w_sheet.write(int(id),int(real_col),real)
        w_sheet.write(int(id),int(status_col),status)
        #保存文件
        self.w.save(self.fat_path+r'\testData\data-result.xls')

write = WriteExcel('data.xls')

if __name__ == '__main__':
    w = WriteExcel('data.xls')
    for i in range(1,4):
        w.write_excel(i,0,'success')


