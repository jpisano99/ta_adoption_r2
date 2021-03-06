import xlsxwriter
import datetime
import os
from .settings import app


def push_list_to_xls(my_list, xls_file, xls_time=app['PROD_DATE']):
    #
    # Get settings for file locations and names
    #
    home = app['HOME']
    working_dir = app['WORKING_DIR']
    path_to_files = os.path.join(home, working_dir)
    print(path_to_files)

    wb_file = os.path.join(path_to_files, xls_file + xls_time + '.xlsx')
    print(wb_file)
    #
    # Write the Excel File
    #
    workbook = xlsxwriter.Workbook(wb_file)
    worksheet = workbook.add_worksheet()

    # cell_format = workbook.add_format()
    # cell_format.set_bold()
    # cell_format.set_bg_color('#B7FFF9')
    #
    # cell_format.set_bg_color('#B7D9FF')
    # cell_format.set_bg_color('#FFFEB7')
    # # cell_format.set_font_color('red')

    xls_money = workbook.add_format({'num_format': '$#,##0'})
    xls_date = workbook.add_format({'num_format': 'mm / dd/ yyyy'})

    for row_num, my_row in enumerate(my_list):
        for col_num, cell_val in enumerate(my_row):
            if type(cell_val) is float:
                worksheet.write(row_num, col_num, cell_val, xls_money)
            elif isinstance(cell_val, datetime.datetime):
                worksheet.write(row_num, col_num, cell_val, xls_date)
            else:
                # worksheet.write(row_num, col_num, cell_val, cell_format)
                worksheet.write(row_num, col_num, cell_val)

    workbook.close()

    return
