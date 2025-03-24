from abc import abstractmethod


class PaymentMethod:
    @abstractmethod
    def display_qr(self):
        pass

class VNPay(PaymentMethod):
    def display_qr(self):
        pixmap="../images/vnpay.jfif"
        return pixmap

class VietQR(PaymentMethod):
    def display_qr(self):
        pixmap="../images/VietQR.jpg"
        return pixmap

class Momo(PaymentMethod):
    def display_qr(self):
        pixmap="../images/qrcode.jpg"
        return pixmap

class PaymentMethodFactory:
    @staticmethod
    def get_qr(method):
        if method=='momo':
            return Momo()
        elif method=='vnpay':
            return VNPay()
        elif method=='vietqr':
            return VietQR()
        else:
            raise ValueError("Invalid payment method")
