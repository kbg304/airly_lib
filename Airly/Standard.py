class Standard:

    def __init__(self, data):

        self.name = data['name']
        self.pollutant = data['pollutant']
        self.limit = data['limit']
        self.percent = data['percent']