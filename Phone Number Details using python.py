import phonenumbers
from phonenumbers import geocoder

# specify the phone number to lookup
phone_number = "+917977890740"

# parse and validate the phone number
parsed_number = phonenumbers.parse(phone_number)
if not phonenumbers.is_valid_number(parsed_number):
    print("Invalid phone number")
    exit()

# get details about the phone number
country = phonenumbers.region_code_for_number(parsed_number)
carrier = phonenumbers.geocoder.description_for_number(parsed_number, "en")

# print the details
print(f"The Number You Entered is : {phone_number}")
print("Country: {}".format(country))
print("Carrier: {}".format(carrier))
