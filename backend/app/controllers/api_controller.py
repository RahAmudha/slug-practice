
from app.services.service import*


def process_request(payload_data):
    
    #TODO User Validation Goes Here
    #** Here **#
    
    format_type = payload_data['format']
    
    if format_type == 'simple':
        response = service_simple(payload_data)
    elif format_type == 'tf':
        response = service_tf(payload_data)
    elif format_type == 'mc':
        response = service_mc(payload_data)
        
    ##TODO Response Validation Goes here
    

    return jsonify(response)