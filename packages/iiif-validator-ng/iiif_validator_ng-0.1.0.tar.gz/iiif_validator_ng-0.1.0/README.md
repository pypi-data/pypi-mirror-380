# IIIF Validator

This validator supports the same validations that are available on the
[IIIF website](http://iiif.io/).


## Installation
### Installation from pypi

The following should install the `iiif-validator` tool, the library, and the necessary dependencies::

```
pip install iiif-validator-ng
```

### Manual installation

Installation from the source code on GitHub can be done with:

```
uv install
```

This should install scripts, library, and the necessary dependencies.
Requires the [uv tool](https://docs.astral.sh/uv/).


## Command line validator, `iiif-validator`

After installation, for an image served at a IIIF Image API v2 server at
`http://localhost:8000/prefix/image_id` the validator can be run with::

```
iiif-validator --v2 --validation-id image_id http://localhost:8000/prefix
```

If the server is a V3 server, omit the `--v2` flag.


## License

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

See [LICENSE.txt](./LICENSE.txt)

Data included with this software, such as the test image file, may be freely
reused under [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
