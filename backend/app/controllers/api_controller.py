
from app.controllers.user_val import isValid
from app.services.service import*
import json


def process_request(payload_data):
    
    errorType = {'1' : "Invalid academic topic", '2': "Invalid example question", '3' : "Topic and Question not related" }

    # user validation step
    response_obj = {}
    valid_code = isValid(payload_data)
    if  valid_code != '4':
        response_obj['status'] = "400"
        response_obj['message'] = "invalid request"
        response_obj['error_type'] = errorType[valid_code]
        json.dumps(response_obj)
        return response_obj

        
    
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
    response_obj['status'] = "200"
    response_obj['message'] = "success"

    return response_obj