__author__ = 'jpisano'

from datetime import datetime
from ta_adoption.my_secrets import passwords
import os

# database configuration settings
database = dict(
    DATABASE="cust_ref_db",
    USER="root",
    PASSWORD=passwords["DB_PASSWORD"],
    HOST="localhost"
)

# Smart sheet Config settings
ss_token = dict(
    SS_TOKEN=passwords["SS_TOKEN"]
)

# application predefined constants
app = dict(
    VERSION=1.0,
    GITHUB="{url}",
    HOME=os.path.expanduser("~"),
    WORKING_DIR='ta_adoption_data',
    UPDATES_DIR='ta_data_updates',
    ARCHIVES_DIR='archives',
    XLS_RENEWALS='TA Renewal Dates as of 1-27-19.xlsx',
    XLS_BOOKINGS='TA Master Bookings as of 2-14-19.xlsx',
    XLS_CUSTOMER='tmp_TA Customer List',
    XLS_ORDER_DETAIL='tmp_TA Order Details',
    XLS_ORDER_SUMMARY='tmp_TA Scrubbed Orders',
    XLS_BOOKINGS_TRASH='tmp Bookings Trash',
    XLS_DASHBOARD='tmp_TA Unified Adoption Dashboard',
    SS_SAAS='SaaS customer tracking',
    SS_CX='Tetration Engaged Customer Report',
    SS_AS='Tetration Shipping Notification & Invoicing Status',
    SS_COVERAGE='Tetration Coverage Map',
    SS_SKU='Tetration SKUs',
    SS_CUSTOMERS='TA Customer List',
    SS_DASHBOARD='TA Unified Adoption Dashboard',
    SS_WORKSPACE='Tetration Customer Adoption Workspace',
    AS_OF_DATE=datetime.now().strftime('_as_of_%m_%d_%Y')
)
