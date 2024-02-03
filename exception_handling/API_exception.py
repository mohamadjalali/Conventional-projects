import json
from pprint import pprint
from http import HTTPStatus
from datetime import datetime




class APIException(Exception):
    """Base exception class"""
    
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API excepted occured'
    user_err_msg = 'We are sorry! User API excepted occured'


    def __init__(self, *args, user_err_msg=None):

        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)

        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg is not None:
            self.user_err_msg = user_err_msg


        
    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)


    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "http_status": self.http_status,
            "message": self.args[0] if self.args else self.internal_err_msg,
            "args": self.args[1:]
        }
        print(f'EXCEPTION: {datetime.utcnow().isoformat()}: {exception}')


 

try:
    raise APIException('Custom message...', 10, 20, user_err_msg='custom user msg')
except APIException as ex:
    print(ex.log_exception())
    print(ex.to_json())

