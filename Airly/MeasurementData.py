from .Values import Values
from .Index import Index
from .Standard import Standard


class MeasurementData:

    def __init__(self, data):
        self.fromDateTime = data['fromDateTime']
        self.tillDateTime = data['tillDateTime']
        self.values = Values(data['values'])
        self.index = Index(data['indexes'][0])
        self.standard = data['standards']




        