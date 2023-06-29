def response(status, msg = None, data = None):

    res = {
        'status': status,
    }

    if msg is not None:
        res['message'] = msg
    
    if data is not None:
        res['data'] = data

    return res 
