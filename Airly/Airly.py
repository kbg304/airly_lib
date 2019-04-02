import urllib.request
import json

from .Installation import Installation
from .Measurement import Measurement

class Airly:

    def __init__(self, apikey):

        self.apikey = apikey
        self.url_installation = 'https://airapi.airly.eu/v2/installations/'
        self.url_measurment = 'https://airapi.airly.eu/v2/measurements/'
        self.headers = {'Accept': 'application/json', 'apikey': apikey}


    def installationsbyid(self, id):

        u = self.url_installation + str(id)
        req = urllib.request.Request(u, headers=self.headers)        
        result = urllib.request.urlopen(req)
        j = json.loads(result.read())
        installstion = Installation(j)
        return installstion
        
    
    def installationnearest(self, lat, lng, maxdistance = 3.0, maxresults = 1):

        u = self.url_installation + 'nearest?lat=' + str(lat) + '&lng=' + str(lng) + '&maxDistanceKM=' + str(maxdistance) + '&maxResults=' + str(maxresults)
        req = urllib.request.Request(u, headers=self.headers)
        result = urllib.request.urlopen(req)
        j = json.loads(result.read())
        n = len(j)
        installation = []
        for i in range(n):
            installation.append(Installation(j[i]))

        return installation

    def measurementbyid(self, id):

        u = self.url_measurment + 'installation?installationId=' + str(id)
        req = urllib.request.Request(u, headers=self.headers)
        result = urllib.request.urlopen(req)
        j = json.loads(result.read())
        measurement = Measurement(j)
        return measurement

    def measurementnearest(self, lat, lng, maxdistance = 3.0):

        u = self.url_measurment + 'nearest?lat=' + str(lat) + '&lng=' + str(lng)  + '&maxDistanceKM=' + str(maxdistance)
        req = urllib.request.Request(u, headers=self.headers)
        result = urllib.request.urlopen(req)
        j = json.loads(result.read())
        measurement = Measurement(j)
        return measurement

    def measurementpoint(self, lat, lng):

        u = self.url_measurment + 'point?lat=' + str(lat) + '&lng=' + str(lng)
        req = urllib.request.Request(u, headers=self.headers)
        result = urllib.request.urlopen(req)
        j = json.loads(result.read())
        measurement = Measurement(j)
        return measurement

    

    




    



