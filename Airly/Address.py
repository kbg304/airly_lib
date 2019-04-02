class Address:

    def __init__(self, data):
        self.country = data['country']
        self.city = data['city']
        self.street = data['street']
        self.number = str(data['number'])