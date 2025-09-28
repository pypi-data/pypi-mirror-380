# Qwak Core

Qwak is an end-to-end production ML platform designed to allow data scientists to build, deploy, and monitor their models in production with minimal engineering friction.
Qwak Core contains all the objects and tools necessary to use the Qwak Platform

# Frog ML Storage

## Table of contents:

- [Overview](#overview)
- [Working with Artifactory](#Working-with-Artifactory)
   - [Login by adding authentication details to your python code](#Login-by-adding-authentication-details-to-your-python-code)
   - [Login via environment variables](#Login-via-environment-variables)
   - [Login via cli](#Login-via-cli)
     - [Login by a single command line with options](#Login-by-a-single-command-line-with-options)
     - [Login by interactive flow in Cli](#Login-by-interactive-flow-in-Cli)
- [Upload ML model to Artifactory](#Upload-ML-model-to-Artifactory)
- [Download ML model from Artifactory](#Download-ML-model-from-Artifactory)
- [Upload ML dataset to Artifactory](#Upload-ML-dataset-to-Artifactory)
- [Download ML dataset from Artifactory](#Download-ML-dataset-from-Artifactory)
- [Testing](#Testing)
  - [Locally run integration tests using local artifactory](#Locally-run-integration-tests-using-artifactory)
  - [Locally run tests using existing Artifactory](#Locally-run-tests-using-existing-Artifactory)
- [Packaging](#Packaging)
- [Linters](#Linters)

## Overview

JFrog ML Storage is a smart python client library providing a simple and efficient method of storing and downloading models, model data and datasets from the JFrog platform, utilizing the advanced capabilities of the JFrog platform.

## Working with Artifactory

FrogML Storage Library support is available from Artifactory version 7.84.x.

To be able to use FrogML Storage with Artifactory, you should authenticate the frogml storage client against Artifactory.
JFrog implements a credentials provider chain. It sequentially checks each place where you can set the credentials to authenticate with FrogML, and then selects the first one you set.

The credentials retrieval order is as follows:

1. [Login by adding authentication details to your python code](#Login-by-adding-authentication-details-to-your-python-code)
2. [Login via environment variables](#Login-via-environment-variables)
3. [Login via cli](#login-via-cli)


#### Login by adding authentication details to your python code

---
**NOTE**

It is strongly discouraged to use credentials in clear text. Use this method for testing purposes only.

---

You can authenticate the FrogML client directly via your Python code, using any of the following credentials (overriding env vars and the credentials in the configuration file):
- Username and Password
- Access Token

To log in as an anonymous user, log in first via CLI, and then you will be able to log in via Python using only your JFrog Platform domain.

Authentication by username and password:

```
from frogml_storage.frog_ml import FrogMLStorage
from frogml_storage.authentication.models._auth_config import AuthConfig

arti = FrogMLStorage(AuthConfig.by_basic_auth("http://myorg.jfrog.io", <username>, <password>))
```

Authentication by access token:

```
from frogml_storage.frog_ml import FrogMLStorage
from frogml_storage.authentication.models._auth_config import AuthConfig

arti = FrogMLStorage(AuthConfig.by_access_token("http://myorg.jfrog.io", <token>))
```

#### Login via environment variables

You can also authenticate the frogml client using the following environment variables:

- JF_URL - your JFrog platform domain, for example 'http://myorg.jfrog.io'
- JF_ACCESS_TOKEN - your artifactory token for this domain. To generate a token, log in to your artifactory, navigate to your FrogML repository and click on "Set Me Up".

After setting the environment variables, you can log in to the frogml client without specifying credentials.


```
from frogml_storage.frog_ml import FrogMLStorage
from frogml_storage.authentication.models._auth_config import AuthConfig

arti = FrogMLStorage()
```


### Login via cli

It is possible to authenticate the frogml client using any of the following methods:

1. Login by a single CLI command
2. Interactive flow

After each login attempt, the authentication result (success or failure) is printed on the screen.
If the login attempt succeeded, the authentication details will be saved as frogml configuration file under the path: ~/.frogml/config.json and from that point you can login again without specifying credentials.

In both interactive flow and the single command flow, it is possible to authenticate the frogml client by:

1. Username and password
2. Access token
3. Anonymous authentication



#### Login by a single command line with options

The below examples show the frogml login options using the cli:

Login using existing jfrog-cli of frogml configuration files (~/.jfrog/jfrog-cli.conf.v6 or ~/.frogml/config.json, respectively):

```
frogml login
```
If no configuration file is found, interactive mode will be triggered.

Login by username and password:

```
frogml login --url <artifactory_url> --username <username> --password <password>
```

Where: 
  - artifactory_url is your JFrog platform domain, for example 'http://myorg.jfrog.io'
  - username and password are your artifactory credentials for this domain

Login by access token:

```
frogml login --url <artifactory_url> --token <access_token> 
```

Where: 
  - artifactory_url is your JFrog platform domain, for example 'http://myorg.jfrog.io'
  - token - your artifactory token for this domain. To generate a token, log in to your artifactory and navigate to Administration -> User Management -> Access Tokens. 

Login by anonymous access:

```
frogml login --url <artifactory_url> --anonymous
```

#### Login by interactive flow in cli:

To start an interactive flow in the cli, run the command:

```
frogml login --interactive
```

After executing the command above, the cli prompts two options as follows:

```
frogml login --interactive
Please select from the following options:
1.Login by jfrog-cli configuration file: ~/.jfrog/jfrog-cli.conf.v6
2.Connecting to a new server
```

On choosing the first option, the cli attempts to retrieve your authentication credentials from your JFrog CLI configuration file and sends them to Artifactory.

On choosing the second option, the cli prompts you to input your JFrog platform domain URL. Afterwards, you can select the method you wish to use for authenticating the FrogML library.

```
Enter artifactory base url: http://myorg.jfrog.io
Choose your preferred authentication option:
0: Username and Password
1: Access Token
2: Anonymous Access
```


### Upload ML model to Artifactory

You can upload a model to a FrogML repository using the upload_model_version() function. 
You can upload a single file or an entire folder.
This function uses checksum upload, assigning a SHA2 value to each model for retrieval from storage. If the binary content cannot be reused, the smart upload mechanism performs regular upload instead.
After uploading the model, FrogML generates a file named model-info.json which contains the model name and its related files and dependencies.

The version parameter is optional. If not specified, Artifactory will set the version as the timestamp of the time you uploaded the model in your time zone, in UTC format:  yyyy-MM-dd-HH-mm-ss.
Additionally, you can add properties to the model in Artifactory to categorize and label it.
The function upload_model_version returns an instance of FrogMlModelVersion, which includes the model's name, version, and namespace.

The below examples show how to upload a model to Artifactory:

---
**NOTE**

namespace, version, properties, dependencies_files_paths and code_archive_file_path are optional.
model_path can point to a single file or a directory, in which case the whole directory is uploaded.
model_type can be written as JSON or as SerializationMetadata object imported from jfrog_ml.serialization_metadata.
All of SerializationMetadata fields must be populated.

---


Upload an entire folder as model:

```
from frogml_storage.frog_ml import FrogMLStorage

arti = FrogMLStorage()
arti.upload_model_version(repository=<repository_key>,
                          namespace=<namespce>,
                          model_name=<model_name>,
                          model_path="~/model_to_upload/",
                          model_type={"framework": "tensorflow", "framework_version": "2.3.0", "serialization_format": "H5", "runtime": "python", "runtime_version": "3.7"},
                          properties={"model_type": "keras", "experiment": "my-exp"},
                          dependencies_files_paths=["path/to/req/file1", "path/to/req/file2"],
                          code_archive_file_path="path/to/code/archieve/file"
                          )
```

Upload a model with a specified version, and no dependencies and code archive:

```
from frogml_storage.frog_ml import FrogMLStorage

arti = FrogMLStorage()
arti.upload_model_version(repository=<repository_key>,
                          namespace=<namespce>,
                          model_name=<model_name>,
                          version=<version>,
                          model_path="~/model_to_upload/",
                          model_type={"framework": "tensorflow", "framework_version": "2.3.0", "serialization_format": "H5", "runtime": "python", "runtime_version": "3.7"}
                          )
```

---

#### Download ML model from Artifactory

The below example shows how to download a model from Artifactory:

```
from frogml_storage.frog_ml import FrogMLStorage

arti = FrogMLStorage()

arti.download_model_version(repository=<repository_key>,
                            namespace=<namespace>,
                            model_name=<model_name>,
                            target_path="~/models",
                            version=<version>)
```

---
**NOTE**

The dependencies and code archive cannot be downloaded.

---

### Upload ML dataset to Artifactory

Upload an entire folder as dataset:


```
from frogml_storage.frog_ml import FrogMLStorage

arti = FrogMLStorage()
arti.upload_dataset_version(repository=<repository_key>,
                            namespace=<namespce>, 
                            dataset_name=<dataset_name>,
                            source_path="~/dataset_to_upload/",
                            properties={"dataset_type": "kerras", "experiment": "my-exp"})
```

Upload a dataset with specified version:

```
from frogml_storage.frog_ml import FrogMLStorage

arti = FrogMLStorage()
arti.upload_dataset_version(repository=<repository_key>, 
                            namespace=<namespce>, 
                            dataset_name=<dataset_name>, 
                            version=<version>,
                            source_path="~/dataset_to_upload/")
```

Upload a single file as a dataset:

```
from frogml_storage.frog_ml import FrogMLStorage

arti = FrogMLStorage()
arti.upload_dataset_version(repository=<repository_key>, 
                            namespace=<namespce>, 
                            dataset_name=<dataset_name>, 
                            version=<version>,
                            source_path="~/dataset_to_upload/config.json")
```

 #### Download ML dataset from Artifactory

The below example shows how to download a dataset from Artifactory:

```
from frogml_storage.frog_ml import FrogMLStorage

arti = FrogMLStorage()

arti.download_dataset_version(repository=<repository_key>, 
                              namespace=<namespace>, 
                              dataset_name=<dataset_name>,
                              target_path="~/datasets", 
                              version=<version>)
```

## Testing

### Locally run integration tests using artifactory

Prerequisites:
-  A user credentials (username, password)

To run the integration tests, use the ```poetry run pytest tests/integrations/test_artifactory_integration.py``` command. 
In addition, you will need to supply your 
ARTIFACTORY_URL in a `http(s)://` format (if not supplied, default will be as defined [here](tests/integrations/conftest.py)), ARTIFACTORY_USERNAME, ARTIFACTORY_PASSWORD. 
the test will create a local repository in RT, will upload and download model and datasets using the provided details,
and will delete the repository after the test.

example: 
```
    export ARTIFACTORY_URL=<artifactory_url>
    export ARTIFACTORY_USERNAME=<username>
    export ARTIFACTORY_PASSWORD=<password>
    
    poetry run pytest tests/integrations/test_artifactory_integration.py
 ```

### Locally run tests using existing Artifactory

To run the tests, use the ```pytest``` command pointing it to an existing Artifactory host. 
Prerequisites:
-  A generic local repository in the Artifactory instance
-  A user token or user credentials (username, password)

To run the test:

```
python3 -m  pytest tests/integrations/test_artifactory_integration.py  --rt_url "<artifactory_url>" --rt_access_token <token> --repo_name <generic-repo-name> -s
```

## Packaging

```
poetry build
```

## Linters
Fix spaces and linebreaks with:
```
make format
```
Run linter check:
```
make format
```