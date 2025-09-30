# bolt-api-sdk

Developer-friendly & type-safe Python SDK specifically catered to leverage *bolt-api-sdk* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=bolt-api-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/bolt/boltpublicapi). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Bolt API Reference: Postman Collection:

[![](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/9136127-55d2bde1-a248-473f-95b5-64cfd02fb445?action=collection%2Ffork&collection-url=entityId%3D9136127-55d2bde1-a248-473f-95b5-64cfd02fb445%26entityType%3Dcollection%26workspaceId%3D78beee89-4238-4c5f-bd1f-7e98978744b4#?env%5BBolt%20Sandbox%20Environment%5D=W3sia2V5IjoiYXBpX2Jhc2VfdXJsIiwidmFsdWUiOiJodHRwczovL2FwaS1zYW5kYm94LmJvbHQuY29tIiwidHlwZSI6ImRlZmF1bHQiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6InRrX2Jhc2UiLCJ2YWx1ZSI6Imh0dHBzOi8vc2FuZGJveC5ib2x0dGsuY29tIiwidHlwZSI6ImRlZmF1bHQiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6ImFwaV9rZXkiLCJ2YWx1ZSI6IjxyZXBsYWNlIHdpdGggeW91ciBCb2x0IFNhbmRib3ggQVBJIGtleT4iLCJ0eXBlIjoic2VjcmV0IiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJwdWJsaXNoYWJsZV9rZXkiLCJ2YWx1ZSI6IjxyZXBsYWNlIHdpdGggeW91ciBCb2x0IFNhbmRib3ggcHVibGlzaGFibGUga2V5PiIsInR5cGUiOiJkZWZhdWx0IiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJkaXZpc2lvbl9pZCIsInZhbHVlIjoiPHJlcGxhY2Ugd2l0aCB5b3VyIEJvbHQgU2FuZGJveCBwdWJsaWMgZGl2aXNpb24gSUQ+IiwidHlwZSI6ImRlZmF1bHQiLCJlbmFibGVkIjp0cnVlfV0=)

## About
 A comprehensive Bolt API reference for interacting with Transactions, Orders, Product Catalog, Configuration, Testing, and much more.

 Note: You must also reference the [Merchant Callback API](/api-merchant) when building a managed checkout custom cart integration
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [bolt-api-sdk](#bolt-api-sdk)
  * [About](#about)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add git+<UNSET>.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from bolt-api-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "bolt-api-sdk",
# ]
# ///

from bolt_api_sdk import Bolt

sdk = Bolt(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from bolt_api_sdk import Bolt, models
import os


with Bolt() as bolt:

    res = bolt.account.get_account(security=models.GetAccountSecurity(
        o_auth=os.getenv("BOLT_O_AUTH", ""),
        x_api_key=os.getenv("BOLT_X_API_KEY", ""),
    ))

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from bolt_api_sdk import Bolt, models
import os

async def main():

    async with Bolt() as bolt:

        res = await bolt.account.get_account_async(security=models.GetAccountSecurity(
            o_auth=os.getenv("BOLT_O_AUTH", ""),
            x_api_key=os.getenv("BOLT_X_API_KEY", ""),
        ))

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name        | Type   | Scheme       | Environment Variable |
| ----------- | ------ | ------------ | -------------------- |
| `x_api_key` | apiKey | API key      | `BOLT_X_API_KEY`     |
| `o_auth`    | oauth2 | OAuth2 token | `BOLT_O_AUTH`        |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from bolt_api_sdk import Bolt, models
import os


with Bolt(
    security=models.Security(
        x_api_key=os.getenv("BOLT_X_API_KEY", ""),
    ),
) as bolt:

    res = bolt.account.create_account(create_account_input={
        "addresses": [
            {
                "company": "Bolt",
                "country": "United States",
                "country_code": "US",
                "door_code": "123456",
                "email": "alan.watts@example.com",
                "first_name": "Alan",
                "last_name": "Watts",
                "locality": "Brooklyn",
                "name": "Alan Watts",
                "phone": "+12125550199",
                "postal_code": "10044",
                "region": "NY",
                "region_code": "NY",
                "street_address1": "888 main street",
                "street_address2": "apt 3021",
                "street_address3": "c/o Alicia Watts",
                "street_address4": "Bridge Street Apartment Building B",
                "metadata": {},
            },
        ],
        "payment_methods": [
            {
                "billing_address": {
                    "company": "Bolt",
                    "country": "United States",
                    "country_code": "US",
                    "default": True,
                    "door_code": "123456",
                    "email": "alan.watts@example.com",
                    "first_name": "Alan",
                    "last_name": "Watts",
                    "locality": "Brooklyn",
                    "name": "Alan Watts",
                    "phone": "+12125550199",
                    "postal_code": "10044",
                    "region": "NY",
                    "region_code": "NY",
                    "street_address1": "888 main street",
                    "street_address2": "apt 3021",
                    "street_address3": "c/o Alicia Watts",
                    "street_address4": "Bridge Street Apartment Building B",
                },
                "billing_address_id": None,
                "bin": "411111",
                "expiration": "2025-11",
                "last4": "1234",
                "metadata": {},
                "postal_code": "10044",
                "token": "a1B2c3D4e5F6G7H8i9J0k1L2m3N4o5P6Q7r8S9t0",
                "token_type": models.PaymentMethodAccountTokenType.BOLT,
            },
        ],
        "profile": {
            "email": "alan.watts@example.com",
            "first_name": "Alan",
            "last_name": "Watts",
            "metadata": {},
            "phone": "+12125550199",
        },
    })

    # Handle response
    print(res)

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
from bolt_api_sdk import Bolt, models
import os


with Bolt() as bolt:

    res = bolt.account.get_account(security=models.GetAccountSecurity(
        o_auth=os.getenv("BOLT_O_AUTH", ""),
        x_api_key=os.getenv("BOLT_X_API_KEY", ""),
    ))

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [account](docs/sdks/account/README.md)

* [get_account](docs/sdks/account/README.md#get_account) - Get Account Details
* [create_account](docs/sdks/account/README.md#create_account) - Create Bolt Account
* [update_account_profile](docs/sdks/account/README.md#update_account_profile) - Update Profile
* [add_address](docs/sdks/account/README.md#add_address) - Add Address
* [delete_address](docs/sdks/account/README.md#delete_address) - Delete Address
* [replace_address](docs/sdks/account/README.md#replace_address) - Replace Address
* [edit_address](docs/sdks/account/README.md#edit_address) - Edit Address
* [detect_account](docs/sdks/account/README.md#detect_account) - Detect Account
* [add_payment_method](docs/sdks/account/README.md#add_payment_method) - Add Payment Method
* [delete_payment_method](docs/sdks/account/README.md#delete_payment_method) - Delete Payment Method


### [configuration](docs/sdks/configuration/README.md)

* [get_merchant_callbacks](docs/sdks/configuration/README.md#get_merchant_callbacks) - Get Callback URLs
* [set_merchant_callbacks](docs/sdks/configuration/README.md#set_merchant_callbacks) - Set Callback URLs
* [get_merchant_identifiers](docs/sdks/configuration/README.md#get_merchant_identifiers) - Get Merchant Identifiers

### [o_auth](docs/sdks/oauth/README.md)

* [o_auth_token](docs/sdks/oauth/README.md#o_auth_token) - OAuth Token Endpoint

### [orders](docs/sdks/orders/README.md)

* [create_order_token](docs/sdks/orders/README.md#create_order_token) - Create Order Token
* [track_order](docs/sdks/orders/README.md#track_order) - Send order tracking details

### [statements](docs/sdks/statements/README.md)

* [get_statements](docs/sdks/statements/README.md#get_statements) - Fetch a Statement

### [testing](docs/sdks/testing/README.md)

* [test_shipping](docs/sdks/testing/README.md#test_shipping) - Test Shipping
* [create_testing_shopper_account](docs/sdks/testing/README.md#create_testing_shopper_account) - Create Testing Shopper Account
* [get_test_credit_card_token](docs/sdks/testing/README.md#get_test_credit_card_token) - Fetch a Test Credit Card Token

### [transactions](docs/sdks/transactions/README.md)

* [authorize_transaction](docs/sdks/transactions/README.md#authorize_transaction) - Authorize a Card
* [capture_transaction](docs/sdks/transactions/README.md#capture_transaction) - Capture a Transaction
* [refund_transaction](docs/sdks/transactions/README.md#refund_transaction) - Refund a Transaction
* [review_transaction](docs/sdks/transactions/README.md#review_transaction) - Review Transaction
* [void_transaction](docs/sdks/transactions/README.md#void_transaction) - Void a Transaction
* [get_transaction_details](docs/sdks/transactions/README.md#get_transaction_details) - Transaction Details
* [update_transaction](docs/sdks/transactions/README.md#update_transaction) - Update a Transaction

### [webhooks](docs/sdks/webhooks/README.md)

* [query_webhooks](docs/sdks/webhooks/README.md#query_webhooks) - Query Webhooks
* [create_webhook](docs/sdks/webhooks/README.md#create_webhook) - Create Bolt Webhook
* [delete_webhook](docs/sdks/webhooks/README.md#delete_webhook) - Delete a Bolt Webhook
* [get_webhook](docs/sdks/webhooks/README.md#get_webhook) - Get Webhook

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from bolt_api_sdk import Bolt, models
from bolt_api_sdk.utils import BackoffStrategy, RetryConfig
import os


with Bolt() as bolt:

    res = bolt.account.get_account(security=models.GetAccountSecurity(
        o_auth=os.getenv("BOLT_O_AUTH", ""),
        x_api_key=os.getenv("BOLT_X_API_KEY", ""),
    ),
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from bolt_api_sdk import Bolt, models
from bolt_api_sdk.utils import BackoffStrategy, RetryConfig
import os


with Bolt(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as bolt:

    res = bolt.account.get_account(security=models.GetAccountSecurity(
        o_auth=os.getenv("BOLT_O_AUTH", ""),
        x_api_key=os.getenv("BOLT_X_API_KEY", ""),
    ))

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`BoltError`](./src/bolt_api_sdk/errors/bolterror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from bolt_api_sdk import Bolt, errors


with Bolt() as bolt:
    res = None
    try:

        res = bolt.account.detect_account(x_publishable_key="<value>")

        # Handle response
        print(res)


    except errors.BoltError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.ErrorsBoltAPIResponse):
            print(e.data.errors)  # Optional[List[models.ErrorBoltAPI]]
            print(e.data.result)  # Optional[models.RequestResult]
```

### Error Classes
**Primary error:**
* [`BoltError`](./src/bolt_api_sdk/errors/bolterror.py): The base class for HTTP error responses.

<details><summary>Less common errors (8)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`BoltError`](./src/bolt_api_sdk/errors/bolterror.py)**:
* [`ErrorsBoltAPIResponse`](./src/bolt_api_sdk/errors/errorsboltapiresponse.py): Applicable to 19 of 31 methods.*
* [`ErrorsOauthServerResponse`](./src/bolt_api_sdk/errors/errorsoauthserverresponse.py): Invalid request to OAuth Token. Applicable to 1 of 31 methods.*
* [`UnprocessableEntityError`](./src/bolt_api_sdk/errors/unprocessableentityerror.py): Unprocessable Entity. Status code `422`. Applicable to 1 of 31 methods.*
* [`ResponseValidationError`](./src/bolt_api_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                         | Description                     |
| --- | ------------------------------ | ------------------------------- |
| 0   | `https://api.bolt.com`         | The Production URL (Live Data). |
| 1   | `https://api-sandbox.bolt.com` | The Sandbox URL (Test Data).    |
| 2   | `https://api-staging.bolt.com` | The Staging URL (Staged Data).  |

#### Example

```python
from bolt_api_sdk import Bolt, models
import os


with Bolt(
    server_idx=2,
) as bolt:

    res = bolt.account.get_account(security=models.GetAccountSecurity(
        o_auth=os.getenv("BOLT_O_AUTH", ""),
        x_api_key=os.getenv("BOLT_X_API_KEY", ""),
    ))

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from bolt_api_sdk import Bolt, models
import os


with Bolt(
    server_url="https://api-staging.bolt.com",
) as bolt:

    res = bolt.account.get_account(security=models.GetAccountSecurity(
        o_auth=os.getenv("BOLT_O_AUTH", ""),
        x_api_key=os.getenv("BOLT_X_API_KEY", ""),
    ))

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from bolt_api_sdk import Bolt
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Bolt(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from bolt_api_sdk import Bolt
from bolt_api_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Bolt(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Bolt` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from bolt_api_sdk import Bolt
def main():

    with Bolt() as bolt:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Bolt() as bolt:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from bolt_api_sdk import Bolt
import logging

logging.basicConfig(level=logging.DEBUG)
s = Bolt(debug_logger=logging.getLogger("bolt_api_sdk"))
```

You can also enable a default debug logger by setting an environment variable `BOLT_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=bolt-api-sdk&utm_campaign=python)
