import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

tel = "+34603188001"

ch_nber = phonenumbers.parse(tel, "CH")
print(geocoder.description_for_number(ch_nber, "pt"))
service_nber = phonenumbers.parse(tel, "RO")
print(carrier.name_for_number(service_nber, "pt"))


