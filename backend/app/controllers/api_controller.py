
from app.services.service import*
import json


def process_request(payload_data):
    
    #TODO User Validation Goes Here
    #** Here **#
    
    """
    Wrong User input
    
        ***If bad input***
    
    if isValid(payload_data) is false <---- isValid checks the user input and returns a status_code
        then return (status_code) 
        
    if status_code is BAD!!
        then return json with the error code and payload_data
        like this
        { 
            data : payload_data <---- the user input
            status: 'muy mal example or 'muy mal topic or muy mal both' TODO find a better code system!
            
        }
    
    otherwise:
        continue 

    """
    
    
    #bad_example = {'topic' : "drugs", 'example' : "How did Light Yagami die?",'difficulty': 5, "format": "mc"}
    
    
    
    format_type = payload_data['format']
    
    if format_type == 'simple':
        response = service_simple(payload_data)
    elif format_type == 'tf':
        response = service_tf(payload_data)
    elif format_type == 'mc':
        response = service_mc(payload_data)
        
    ##TODO Response Validation Goes here
    
    response_str = response  # Assuming response is a JSON string
    response_obj = json.loads(response_str)
    response_obj['status'] = "bueno"

    return response_obj