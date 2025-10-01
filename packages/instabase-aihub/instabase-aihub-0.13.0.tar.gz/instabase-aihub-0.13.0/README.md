# Instabase AI Hub Python Library

The AI Hub Python library provides convenient access to the AI Hub REST API from any Python 3.7+ application. The library includes type definitions for all request params and response fields.

The SDK is automatically from an OpenAPI specification using the [OpenAPI Generator](https://openapi-generator.tech).

## Documentation

The REST API documentation is available at [AI Hub docs](https://docs.instabase.com).

## Installation

```sh
# install from PyPI
pip install instabase-aihub
```

### Usage

Here is a simple example that creates a batch by uploading a single file and runs an app to summarize it.

```py
from aihub import AIHub
import os
import time

# Initializes the client. Set the API token.
client = AIHub(api_key="<API-TOKEN>")

# Creates a batch and adds files.
batch = client.batches.create(name='<BATCH-NAME>')
file_paths = ['<inner/folder/sample1.pdf>', '<.../sample2.docx>', '<.../sample3.png>']
for file_path in file_paths:
    with open(file_path, "rb") as file:
        client.batches.add_file(id=batch.id, file_name=os.path.basename(file_path), file=file)

# Runs an app and gets the results when the app run is complete.
run = client.apps.runs.create(app_name='<APP-NAME>', owner=None, batch_id=batch.id)

# Continuously checks the run status until it's done.
while True:
    status = client.apps.runs.status(run.id)
    if status.status == 'COMPLETE':
        break
    time.sleep(5)  # Polling interval

results = client.apps.runs.results(run.id)
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/instabase/aihub-sdk/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.
