# ReCodEx Client Library

A client API library for the [ReCodEx](https://recodex.mff.cuni.cz/) system.
This library can be used in custom scripts and command-line interfaces for fine-grained interactions with the system.

## Installation

The recommended way to install the library is via `pip`. Python 3.11 is recommended, but other versions may also work:

```bash
PIP_EXTRA_INDEX_URL="https://test.pypi.org/simple/" pip install recodex-pylib
```

### Installation from Source

For developers or those who prefer to install directly from the source code, follow these steps:

```bash
# make sure to run these commands from the root of the repository
./commands/initRepo.sh
source venv/bin/activate
```

This will install the library in interactive mode, meaning that changes made to the source afterwards will be automatically reflected in the installation.

The script will clone the `swagger-api/swagger-codegen` repository, install it, generate code from an OpenAPI Specification file, and setup a Python `venv` environment.
Note that this process may take several minutes.

## Usage

### Creating Client Instance

The Client class is the primary interface with the library and can be created using an existing API token or ReCodEx credentials.

By using the `get_client_from_token` and `get_client_from_credentials` functions shown below, a local session file will be created that holds the host URL and API token.
In case a session already exists, the functions will remove it and create a new one.
Note that the `get_client_from_credentials` function will always communicate with the server to create a new API token, please use the function below if there is a session available.

The `get_client_from_session` function can be used to create a Client instance directly from the session file without communicating with the server.

It is not recommended to instantiate the Client directly (without the `client_factory`), because doing so will not create a session.

```python
from recodex_pylib import client_factory
from recodex_pylib.client import Client

# URL of the API server
api_url = "http://localhost:4000"

# JWT token used for authentication
api_token = "eyJhbGciOi..."

username = "user"
password = "pwd"

# creating a client with an API token (also creates a session file that stores the API token)
client = client_factory.get_client_from_token(api_url, api_token, verbose=True)

# creating a client with ReCodEx credentials (also creates a session file that stores a newly created API token)
client = client_factory.get_client_from_credentials(api_url, username, password, verbose=True)

# creating a client from the session
client = client_factory.get_client_from_session()

# removing the session file
client_factory.remove_session()
```

### Calling Endpoints

There are two methods for calling an endpoint that differ on how the it is specified.
- `send_request` accepts string names of the presenter and action.
- `send_request_by_callback` accepts a generated callback.

Request parameters are passed with the `path_params`, `query_params`, `body`, and `files` function parameters as name-value pairs.
Generated model instances can also be passed to the `body` parameter. 

```python
# DefaultApi can be used as an enumeration of all endpoint callbacks
from recodex_pylib.generated.swagger_client import DefaultApi
# generated models are imported one by one
from recodex_pylib.generated.swagger_client.models.id_organizational_body import IdOrganizationalBody

# specify endpoint with string identifiers
response = client.send_request("groups", "set_organizational", path_params={"id": "154b..."}, body={"value": True})

# specify endpoint with a callback
response = client.send_request_by_callback(
  DefaultApi.groups_presenter_action_set_organizational, 
  path_params={"id": "154b..."},
  # body can also be specified with a generated model class
  body=IdOrganizationalBody(value=True)
)
```

The methods return a `ClientResponse` object that contains the status, headers, and the actual data.
The data can be retrieved in multiple ways.

```python
# binary response data
binary_data = response.data_binary

# stringified response data
utf8_string = response.data

# data parsed into a dictionary
dictionary_data = response.get_parsed_data()
if dictionary_data is None:
  raise Exception("Data is not in JSON format.")

# formatted data (useful for printing in the CLI)
formatted_json_string = response.get_json_string()
formatted_yaml_string = response.get_json_string()
```

### Utility Functions

In case you want to manually create api tokens, the Client contains methods for this purpose. 

```python
new_token = client.get_login_token(username, password)
refresh_token = client.get_refresh_token()
```

To upload a file, you can use the `upload` utility function that automatically sends the file in chunks.

```python
from recodex_pylib.helpers.file_upload_helper import upload
file_id = upload(client, "file.txt", verbose=True)
```

# Development

## Commands

The `commands` folder contains four utility commands:
- `initRepo.sh` is used for initial setup of the repository after download; it is described in the installation section.
- `replaceGenerated.sh` generates code from a new OAS and replaces the old one. It also appends an update log to this README. Make sure to change the `recodexSwaggerDocsPath` variable to point to the path of the new OAS before you run the command.
- `runTestsLocally` installs the library in interactive mode and runs all tests in the `tests` folder.
- `uploadPackage.sh` packages the library and uploads it to PyPI. This action requires a PyPI token and rights to modify the package.

### Releasing New Versions

To release a new version of the package, you need to increment the version number in the `pyproject.toml` file (in the `[project]` section) and then run the `uploadPackage.sh` script.

In case the ReCodEx API changed, do not forget to run `replaceGenerated.sh` beforehand to update the generated API functions and the swagger file used for user input validation.

## Repository Structure

### Library Code

The `src/recodex-pylib` contains all code of the library.

The `client.py` contains the main `Client` class that links all parts together.
It uses the `SwaggerValidator` (`client_components/swagger_validator.py`) class to validate requests against their schema and the `EndpointResolver` (`client_components/endpoint_resolver.py`) to translate endpoint identifiers to the generated API functions.

It uses the generated `ApiClient` and `DefaultApi` classes to interface the generated part of the library, which is contained in the `generated` folder.
The folder is not part of the repository and needs to be manually generated.

The `aliases.yaml` file contains all aliases for endpoints. These aliases can be used instead of the default presenter and action identifiers.
The aliases are parsed and managed by the `AliasContainer` (`client_components/alias_container.py`) class.

### Repository Utilities

During code regeneration, the `src/swaggerDiffchecker.py` script is used to find differences between the old and new OAS and writes a summary to this README file.

### Testing

Testing relies on a mock ReCodEx API server implemented in flask that exposes a few endpoints, which are implemented in the `tests/mockEndpoints` folder.
The files are then linked to the server in the `tests/mock_server.py` script.

The actual tests are implemented in dedicated classes in the `tests/testClasses` folder.
They derive from the `test_class_base.py` which uses the full login process to connect to the mock server.

The tests are automatically run in GitHub CI/CD, where code is generated from the `tests/swagger.yaml` file.
This file should be updated regularly to make sure the tests reflect the latest state.


## Latest API Endpoint Changes

You can find a summary of the latest API changes [here](api-changes.md).
