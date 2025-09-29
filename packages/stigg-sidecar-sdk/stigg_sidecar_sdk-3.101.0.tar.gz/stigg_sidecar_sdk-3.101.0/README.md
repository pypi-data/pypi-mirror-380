# stigg-sidecar-sdk 

Stigg Python SDK makes it easier to interact with Stigg Sidecar

## Documentation

See https://docs.stigg.io/docs/sidecar-sdk

## Installation

```shell
    pip install stigg-sidecar-sdk
```

## Usage

Initialize the client:

```python

import os
from stigg_sidecar_sdk import Stigg, ApiConfig, LocalSidecarConfig, RedisOptions

api_key = os.environ.get("STIGG_SERVER_API_KEY")

stigg = Stigg(
    ApiConfig(
        api_key=api_key,
    ),
    # for development purposes, configure local sidecar (spawned as a subprocess): 
    local_sidecar_config=LocalSidecarConfig(
        redis=RedisOptions(
            environment_prefix="development",
            host="localhost",
            port=6379,
            db=0
        )
    ),
    # for production use, set remote sidecar host and port:
    remote_sidecar_host='localhost',
    remote_sidecar_port=80
)

```

Get single entitlement of a customer

```python

from stigg_sidecar_sdk import Stigg, ApiConfig, GetMeteredEntitlementRequest, MeteredEntitlementOptions


async def get_entitlement():
    stigg = Stigg(ApiConfig(api_key='api_key'))
    resp = await stigg.get_metered_entitlement(
        GetMeteredEntitlementRequest(customer_id='customer-demo-01',
                                     feature_id='feature-01-templates',
                                     options=MeteredEntitlementOptions(requested_usage=1))
    )
    print(resp.entitlement.has_access) 
```

Accessing the `api` client: 

```python

from stigg_sidecar_sdk import Stigg, ApiConfig
from stigg.generated import ProvisionCustomerInput

async def get_entitlement():
    stigg = Stigg(ApiConfig(api_key='api_key'))
    
    resp = await stigg.api.provision_customer(
        ProvisionCustomerInput(
            customer_id='customer-demo-01',
            name='customer-name'
        )
    )
    print("customer created", resp.provision_customer.customer.created_at)
```
