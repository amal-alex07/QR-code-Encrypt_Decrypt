# storage.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This storage.py file demonstrates the database process.


import constant

# writing to the database function, storing username and file id 
def Write_to_Database(con, username, file_id):
    query = f""" insert into encrypt (username, file_id)
                    values('{username}', '{file_id}')"""
    cur = con.cursor()
    cur.execute(query)
    con.commit()

# reading from the data base username and file id  
def Read_from_Database(con, username, file_id):
    query = f""" select key_status from encrypt
                    where username = '{username}' and
                    file_id = '{file_id}'"""
    cur = con.cursor()
    result = cur.execute(query).fetchone()
    return result

# function that helps to know about the key status whether it's expired or not, because the key is one time use. 
def Write_key_Status(con, username, file_id):
    query = f""" update encrypt set key_status=0
                    where username = '{username}' and
                    file_id = '{file_id}'"""
    cur = con.cursor()
    cur.execute(query)
    con.commit()

def get_password(con, username):
    query = f""" select password from user
                    where username = '{username}'"""
    cur = con.cursor()
    result = cur.execute(query).fetchone()
    return None if not result else result[0]