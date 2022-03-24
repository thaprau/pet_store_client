import time
import my_petstore_client
from my_petstore_client.rest import ApiException
from pprint import pprint


def main():
    configuration = my_petstore_client.Configuration()
    configuration.access_token = 'YOUR_ACCESS_TOKEN'

    # create an instance of the API class
    api_instance = my_petstore_client.PetApi(my_petstore_client.ApiClient(configuration))
    body = my_petstore_client.Pet(id=1, name="Test", photo_urls=["test"]) # Pet | Pet object that needs to be added to the store

    try:
        # Add a new pet to the store
        api_instance.add_pet(body)
    except ApiException as e:
        print("Exception when calling PetApi->add_pet: %s\n" % e)

    test = api_instance.get_pet_by_id(1)

    print(test)



if __name__ == "__main__":
    main()