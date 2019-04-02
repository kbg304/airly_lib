class Values:

    def __init__(self, data):

        if len(data) == 6:
          self.pm1 = data[0]['value']
          self.pm25 = data[1]['value']
          self.pm10 = data[2]['value']
          self.pressure =data[3]['value']
          self.humidity = data[4]['value']
          self.temperature = data[5]['value']
        else:
            self.pm25 = data[0]['value']
            self.pm10 = data[1]['value']
        