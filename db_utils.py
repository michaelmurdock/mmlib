# db_utils.py



def execute_query_for_single_value(cursor, query):
    '''
    query is a string containing a well-formed query that is executed
    against the specified cursor.
    RETURNS: the following tripe: (results_flag, err_msg, value)
    '''
    try:
        # Execute the query
        cursor.execute(query)

    except Exception as e:
        msg = 'Exception calling cursor.execute(). Query: %s, Error details: %s' % (query, str(e))
        return (False, msg, None)
    
    try:
        # Fetch the single result
        query_result = cursor.fetchone()

    except Exception as e:
        msg = 'Exception calling cursor.fetchone(). Query: %s, Error details: %s' % (query, str(e))
        return (False, msg, None)
    

    return (True, '', query_result[0])


def query_for_multiple_values(cursor, query):
    '''
    query is a string containing a well-formed query that is executed
    against the specified cursor.
    RETURNS: the following tripe: (results_flag, err_msg, x_values)
    '''
    try:
        # Execute the query
        cursor.execute(query)

    except Exception as e:
        msg = 'Exception calling cursor.execute(). Query: %s, Error details: %s' % (query, str(e))
        return (False, msg, None)
    
    try:
         
        # Fetch the result
        query_fetch_results = cursor.fetchall()

    except Exception as e:
        msg = 'Exception calling cursor.fetchall(). Details: %s' % (str(e))
        return (False, msg)
    

    return (True, '', query_fetch_results)

