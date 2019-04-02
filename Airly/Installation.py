from .Location import Location
from .Address import Address
from .Sponsor import Sponsor


class Installation:

    def __init__(self, json):

        self.id = json['id']
        self.location = Location(json['location'])
        self.address = Address(json['address'])
        self.elevation = json['elevation']
        self.sponsor = Sponsor(json['sponsor'])




