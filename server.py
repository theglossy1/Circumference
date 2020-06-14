# https://python-socketio.readthedocs.io/en/latest/client.html
import html
import os
import string
import sys
import threading

import flask
from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room

app = Flask('circumference')
socketio = SocketIO(app)


COA_HOST = '192.168.1.88'
COA_PORT = 3799
COA_SECRET = 'zqzalxh1nblta2kd'


@socketio.on('join mysql')
def on_join_mysql():
    join_room('mysql')
    emit('get tables', {'sql': 'SHOW TABLES;'}, room='mysql')


@socketio.on('join coa')
def on_join_coa():
    join_room('coa')


@app.route('/coa', methods=['GET', 'POST'])
def send_coa():
    if 'sessionid' in request.args and 'update' in request.args:
        if all(char in string.hexdigits for char in request.args['sessionid']):
            sessionid = request.args['sessionid']
        update = request.args['update'].split(":")
        if len(update) == 1:
            url_format =  "URL Format: https://example.com/coa?sessionid=SESSION-ID&update=ATTRIBUTE:VALUE\n"
            url_format += "Example:    https://example.com/coa?sessionid=81c00008&update=MikroTik-Rate-Limit:500k/500k\n"
            r = flask.make_response(url_format)
            r.status_code = 400
            r.headers["Content-type"] = "text/plain"

        if all(char in string.digits+string.ascii_letters+'-' for char in update[0]):
            coa_data = {
                'Acct-Session-ID': sessionid,
                'host': COA_HOST,
                'port': COA_PORT,
                'secret': COA_SECRET,
                'attribute': update[0],
                'value': update[1]
            }
            r = flask.jsonify(coa_data)
            # emit('coa', coa_data, room='coa')
            # emit('send coa', coa_data, room='coa')
    else:
        r = flask.jsonify({'message': 'howdy'})

    try: r
    except:
        r = flask.make_response("Something unknown went wrong\n")
        r.status_code = 500
        r.headers["Content-type"] = "text/plain"
    return r

# @app.route('/mysql', methods=['GET', 'POST'])
# def mysql_commands():

def main():
    socketio.run(app, port=8383, host='0.0.0.0')


if __name__ == '__main__':
    main()
