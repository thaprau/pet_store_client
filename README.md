# my-petstore-client
This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.6
- Package version: 0.0.1
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import my_petstore_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import my_petstore_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import my_petstore_client
from my_petstore_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
configuration = my_petstore_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = my_petstore_client.PetApi(my_petstore_client.ApiClient(configuration))
body = my_petstore_client.Pet() # Pet | Pet object that needs to be added to the store

try:
    # Add a new pet to the store
    api_instance.add_pet(body)
except ApiException as e:
    print("Exception when calling PetApi->add_pet: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = my_petstore_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = my_petstore_client.PetApi(my_petstore_client.ApiClient(configuration))
pet_id = 789 # int | Pet id to delete
api_key = 'api_key_example' # str |  (optional)

try:
    # Deletes a pet
    api_instance.delete_pet(pet_id, api_key=api_key)
except ApiException as e:
    print("Exception when calling PetApi->delete_pet: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = my_petstore_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = my_petstore_client.PetApi(my_petstore_client.ApiClient(configuration))
status = ['status_example'] # list[str] | Status values that need to be considered for filter

try:
    # Finds Pets by status
    api_response = api_instance.find_pets_by_status(status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->find_pets_by_status: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = my_petstore_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = my_petstore_client.PetApi(my_petstore_client.ApiClient(configuration))
tags = ['tags_example'] # list[str] | Tags to filter by

try:
    # Finds Pets by tags
    api_response = api_instance.find_pets_by_tags(tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->find_pets_by_tags: %s\n" % e)

# Configure API key authorization: api_key
configuration = my_petstore_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = my_petstore_client.PetApi(my_petstore_client.ApiClient(configuration))
pet_id = 789 # int | ID of pet to return

try:
    # Find pet by ID
    api_response = api_instance.get_pet_by_id(pet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->get_pet_by_id: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = my_petstore_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = my_petstore_client.PetApi(my_petstore_client.ApiClient(configuration))
body = my_petstore_client.Pet() # Pet | Pet object that needs to be added to the store

try:
    # Update an existing pet
    api_instance.update_pet(body)
except ApiException as e:
    print("Exception when calling PetApi->update_pet: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = my_petstore_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = my_petstore_client.PetApi(my_petstore_client.ApiClient(configuration))
pet_id = 789 # int | ID of pet that needs to be updated
name = 'name_example' # str |  (optional)
status = 'status_example' # str |  (optional)

try:
    # Updates a pet in the store with form data
    api_instance.update_pet_with_form(pet_id, name=name, status=status)
except ApiException as e:
    print("Exception when calling PetApi->update_pet_with_form: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = my_petstore_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = my_petstore_client.PetApi(my_petstore_client.ApiClient(configuration))
pet_id = 789 # int | ID of pet to update
additional_metadata = 'additional_metadata_example' # str |  (optional)
file = 'file_example' # str |  (optional)

try:
    # uploads an image
    api_response = api_instance.upload_file(pet_id, additional_metadata=additional_metadata, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->upload_file: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://petstore.swagger.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PetApi* | [**add_pet**](docs/PetApi.md#add_pet) | **POST** /pet | Add a new pet to the store
*PetApi* | [**delete_pet**](docs/PetApi.md#delete_pet) | **DELETE** /pet/{petId} | Deletes a pet
*PetApi* | [**find_pets_by_status**](docs/PetApi.md#find_pets_by_status) | **GET** /pet/findByStatus | Finds Pets by status
*PetApi* | [**find_pets_by_tags**](docs/PetApi.md#find_pets_by_tags) | **GET** /pet/findByTags | Finds Pets by tags
*PetApi* | [**get_pet_by_id**](docs/PetApi.md#get_pet_by_id) | **GET** /pet/{petId} | Find pet by ID
*PetApi* | [**update_pet**](docs/PetApi.md#update_pet) | **PUT** /pet | Update an existing pet
*PetApi* | [**update_pet_with_form**](docs/PetApi.md#update_pet_with_form) | **POST** /pet/{petId} | Updates a pet in the store with form data
*PetApi* | [**upload_file**](docs/PetApi.md#upload_file) | **POST** /pet/{petId}/uploadImage | uploads an image
*StoreApi* | [**delete_order**](docs/StoreApi.md#delete_order) | **DELETE** /store/order/{orderId} | Delete purchase order by ID
*StoreApi* | [**get_inventory**](docs/StoreApi.md#get_inventory) | **GET** /store/inventory | Returns pet inventories by status
*StoreApi* | [**get_order_by_id**](docs/StoreApi.md#get_order_by_id) | **GET** /store/order/{orderId} | Find purchase order by ID
*StoreApi* | [**place_order**](docs/StoreApi.md#place_order) | **POST** /store/order | Place an order for a pet
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | Create user
*UserApi* | [**create_users_with_array_input**](docs/UserApi.md#create_users_with_array_input) | **POST** /user/createWithArray | Creates list of users with given input array
*UserApi* | [**create_users_with_list_input**](docs/UserApi.md#create_users_with_list_input) | **POST** /user/createWithList | Creates list of users with given input array
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user/{username} | Delete user
*UserApi* | [**get_user_by_name**](docs/UserApi.md#get_user_by_name) | **GET** /user/{username} | Get user by user name
*UserApi* | [**login_user**](docs/UserApi.md#login_user) | **GET** /user/login | Logs user into the system
*UserApi* | [**logout_user**](docs/UserApi.md#logout_user) | **GET** /user/logout | Logs out current logged in user session
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user/{username} | Updated user

## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [Category](docs/Category.md)
 - [Order](docs/Order.md)
 - [Pet](docs/Pet.md)
 - [PetIdUploadImageBody](docs/PetIdUploadImageBody.md)
 - [PetPetIdBody](docs/PetPetIdBody.md)
 - [Tag](docs/Tag.md)
 - [User](docs/User.md)

## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## petstore_auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://petstore.swagger.io/oauth/authorize
- **Scopes**: 
 - **read:pets**: read your pets
 - **write:pets**: modify pets in your account


## Author

apiteam@swagger.io
