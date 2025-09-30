# Introduction

Provide : 

- A base set of tools and classes to implement BioInfo algorithms
- Execution context, using the `ngs-run` script

# Installation

Add the CodeArtifact repository to your pyproject.toml
```
[[tool.poetry.source]]
name = "codeartifact"
url = "https://pdx-platform-224016688692.d.codeartifact.eu-west-1.amazonaws.com/pypi/pdx-python-libs/simple/"
secondary = true
```

Then authenticate your local environment to CodeArtifact 

```bash
export CODEARTIFACT_AUTH_TOKEN=$(aws codeartifact get-authorization-token --domain pdx-platform --query authorizationToken --output text --profile ADX_DEV)
poetry config http-basic.codeartifact aws $CODEARTIFACT_AUTH_TOKEN
```

**Note** : The token acquired with AWS is a temporary one. Each time you want to download new packages from the CodeArtifact repository, you may have to re-do the authentication process.

Then, simply add the library to your poetry dependencies.

```bash
poetry add ngs-pipeline-lib --source codeartifact
```

# Update

To update to a newer version of the library : 
```bash
poetry update ngs-pipeline-lib
```

> You may need to update your version constraint in the pyproject.toml file 

# Getting started

Once the library has been installed in your project, you can implement your algorithms by extending the `Algorithm` class.

If you want to add specific inputs to your Algorithm, extend `BaseInputs` (which is a Pydantic Model) and use it as the inputs Type.  
In order to adds outputs, extend BaseOutputs and set the `outputs_class` class attribute of your algorithm as this class.  
If you have specific inputs or outputs classes, you should also provide them to `Algorithm` when subclassing it. You place them between brackets as shown below, this will help your IDE undestand what kind of object it is dealing with, thus improving the autocompletion and the tooltips. 


```python
from pydantic import Field

from ngs_pipeline_lib.base.algorithm import Algorithm
from ngs_pipeline_lib.base.inputs import BaseInputs
from ngs_pipeline_lib.base.file import JsonFile
from ngs_pipeline_lib.base.outputs import BaseOutputs

class YourInputs(BaseInputs):
  your_input: str = Field(description="Description")


class YourOutputs(BaseOutputs):
  
  def __init__(self):
        super().__init__()
        self.my_own_output = JsonFile(name="my_json_file")

class YourAlgorithm(Algorithm[YourInputs, YourOutputs]):

    outputs_class = YourOutputs

    def execute_stub(self):
        ...

    def execute_implementation(self):
        print(self.inputs.your_input)
        ...

```

Then, you can call your Algorithm with the following command

`poetry run ngs-run --sample-id 1`

If you want to only create the stub output file, add the `--stub` parameter.


## Example
In `example/` you'll find the implementation of a dummy algorithm `DemoAlgorithm`.  
This algorithm takes 3 parameters:
- `value`: an integer 
- `kb`: a path to a knowledge base (a folder that contains `info.json` which references other local inputs and/or contains values), here it holds
  - `value`: an optional float (you can safely remove it from `info.json`)
  - `json_file`: a path to a json file
- `text_file`: a path to a text file  

The `example/data` folder contains some dummy data to run the algorithm.  
You can call it (from within `example/`) using : 
```sh
poetry run ngs-run --sample-id some_id --publish-dir /tmp --text-file data/some_text_file.txt --kb.path data/demo_kb
```
Note that for a `KnowledgeBase` the argument's name passed should be `--<name of the knowledge base>.path`.  
Add the `--stub` flag to run the stub instead of the implementation.

# Docker build & push

This library also includes two utilitary scripts to build & push Docker image : 

- ngs-build
- ngs-push

### Build

This script accepts the following arguments : 

| Short Arg | Long Arg   | Description             | Mandatory ? | Default value |
| --------- | ---------- | ----------------------- | ----------- | ------------- |
| -e        | --env-file | Path to env file to use | No          | `.env`        |

This script accepts the following environment variables as parameters 

| ENV VAR               | Description                                                  | Mandatory ? | Default value           |
| --------------------- | ------------------------------------------------------------ | ----------- | ----------------------- |
| PROCESS_NAME          | Name of the process                                          | Yes         | --                      |
| IMAGE_PREFIX          | Prefix used with the process name to create Docker repo name | No          | `ngs-pipeline-process-` |
| TAG                   | Tag of the image to create                                   | No          | `latest`                |
| DOCKERFILE            | Relative path to Dockerfile                                  | No          | `Dockerfile`            |
| PIP_REGISTRY_USERNAME | If needed, username to use for pip auth                      | No          | --                      |
| PIP_REGISTRY_PASSWORD | If needed, password to use for pip auth                      | No          | --                      |

> Note : the docker context used to build is `.`

### Push

This script accepts the following arguments : 

| Short Arg | Long Arg   | Description             | Mandatory ? | Default value |
| --------- | ---------- | ----------------------- | ----------- | ------------- |
| -e        | --env-file | Path to env file to use | No          | `.env`        |

This script accepts the following environment variables as parameters 

| ENV VAR               | Description                                 | Mandatory ? | Defaut value            |
| --------------------- | ------------------------------------------- | ----------- | ----------------------- |
| EXTERNAL_REGISTRY_URL | URL of Destination Registry                 | Yes         | --                      |
| PROCESS_NAME          | Name of the process to push                 | Yes         | --                      |
| IMAGE_PREFIX          | Prefix used in the process Docker repo name | No          | `ngs-pipeline-process-` |
| TAG                   | Tag of the image to create                  | No          | `latest`                |
| DOCKER_USERNAME       | If needed, username to use for docker auth  | No          | --                      |
| DOCKER_PASSWORD       | If needed, password to use for docker auth  | No          | --                      |

# Test tools

This library comes with two tools :
 - Integration test, to verify the behaviour of one process
 - E2E test, to verify the workflow of a complete pipeline with one/multiple samples

To run the integration test : 

"""bash
poetry run ngs-test integration 
"""

To run the E2E test : 

"""bash
poetry run ngs-test e2e --output-path <<YOUR_PIPELINE_OUTPUT_DIR>>  --scenario-file <<SCENARIO_PATH>>
"""

## End-To-End Test

This tool will do the following : 
- Load specified test scenario
  - Can be local or S3 path
- Load specified pipeline run :
  - Import the trace file
  - Import the hashed_id mapping file
  - Import the execution.json file
  - Explore all published files per sample & process
- Compare scenario and run
  - Check samples consistency (missing or extra)
  - Check task consistency for each sample (missing or extra, but also status)
  - Check published files for each task on each samples (missing or extra)

> Note : no validation is done on the file's content, only its presence. Please use integration tests for this purpose.

### Execution params
| Arg             | Description                                                     | Mandatory ? | Default value |
| --------------- | --------------------------------------------------------------- | ----------- | ------------- |
| --output-path   | The pipeline run to verify                                      | Yes         |               |
| --scenario-file | The scenario to use, containing expected samples, tasks & files | Yes         |               |


### Settings

All these settings are primarily loaded from the `.env` file. Ensure to have that file before running E2E tests.
They can be overridden by manually defining environment variables before launching `ngs-test integration`.

| Environment Variable    | Description                                                       | Mandatory ? | Default value          |
| ----------------------- | ----------------------------------------------------------------- | ----------- | ---------------------- |
| PROFILE                 | AWS Profile to use when connecting to S3 through boto3            | Yes         | ADX_DEV                |
| TEST_OUTPUT_FOLDER      | Local path where to store results and expected output of pipeline | No          | tests/e2e/outputs      |
| NEXTFLOW_TRACE_FILE     | Trace file path to look for in the output_folder                  | Yes         | trace.txt              |
| NEXTFLOW_HASHED_ID_FILE | sample_to_hashed_id file path to look for in the output_folder    | No          | sample_to_hash_map.tsv |
| NEXTFLOW_EXECUTION_FILE | Execution file path to look for in the output_folder              | No          | execution.json         |

## Integration Test

This tool must be used within a process project, containing a `.env` file with standard envvar (image_prefix, process_name etc...)
When used, this tool will do the following : 
- Load all scenarios
  - Search for scenario in a dedicated folder (by default : tests/integration/scenarios)
  - Can be filtered with the param `name_filter`
- For each scenario
  - Run the process image with the specified inputs
  - Extract output from container
  - Download expected output
  - Compare outputs

### Execution params
| Arg                            | Description                                                                                              | Mandatory ? | Default value |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- | ----------- | ------------- |
| --name-filter                  | Specify some filter on scenario name. Can be used multiple times (logical `AND` applied between filters) | No          |               |
| --post-clean / --no-post-clean | Flag to enable/disable cleaning of input and output files after test completion.                         | No          | True          |


### Settings

All these settings are primarly loaded from `.env` file. Ensure to have that file before running integration tests.
They can be overriden by defining manually environment variables before launching `ngs-test integration`.

| Environment Variable        | Description                                                                                | Mandatory ? | Default value               |
| --------------------------- | ------------------------------------------------------------------------------------------ | ----------- | --------------------------- |
| REMOTE_DOCKER_REPO          | Docker repository to use when launching process container                                  | Yes         |                             |
| IMAGE_PREFIX                | Combined with PROCESS_NAME to set the docker image to use when launching process container | Yes         |                             |
| PROCESS_NAME                | Combined with IMAGE_PREFIX to set the docker image to use when launching process container | Yes         |                             |
| TAG                         | Docker tag to use when launching process container                                         | Yes         |                             |
| PROFILE                     | AWS Profile to use when connecting to S3/ECR through boto3                                 | Yes         |                             |
| TEST_SCENARIOS_FOLDER       | Local path where to look for scenarios                                                     | No          | tests/integration/scenarios |
| TEST_OUTPUT_FOLDER          | Local path where to store results and expected output of process                           | No          | tests/integration/outputs   |
| TEST_LOCAL_INPUT_FOLDER     | Local path where to put input files (downloaded from S3)                                   | No          | tests/integration/inputs    |
| TEST_CONFIGURATION_FILENAME | Filename to look for when loading a scenario                                               | No          | test.json                   |

# Best Practices

When implementing your process, please refer to the [guidelines](./docs/GUIDELINES.md) documentation.

# License 

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

&copy; 2023-2025 bioMérieux - all right reserved
