class Address(object):
    """
    Maintains a structure for all addresses
    :param str building: address line 1
    :param str street_name: address line 2
    :param str locality: address line 3
    :param str landmark: landmark
    :param str city: city of the address
    :param str state: state of the address
    :param str country: country of the address
    :param str zip_code: postal code of the address
    """

    def __init__(self, zip_code, street_name, locality, state, country, landmark, building, city):
        """
        Initialisation function for Address class
        """
        self.zip_code = zip_code
        self.street_name = street_name
        self.locality = locality
        self.city = city
        self.state = state
        self.country = country
        self.landmark = landmark
        self.building = building

    def __str__(self):
        """
        :return printable string for an object of Address class
        :rtype str
        """
        return str(
            f'Building: {self.building}\nStreet: {self.street_name}\nLocality: {self.locality}\nLandmark:'
            f' {self.landmark}\nCity: {self.city}\nState: {self.state}\nCountry: {self.country}\nZip Code: '
            f'{self.zip_code}')

    def input_address(self):
        """
        Input function to take values from the user and assign it to an object of Address class
        """
        self.building = input('Building: ')
        self.street_name = input('Street Name: ')
        self.locality = input('Locality: ')
        self.landmark = input('Landmark: ')
        self.city = input('City: ')
        self.state = input('State: ')
        self.country = input('Country: ')
        while True:
            self.zip_code = input('Zip Code: ')
            if self.zip_code.isnumeric() and len(self.zip_code) == 6:
                break
            else:
                print('\nInvalid Zip Code\n')

    def modify_address(self):
        """
        Modify function to modify an object of Address class
        """
        modify_address_list = ['1. Building', '2. Street', '3. Landmark', '4. City', '5. State', '6. Country',
                               '7. Zip Code', '8. Re-enter Address']
        for i in modify_address_list:
            print('\t' + i)
        print()
        ch = input('Command: ')
        if ch == '1':
            self.building = input('New Building: ')
        elif ch == '2':
            self.street_name = input('New Street Name: ')
        elif ch == '3':
            self.landmark = input('New Landmark: ')
        elif ch == '4':
            self.city = input('New City: ')
        elif ch == '5':
            self.state = input('New State: ')
        elif ch == '6':
            self.country = input('New Country: ')
        elif ch == '7':
            while True:
                self.zip_code = input('New Zip Code: ')
                if self.zip_code.isnumeric() and len(self.zip_code) == 6:
                    break
                else:
                    print('\nInvalid Zip Code\n')
        elif ch == '8':
            self.input_address()
        else:
            print('Invalid entry!')
