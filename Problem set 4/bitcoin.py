import requests
import json
import sys

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')


'''
print(json.dumps(response.json(), indent = 2)) # get rate

"bpi": {
    "USD": {
      "code": "USD",
      "symbol": "&#36;",
      "rate": "66,689.559",
      "description": "United States Dollar",
      "rate_float": 66689.5585
    }, ....


to get rate_float:

jsonresponse = response.json()
jresponse = jsonresponse['bpi']
currency = jresponse['USD']
rate = currency['rate_float']

'''
#simplify
jresponse = response.json()
rate = jresponse['bpi']['USD']['rate_float']



try:
    n = float(sys.argv[1])

    if len(sys.argv) == 2:
        value = n * rate
        print(f'${value:,.4f}')

except ValueError:
    sys.exit('Command-line argument is not a number')
except IndexError:
    sys.exit('Missing command-line argument')
