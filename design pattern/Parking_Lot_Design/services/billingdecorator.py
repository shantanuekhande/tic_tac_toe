from abc import ABC, abstractmethod

# Base interface
class Billing(ABC):
    @abstractmethod
    def calculate(self, base_amount: float) -> float:
        pass


# Abstract Decorator
class BillingDecorator(Billing):
    def __init__(self, wrapped: Billing):
        self.wrapped = wrapped

    @abstractmethod
    def calculate(self, base_amount: float) -> float:
        pass


# Root component (plain billing, no changes)
class BaseBilling(Billing):
    def calculate(self, base_amount: float) -> float:
        return base_amount


########################## Vehicle Decorators ############################
class CarBilling(BillingDecorator):
    def calculate(self, base_amount: float) -> float:
        return self.wrapped.calculate(base_amount) * 1.0


class BikeBilling(BillingDecorator):
    def calculate(self, base_amount: float) -> float:
        return self.wrapped.calculate(base_amount) * 0.5


class TruckBilling(BillingDecorator):
    def calculate(self, base_amount: float) -> float:
        return self.wrapped.calculate(base_amount) * 1.5



class EVBilling(BillingDecorator):
    def calculate(self, base_amount: float) -> float:
        return self.wrapped.calculate(base_amount) * 0.7  # e.g., 30% discount for EVs

############################### User Decorators ############################
class RegularBilling(BillingDecorator):
    def calculate(self, base_amount: float) -> float:
        return self.wrapped.calculate(base_amount)


class VIPBilling(BillingDecorator):
    def calculate(self, base_amount: float) -> float:
        return self.wrapped.calculate(base_amount) * 0.8  # 20% discount


class EmployeeBilling(BillingDecorator):
    def calculate(self, base_amount: float) -> float:
        return 0  # free parking
