from abc import ABC, abstractmethod
from uuid import uuid4


class PaymentProvider(ABC):
    def charge(self,user_id:str, amount_cents:int):
        pass


class StripePaymentProvider(PaymentProvider):
    def charge(self,user_id:str, amount_cents:int):
        print(f"Charging {user_id} with ${(amount_cents / 100):.2f}")
        return f"stripe-{uuid4()}"


class ApplePayPaymentProvider(PaymentProvider):
    def charge(self,user_id:str, amount_cents:int):
        print(f"Charging {user_id} with ${(amount_cents / 100):.2f}")
        return f"applepay-{uuid4()}"


class PayPalPaymentProvider(PaymentProvider):
    def charge(self,user_id:str, amount_cents:int):
        print(f"Charging {user_id} with ${(amount_cents / 100):.2f}")
        return f"paypal-{uuid4()}"


def create_provider(provider_type:str):
    providers = {
        "stripe": StripePaymentProvider(),
        "applepay": ApplePayPaymentProvider(),
        "paypal": PayPalPaymentProvider
    }

    if provider_type in providers.keys():
        return providers.get(provider_type)
    else:
        raise ValueError(f"No such provider: {provider_type}")


