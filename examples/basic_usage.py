import configly

# You can try this example out by setting the `CONFIGLY_API_KEY`
# environmental variable to our demo account: 'Dem0apiKEY'
configly.api_key = 'YOUR_API_KEY'

try:
    catalog = configly.get('store_catalog')

    # `get` returns None if the key is not found.
    if catalog is None:
        print('The key was not found')
    else:
        items = catalog['items']
        prices = catalog['prices']

        for index in range(0, len(items)):
            item = items[index]
            price = prices[index]
            if catalog['has_sale']:
                price = catalog['discount']*price
            print(f'{item}: {price:.2f} USD')
except Exception as error:
    print(error)
    # configly.errors.InvalidApiKeyError is thrown when there's an unknown API Key
    # configly.errors.ConfiglyRequestError is thrown on a timeout or failure to connection to the server
    # configly.errors.ConfiglyrequestError is thrown when the server responds with an error
