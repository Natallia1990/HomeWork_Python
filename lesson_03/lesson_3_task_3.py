from address import Address

from mailing import Mailing

to_address = Address("230230", "Москва", "Вернадского", "15", "24")
from_address = Address("320320", "Санкт-Петербург", "Елизарова", "7", "12")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350,
    track="TR123456789"
)

message = (
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.room} в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.room}. "
    f"Стоимость {mailing.cost} рублей."
)
print(message)
