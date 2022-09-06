from conn import conn
import hashlib
import string
import random

def add_user(login, password):
    
    if check_login_if_exists(login):
        return 'login {} is already taken'.format(login)
    if password == '':
        return 'password is too short'
    
    token = (random_string(190))
    hpass = hashpassword(password)
    
    query = """
    INSERT INTO users (login, password, token) VALUES('{}', '{}', '{}');
    """.format(login, hpass, token)
    
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    
    return token

def autorisation(login, password):
    
    if check_login_if_exists(login)==False:
        return 'login or password is incorrect'
    
    if check_login_and_password_mach(login, password)==False:
        return 'login or password is incorrect'
    
    token = (random_string(190))
    
    query = """
    UPDATE users
    SET token = '{}',
    timetag = NOW()
    WHERE login='{}';
    """.format(token, login)
    
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    
    return token

    
def check_login_if_exists(login):
    cursor = conn.cursor()
    
    query = """
    SELECT EXISTS(SELECT 1 FROM users WHERE login = '{}');
    """.format(login)
    
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    return result[0][0]

def check_login_and_password_mach(login, password):
    cursor = conn.cursor()
    hpass = hashpassword(password)
    
    query = """
    SELECT EXISTS(SELECT 1 FROM users WHERE login = '{}' AND password = '{}');
    """.format(login, hpass)
    
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    return result[0][0]

def random_string(length):
    return "=="+''.join(random.choice(string.ascii_letters) for m in range(length))+"=="

def hashpassword(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()