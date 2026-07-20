from typing import Protocol


# =========================
# TASK 1. NOTIFICATION SYSTEM
# =========================

class Notifiable(Protocol):
    def send(self, message: str) -> None:
        ...


class RequiredSendMeta(type):
    def __new__(mcls, name, bases, attrs):
        if "send" not in attrs or not callable(attrs["send"]):
            raise TypeError(f"Class '{name}' must have a 'send' method")

        return super().__new__(mcls, name, bases, attrs)


class EmailNotification(metaclass=RequiredSendMeta):
    def send(self, message: str) -> None:
        print(f"Email notification: {message}")


class SmsNotification(metaclass=RequiredSendMeta):
    def send(self, message: str) -> None:
        print(f"SMS notification: {message}")


class TelegramNotification(metaclass=RequiredSendMeta):
    def send(self, message: str) -> None:
        print(f"Telegram notification: {message}")


notifications: list[Notifiable] = [
    EmailNotification(),
    SmsNotification(),
    TelegramNotification()
]

print("TASK 1")

for notification in notifications:
    notification.send("Hello!")

print()


# =========================
# TASK 2. PAYMENT SYSTEM
# =========================

class Payable(Protocol):
    def pay(self, amount: float) -> None:
        ...

    def refund(self, amount: float) -> None:
        ...


class PaymentMeta(type):
    def __new__(mcls, name, bases, attrs):
        required_methods = ["pay", "refund"]

        for method in required_methods:
            if method not in attrs or not callable(attrs[method]):
                raise TypeError(
                    f"Class '{name}' must have a '{method}' method"
                )

        return super().__new__(mcls, name, bases, attrs)


class CreditCardPayment(metaclass=PaymentMeta):
    def pay(self, amount: float) -> None:
        print(f"Credit Card payment: ${amount:.2f}")

    def refund(self, amount: float) -> None:
        print(f"Credit Card refund: ${amount:.2f}")


class PayPalPayment(metaclass=PaymentMeta):
    def pay(self, amount: float) -> None:
        print(f"PayPal payment: ${amount:.2f}")

    def refund(self, amount: float) -> None:
        print(f"PayPal refund: ${amount:.2f}")


class CryptoPayment(metaclass=PaymentMeta):
    def pay(self, amount: float) -> None:
        print(f"Crypto payment: ${amount:.2f}")

    def refund(self, amount: float) -> None:
        print(f"Crypto refund: ${amount:.2f}")


payments: list[Payable] = [
    CreditCardPayment(),
    PayPalPayment(),
    CryptoPayment()
]

print("TASK 2")

for payment in payments:
    payment.pay(100)
    payment.refund(25)

print()


# =========================
# TASK 3. TRANSPORT SYSTEM
# =========================

class Movable(Protocol):
    def move(self) -> None:
        ...

    def stop(self) -> None:
        ...


class TransportMeta(type):
    def __new__(mcls, name, bases, attrs):
        required_methods = ["move", "stop"]

        for method in required_methods:
            if method not in attrs or not callable(attrs[method]):
                raise TypeError(
                    f"Class '{name}' must have a '{method}' method"
                )

        attrs["category"] = "transport"

        return super().__new__(mcls, name, bases, attrs)


class Car(metaclass=TransportMeta):
    def move(self) -> None:
        print("The car is driving.")

    def stop(self) -> None:
        print("The car stopped.")


class Bicycle(metaclass=TransportMeta):
    def move(self) -> None:
        print("The bicycle is moving.")

    def stop(self) -> None:
        print("The bicycle stopped.")


class Train(metaclass=TransportMeta):
    def move(self) -> None:
        print("The train is moving.")

    def stop(self) -> None:
        print("The train stopped.")


class Airplane(metaclass=TransportMeta):
    def move(self) -> None:
        print("The airplane is flying.")

    def stop(self) -> None:
        print("The airplane stopped.")


vehicles: list[Movable] = [
    Car(),
    Bicycle(),
    Train(),
    Airplane()
]

print("TASK 3")

for vehicle in vehicles:
    vehicle.move()
    vehicle.stop()
    print(f"Category: {vehicle.category}")
    print()