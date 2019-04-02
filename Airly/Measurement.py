from .MeasurementData import MeasurementData




class Measurement:

    def __init__(self, json):

        self.current = MeasurementData(json['current'])
        self.history = []
        for x in json['history']:
            self.history.append(MeasurementData(x))

        self.forecast = []
        for x in json['forecast']:
            self.forecast.append(MeasurementData(x))





