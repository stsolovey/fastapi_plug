from conn import conn

def check_token(token):
    
    
    query = """
    SELECT EXISTS(SELECT 1 FROM users WHERE token = '{}');
    """.format(token)
    
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    cursor.close()

    return result
     

def get_uid_by_token(token):

    query = """
    SELECT user_id FROM users WHERE token = '{}';
    """.format(token)
    
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    cursor.close()
    
    return result

