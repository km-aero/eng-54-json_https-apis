import requests

# GET request
# URL = path + arguments

# postcode.io

# capture the input --> decrypt json to dictionary

# get some data out

# Variables for GET request:
path = 'http://api.postcodes.io/postcodes/'
argument = 'E161QN'
url = path + argument

get = requests.get(url)
# print(get.content)

# JSON decoder

dict_postcode = get.json()
print(dict_postcode['result']['european_electoral_region'])
print(dict_postcode['result']['outcode'])
print(dict_postcode['result']['longitude'])
print(dict_postcode['result']['latitude'])