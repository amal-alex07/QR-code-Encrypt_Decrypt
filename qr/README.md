# QR Backend

This project implements the backend functionality for QR code encryption and decryption in Python.

## Prerequisites

Before you can run the development server, make sure to install the following requirements:

```bash
pip install -r requirements.txt

```
Where requirements.txt contains the following dependencies:

``` bash
exif==1.3.5
Flask==2.2.2
Flask-Bcrypt==1.0.1
Flask-Login==0.6.2
Pillow==9.0.1
pycryptodome==3.15.0
PyQRCode==1.2.1
requests==2.25.1
Werkzeug==2.2.2

```
## Development Server
To start the development server, open a terminal and navigate to the project folder. Then, run the following command:

``` bash
flask --app api run
```
You can access the development server at http://127.0.0.1:5000/.

## Important APIs

Login: http://127.0.0.1:5000/login - Perform user login and authentication.

Encryption: http://127.0.0.1:5000/encrypt - Perform encryption.

QR Code Preview: http://127.0.0.1:5000/encrypt/preview/{filename} - Preview and download the encrypted QR code.

Decrypt and Upload: http://127.0.0.1:5000/decrypt/upload - Upload and decrypt an encrypted QR code.

Logout: http://127.0.0.1:5000/logout - Perform user logout.

Feel free to explore these APIs for QR code encryption and decryption.


``` bash

Please note that you should create a `requirements.txt` file containing the specified dependencies and replace `{filename}` with an actual filename when using the QR code preview API. This README file provides clear instructions for setting up and using your Python backend project.
```

