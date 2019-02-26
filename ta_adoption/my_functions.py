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


def get_fresh_data():
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

    # Look in the "ta_data_updates" dir
    # this is where we place newly updated sheets to be put into production
    if len(update_files) == 0:
        # NO update files exist so throw an error ?
        print('ERROR: No Update files exist in:', path_to_updates)
        exit()
    else:
        for file in update_files:

            # When we find a "Master Bookings" file
            # Add the rows to the "bookings" list
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

    # Look in the main working directory for current production files
    # and move to a dated archive folder in the 'archives' directory

    # Get the as_of_date from the current production files
    # so we can create the properly named archive folder
    main_files = os.listdir(path_to_main_dir)
    for file in main_files:
        if file.find('Master Bookings') != -1:
            archive_date = file[-13:-13 + 8]

    # Make the archive directory we need
    os.mkdir(os.path.join(path_to_archives, archive_date+" Updates"))
    archive_folder_path = os.path.join(path_to_archives, archive_date+" Updates")

    for file in main_files:
        if file.find('Master Bookings') != -1:
            os.rename(os.path.join(path_to_main_dir, file), os.path.join(archive_folder_path, file))
        elif file.find('Renewal') != -1:
            os.rename(os.path.join(path_to_main_dir, file), os.path.join(archive_folder_path, file))

    # We have now created the bookings list lets write it
    print('New Master Bookings has ', len(bookings), ' line items')
    push_list_to_xls(bookings, 'TA Master Bookings as of ', as_of_date)

    # Move the Renewals file into production from updates director
    renewal_file = 'TA Renewal Dates as of '+as_of_date+'.xlsx'
    os.rename(os.path.join(path_to_updates, renewal_file), os.path.join(path_to_main_dir, renewal_file))

    # Create a list of just AS services from the bookings file
    # This is for AS staffing services

    return

def get_prod_date():
    print(app['XLS_TEST'])
    # path_to_main_dir = (os.path.join(app['HOME'], app['WORKING_DIR']))
    # main_files = os.listdir(path_to_main_dir)
    # prod_date = [file[-13:-13 + 8] for file in main_files if file.find('Master Bookings') != -1]
    return

