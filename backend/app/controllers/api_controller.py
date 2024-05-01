
from app.services.service import*


#TODO Find a way to return success status alongside JSON data
def process_request_simple(data):

    response_data = service_simple(data)
    
    ##!Figure this out
    response = {
        'status': 'success',
        'data': response_data
    }
    
    return response_data

def process_request_mc(data):
    
    response_data = service_mc(data)
    
    ##!Figure this out
    response = {
        'status': 'success',
        'data': response_data
    }
    
    return response_data


def process_request_tf(data):
    
    response_data = service_tf(data)
    
    ##!Figure this out
    response = {
        'status': 'success',
        'data': response_data
    }
    
    return response_data



