from Airly import Airly

key = 'api_key'

airly = Airly(key)

m = airly.measurementbyid(204)
i = airly.installationsbyid(204)


city = i.address.city
street = i.address.street
temp = m.current.values.temperature
caqi = m.current.index.value

print(city)
print(street)
print('Temperature: ' + str(temp))
print('CAQI: ' + str(caqi))
