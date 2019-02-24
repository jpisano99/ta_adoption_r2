from flask import render_template, flash, redirect, url_for, request, session
from ta_adoption import application
# from application import db
from ta_adoption.models import *


@application.route('/')
def index():
    session['user'] = ''
    return render_template('index.html')

@application.route('/test')
def test():
    print ('hello')
    session['user'] = ''
    return render_template('index.html')

@application.route('/MyPage', methods=['GET', 'POST'])
def my_page():
    if request.method == 'POST':
        print('Got a POST: ', request.get_data())

    # return render_template('MyPage.html', lastnames=pss_names, my_name='any')

    pss_names = Coverage.query.all()
    return render_template('my_page.html', lastnames=pss_names, my_name='any')


@application.route('/outputs', methods=['GET', 'POST'])
def outputs():
    if request.method == 'POST':
        print('Got a POST: ', request.get_data())

    #pss_names = Coverage.query.all()
    pss_names = Coverage.newest_name(10)
    #pss_names = Coverage.newest()

    return render_template('outputs.html', lastnames=pss_names, my_name='any')

@application.route('/status')
def status():
    print('here i am')
    return render_template('index.html')

@application.route('/team', methods=['GET', 'POST'])
def team():
    print("/team got a ",request.method,request.data)
    #print ("is this it ?  ",request.form['next'])

    print("url_for index ", url_for('index'))
    # Default is 20 results per page
    my_pages = Coverage.query.paginate(per_page=10)
    print ("pages  ",my_pages.pages)
    print (db.session.query(Coverage).count())


    print (request.get_data())
    if request.method == 'POST':
        print('Got a POST: ', request.get_data())

    #pss_names = Coverage.query.all()
    coverages = Coverage.newest_name(12)
    #pss_names = Coverage.newest()

    return render_template('team.html', coverages=coverages, my_name='any')

@application.route('/add_name', methods=['GET', 'POST'])
def add_name():
    if request.method == 'POST':
        print('Got a POST from add name: ', request.get_data())
        #print("pss   ",request.form['pss_name'])

        for thing in request.form.items():
            print(thing)

        print(request.form['BtnClick'])
        if request.form['BtnClick'] == 'Done':
            return redirect('/')
        elif request.form['BtnClick'] == 'Submit':
            name = Coverage(pss_name = request.form['pss_name'], tsa_name = request.form['tsa_name'])
            #db.session.add(name)
            #db.session.commit()

    return render_template('add_name.html')


@application.route('/inputs', methods=['GET', 'POST'])
def inputs():
    if request.method == 'POST':
        print('Got a POST: ', request.get_data())

        for thing in request.form.items():
            print(thing)

        print(request.form['BtnClick'])
        if request.form['BtnClick'] == 'Done':
            return redirect('/')
        elif request.form['BtnClick'] == 'Submit':
            name = Coverage(pss_name = request.form['pss_name'], tsa_name = request.form['tsa_name'])
            db.session.add(name)
            db.session.commit()

    return render_template('inputs.html')

@application.route('/FlaskTesting')
def FlaskTesting():
    # Creates all tables *IF* they don't exist
    db.create_all()

    # To Create or Drop an Individual Table
    # models.Coverage.__table__.drop(db.session.bind)
    # models.Coverage.__table__.create(db.session.bind)
    return

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@application.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500
