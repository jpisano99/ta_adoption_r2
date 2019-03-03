from ta_adoption import application
# from ta_adoption.my_functions import get_as_skus
# from application import db
# from flask_script import Manager, prompt_bool
# from sqlalchemy_utils import create_database

# manager = Manager(application)

if __name__ == "__main__":
    print("**************************")
    print ('In application.py Name: ',__name__)
    print (' In application.py File: ',__file__)
    print("**************************")
    # get_as_skus()
    application.run(debug=False)

