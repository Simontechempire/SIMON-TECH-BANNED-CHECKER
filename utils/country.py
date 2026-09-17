import phonenumbers
from phonenumbers import geocoder


def get_country(phone):
    number = phonenumbers.parse(phone, None)

    country_code = phonenumbers.region_code_for_number(number)
    country_name = geocoder.country_name_for_number(number, "en")

    return country_code or "UN", country_name or "Unknown"
