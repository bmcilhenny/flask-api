
import sqlite3, render_template, url_for, request, redirect
from flask import Flask, render_template, g, jsonify
# from flask_sqlalchemy import SQLAlchemy



# For debugging purposes use ->
import pdb
import logging

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FIXMEEEEEEEEEEEE'
#db = SQLAlchemy(app)

DATABASE = './database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # db.row_factory = sqlite3.Row
        def make_dicts(cursor, row):
            # logging.warning(enumerate(row))
            return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))
        db.row_factory = make_dicts
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/meters')
def meters():

    # Create cursor
    # cur = get_db().cursor()

    #Get meters
    # result = cur.execute("SELECT * FROM meters")
    # meters = cur.fetchall()
    # pdb.set_trace()
    meters = query_db("SELECT * FROM meters")


    if len(meters) > 0:
        return render_template('meters.html', meters=meters)
    else:
        msg = 'No Meters Found'
        return render_template('meters.html', msg=msg)

    # cur.close()

    return render_template('articles.html')

@app.route('/meters/<string:id>')
def meter(id):
    # Create cursor
    # cur = get_db().cursor()

    #Get meters
    # result = cur.execute("SELECT * FROM meter_data WHERE meter_id= ? ORDER BY timestamp", id)
    # meter_data = cur.fetchall()
    # pdb.set_trace()
    meter_data = query_db("SELECT * FROM meter_data WHERE meter_id= ? ORDER BY timestamp", id)

    # cur.close()

    return jsonify(meter_data)

# @app.route('/addmeter', methods=['POST'])
# def addpost():
#     # label =
#     # meter_da
#
#     meter = Meter(label=label)
#
#     db.session.add(meter)
#     db.session.commit()
#
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
