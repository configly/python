import configly
from configly import errors

configly.api_key = 'YOUR_API_KEY'

try:
    greetings_list = configly.get('greetings')
    if greetings_list is None:
        print("Can't find key")
    else:
        print('Greetings!\n')
        for saying in greetings_list:
            print(f'A greeting: {saying}')
except errors.InvalidApiKeyError as error:
    print(f'Invalid API Key: {error.message}')
except errors.ConfiglyRequestError as error:
    print(f'Generic error: {error.message}')
except errors.ConfiglyConnectionError as error:
    print(f'Connection error: {error.message}')
    # print(error.original_error)
