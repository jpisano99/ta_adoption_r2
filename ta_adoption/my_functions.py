from .Ssheet_class import Ssheet
from .settings import app
from .open_wb import open_wb
from .process_bookings_file_r2 import stan
from .build_dashboard import blanche
from .push_list_to_xls import push_list_to_xls
import time
import os


def get_status():
    print('now i am here')
    stan()
    print('Stan DONE !')
    return


def get_dashboard():
    print('now i am here')
    blanche()
    print('Blanche DONE !')
    return


def build_update():
    home = app['HOME']
    working_dir = app['WORKING_DIR']
    update_dir = app['UPDATES_DIR']
    archive_dir = app['ARCHIVES_DIR']

    path_to_main_dir = (os.path.join(home, working_dir))
    path_to_updates = (os.path.join(home, working_dir, update_dir))
    path_to_archives = (os.path.join(home, working_dir, archive_dir))

    update_files = os.listdir(path_to_updates)
    bookings = []
    start_row = 0
    as_of_date = ''

    if len(update_files) == 0:
        # NO update files exist
        print('ERROR: No Update files exist in:', path_to_updates)
        exit()
    else:
        for file in update_files:
            if file.find('Master Bookings') != -1:
                wb, ws = open_wb(file, 'updates')
                as_of_date = file[-13:-13+8]

                if start_row == 0:
                    # For the first workbook include the header row
                    start_row = 2
                elif start_row == 2:
                    # For subsequent workbooks skip the header
                    start_row = 3

                for row in range(start_row, ws.nrows):
                    bookings.append(ws.row_values(row))

    # Look in the main working directory for files to move to archive
    main_files = os.listdir(path_to_main_dir)
    for file in main_files:
        if file.find('Master Bookings') != -1:

            os.rename(os.path.join(path_to_main_dir, file), os.path.join(path_to_archives, file))
            print(file)

    # We have now created the bookings file lets write it
    print(len(bookings))
    push_list_to_xls(bookings, 'TA Master Bookings as of ', as_of_date)

    exit()

    return


