from xlrd import open_workbook 
from xlwt import easyxf
from xlutils.copy import copy
import os

excel_address = r'/Users/zhoufengting/projet/donee.xls'
work_book = open_workbook(excel_address,formatting_info=True)
wb = copy(work_book)
sheet = wb.get_sheet(0)
sheet.write(1,2,'test')
os.remove(excel_address)
wb.save(excel_address)


# save all the data in a list and then input it in excel?