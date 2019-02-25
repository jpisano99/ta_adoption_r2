from .Ssheet_class import Ssheet
from .settings import app
from .open_wb import open_wb
from .process_bookings_file_r2 import stan
from .build_dashboard import blanche


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