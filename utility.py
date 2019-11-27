class Address:
    def __init__(self, streetAddress, city, state, country):
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.country = country


class ContactDetails:
    def __init__(self, email, phoneNumber, address):
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
