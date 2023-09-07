# qr
This project is the Backend implemented in python 

This project was generated with [Python 3.6]

## Development server
first install the following requirements

1. open the project folder in terminal, after that enetr the following command. 
 
    exif==1.3.5

    Flask==2.2.2

    Flask-Bcrypt==1.0.1

    Flask-Login==0.6.2

    Pillow==9.0.1

    pycryptodome==3.15.0

    PyQRCode==1.2.1

    requests==2.25.1

    Werkzeug==2.2.2

    pip install -U Flask

    pip install pycryptodome

    pip install pyqrcode

    pip install pillow

    pip install exif

    pip install PyQRCode

    pip install requests


Run ` flask --app api run` for a dev server. 

Navigate to `http://127.0.0.1:5000/`. - this is the develeopment server for Backend. 


## Important API's

http://127.0.0.1:5000/login - perform the user login and authentication

http://127.0.0.1:5000/encrypt - perform the encryption

http://127.0.0.1:5000/encrypt/preview/{filename} - perform the encrypted QR code preview and download

http://127.0.0.1:5000/decrypt/upload - perform the Enceyptrd QR code Upload and Decrypt.

http://127.0.0.1:5000/logout - perform the user logout.