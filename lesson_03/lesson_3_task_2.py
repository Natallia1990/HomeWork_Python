from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", 3100, "+7123123456789"),
    Smartphone("Iphone", 17, "+7123123456781"),
    Smartphone("Samsung", "S30", "+7123123456782"),
    Smartphone("Huawei", 200, "+7123123456783"),
    Smartphone("Honor", "C200", "+7123123456784")
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model} . {smartphone.number}")
