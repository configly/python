try:
    copy = configly.get('en_copy')
    if copy is None:
        print("No copy was found")
    else:
      print(copy)
except errors.InvalidApiKeyError as error:
    print(f"Invalid API Key: {error.message}")
except errors.ConfiglyRequestError as error:
    print(f"Generic error: {error.message}")
    # You can access the response via error.response
except errors.ConfiglyConnectionError as error:
    print(f"Connection error: {error.message}")
    # You can access the internal error via original_error
