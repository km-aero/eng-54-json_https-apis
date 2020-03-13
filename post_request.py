# post with requests

import requests
import json

# .dumps() - string in json
# .dump() - text file in json

# filipe = {
#     'name': 'FILIPE PV',
#     'SuperPower': 'Patience...',
#     'prep level': 'wine and batteries for the xbox'
# }
#
# file = 'file'
#
# json.dump(filipe, file)

json_body = json.dumps({
    'postcodes' : ['e147le', 'e161qn', 'ne301dp']
})

header = {'Content-type': 'application/json'}

url = 'http://api.postcodes.io/postcodes/'

post = requests.post(url, headers=header, data=json_body)

x = post.json()['result']

for i in x:
    print(i)