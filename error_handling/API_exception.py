from pprint import pprint
from http import HTTPStatus
from datetime import datetime



class WidgetException(Exception):

    message = 'Generic internal exception.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

    
    def __init__(self, *args, customer_message=None):

        super().__init__(*args)
        if args:
            self.message = args[0]

        self.customer_message = customer_message if customer_message is not None else self.message


    def log_exception(self):
        exception = {
                "type": type(self).__name__,
                "message": self.message,
                "args": self.args[1:]
            }
        print(f'EXCEPTION: {datetime.utcnow().isoformat()}: {exception}')


    def from_exception(self):
        pass


    def format(self):
        pass




class SupplierException(WidgetException):
    message = 'Supplier exception.'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class NotManufacturedException(SupplierException):
    message = 'Widget is no longer manufactured by supplier'
    http_status = HTTPStatus.NOT_FOUND


class ProductionDelayedException(SupplierException):
    message = 'Widget production has been delayed by manufacturer'
    http_status = HTTPStatus.GATEWAY_TIMEOUT



class ShippingDelayedException(SupplierException):
    message = 'Widget shipping has been delayed by supplier'
    http_status = HTTPStatus.REQUEST_TIMEOUT




class CheckoutException(WidgetException):
    message = 'Checkout exception.'


class InventoryException(CheckoutException):
    message = 'Checkout inventory exception'


class OutOfStockException(InventoryException):
    message = 'Inventory out of stock'


class PricingException(CheckoutException):
    message = 'Checkout pricing exception'


class InvalidCouponCodeException(PricingException):
    message = 'Invalid checkout coupon code'


class CannotStackCouponException(PricingException):
    message = 'Cannot stack checkout coupon code'





try:
    raise CannotStackCouponException()
except CannotStackCouponException as ex:
    print(ex.log_exception())
    raise
