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


 

# Application side
class ApplicationException(APIException):
    """Indicates an application error (not user caused) - 5xx HTTP type errors"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Generic server side exception.'
    user_err_msg = 'We are sorry. An exception error occured on our end.'


class DBException(ApplicationException):
    """General database exception"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database exception'
    user_err_msg = 'We are sorry. An exception error occured on our end.'


class DBConnectionError(DBException):
    """Indicates an error connecting to database"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database connection exception'
    user_err_msg = 'We are sorry. An exception error occured on our end.'




# Client side
class ClientException(APIException):
    """Indicates exceptin that was caused by user, not an internal error"""
    
    http_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = 'Client submitted bad request.'
    user_err_msg = 'A bad request was received.'


class NotFoundException(ClientException):
    """Indicates resource was not found"""
        
    http_status = HTTPStatus.NOT_FOUND
    internal_err_msg = 'Resource not found.'
    user_err_msg = 'Requeat resource was not found.'
        

class NotAuthorizedError(ClientException):
    """User is not authorized to perform requested action on resource"""

    http_status = HTTPStatus.UNAUTHORIZED
    internal_err_msg =  'Client not authorized to perform operation'
    user_err_msg = 'You are not authorized to perform this request.'






class Account:
    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type



def lookup_account_by_id(account_id):

    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f'Account number {account_id} is invalid.',
                              f'account_id = {account_id}',
                               'type error - account number not an integer')

    
    if account_id < 100:
        raise DBConnectionError('Permanent failure connecting to database', 'db=db01')

    elif account_id < 200:
        raise NotAuthorizedError('User does not have permissions to read thid account.',
                                f'account_id={account_id}')

    elif account_id < 300:
        raise NotFoundException('Account not found')

    elif account_id < 400:
        raise ApplicationException('Application exception was raised.')

    else:
        return Account(account_id, 'Savings')




def get_account(account_id):

    try:
        account = lookup_account_by_id(account_id)
    except APIException as ex:
        ex.log_exception()
        return ex.to_json()
    else:
        return HTTPStatus.OK, {'id': account.account_id, 'type': account.account_type}


print(get_account('ABC'))
