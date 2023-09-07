import os
import uuid
import json
import sqlite3
from flask import Flask
from flask import flash
from flask import request
from flask import redirect
from flask import url_for
from flask import send_from_directory
from flask import session
from flask_cors import CORS
from flask import jsonify as _json

# from werkzeug.security import get_password_hash
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

import constant
from decors import logged_in
from storage import get_password
from code import Encrypt, Decrypt
from image import Qr_Generation, Write_to_Metadata, Read_to_MetaData
from storage import Write_to_Database, Read_from_Database, Write_key_Status


connection = sqlite3.connect(constant.DB_NAME, check_same_thread=False)

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = constant.SESSION_SECRET

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        password_db = get_password(connection, username)
        message = "unauthorized access"
        status = 401
        if password_db:
            if check_password_hash(password_db, password):
                session['username'] = username
                message = 'success'
                status = 200
        response =  _json({
            'status': status,
            'message': message,
            'opr': 'login'
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route("/encrypt", methods=['POST'])
@logged_in
def encrypt_post():
        message = request.form['message']
        key = request.form['key']
        
        username = session['username']
        file_uuid = str(uuid.uuid4())

        u = Encrypt(username, key, constant.PADDING_SIZE)
        f = Encrypt(file_uuid, key, constant.PADDING_SIZE)
        c = Encrypt(message, key)

        filename = Qr_Generation()
        Write_to_Metadata(filename, u+f+c)
        Write_to_Database(connection, username, file_uuid)
        return json.dumps({
            'status': 200,
            'message': 'success',
            'secret': filename,
            'opr': 'encrypt'
        })

@app.route('/encrypt/preview/<filename>', methods=['GET'])
@logged_in
def preview(filename):
    # filename = constant.CONST_PREVIEW_URL+filename
    # print(filename, "This is file name...!")
    return send_from_directory(constant.PNG_PATH, filename + '.png')

@app.route('/encrypt/download/<filename>', methods=['GET'])
@logged_in
def download(filename):
    return send_from_directory(constant.JPG_PATH, filename + '.jpg')

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in constant.ALLOWED_EXTENSIONS

@app.route("/decrypt/upload", methods=['POST'])
@logged_in
def upload_image():
    status = 401
    message = 'error'
    secret = None
    file = request.files['image']
    key = request.form['key']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(constant.UPLOADS, filename))
        em = Read_to_MetaData(os.path.join(constant.UPLOADS, filename))

        try:
            ud = Decrypt(em[:constant.NAME_INDEXING], key)
            fd = Decrypt(em[constant.NAME_INDEXING:constant.MSG_INDEXING], key)
            result = Read_from_Database(connection, ud, fd)
            if result[0]:
                cd = Decrypt(em[constant.MSG_INDEXING:], key)
                Write_key_Status(connection, ud, fd)
                status = 200
                message = 'success'
                secret = cd
        except UnicodeDecodeError as e:
            message = 'invalid key'
        # return redirect(url_for('download_file', name=filename))
    
    return json.dumps({
        'status': status,
        'message': message,
        'secret': secret,
        'opr': 'decrypt'
    })

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('username', None)
    return json.dumps({
        'status': 200,
        'message': "logged out",
        'opr': 'logout'
    })
    