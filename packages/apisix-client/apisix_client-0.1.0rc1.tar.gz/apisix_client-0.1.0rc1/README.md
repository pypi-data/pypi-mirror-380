# Apisix Python Client
[![pypi](https://img.shields.io/pypi/v/apisix_client.svg)](https://pypi.python.org/pypi/apisix_client)
[![python](https://img.shields.io/pypi/pyversions/apisix_client.svg)](https://pypi.python.org/pypi/apisix_client)
[![license](https://img.shields.io/pypi/l/apisix_client.svg)](https://pypi.python.org/pypi/apisix_client)

The Apisix client Library provides convenient access to the Apisix admin API from applications written in Python.


# Documentation
Explore the Apisix admin API documentation [here](https://apisix.apache.org/docs/apisix/admin-api/).


# Installation

```sh
pip install --upgrade apisix_client
```

# Usage

```python
from apisix_client import ApisixClient

apisix_client = ApisixClient(base_url='YOUR_APISIX_URL', api_key="YOUR_API_KEY")
```