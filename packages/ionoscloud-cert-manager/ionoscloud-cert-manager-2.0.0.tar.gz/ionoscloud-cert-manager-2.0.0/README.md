[![Gitter](https://img.shields.io/gitter/room/ionos-cloud/sdk-general)](https://gitter.im/ionos-cloud/sdk-general)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-cert-manager&metric=alert_status)](https://sonarcloud.io/summary?id=sdk-python-cert-manager)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-cert-manager&metric=bugs)](https://sonarcloud.io/summary/new_code?id=sdk-python-cert-manager)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-cert-manager&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-cert-manager)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-cert-manager&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-cert-manager)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-cert-manager&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-cert-manager)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-cert-manager&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=sdk-python-cert-manager)
[![Release](https://img.shields.io/github/v/release/ionos-cloud/sdk-python-cert-manager.svg)](https://github.com/ionos-cloud/sdk-python-cert-manager/releases/latest)
[![Release Date](https://img.shields.io/github/release-date/ionos-cloud/sdk-python-cert-manager.svg)](https://github.com/ionos-cloud/sdk-python-cert-manager/releases/latest)
[![PyPI version](https://img.shields.io/pypi/v/ionoscloud-cert-manager)](https://pypi.org/project/ionoscloud-cert-manager/)

![Alt text](.github/IONOS.CLOUD.BLU.svg?raw=true "Title")


# Python API client for ionoscloud_cert_manager

Using the Certificate Manager Service, you can conveniently provision and manage SSL certificates 
with IONOS services and your internal connected resources. 

For the [Application Load Balancer](https://api.ionos.com/docs/cloud/v6/#Application-Load-Balancers-get-datacenters-datacenterId-applicationloadbalancers),
you usually need a certificate to encrypt your HTTPS traffic.
The service provides the basic functions of uploading and deleting your certificates for this purpose.

## Overview
The IONOS Cloud SDK for Python provides you with access to the IONOS Cloud API. The client library supports both simple and complex requests. It is designed for developers who are building applications in Python. All API operations are performed over SSL and authenticated using your IONOS Cloud portal credentials. The API can be accessed within an instance running in IONOS Cloud or directly over the Internet from any application that can send an HTTPS request and receive an HTTPS response.


### Installation & Usage

**Requirements:**
- Python >= 3.5

### pip install

Since this package is hosted on [Pypi](https://pypi.org/) you can install it by using:

```bash
pip install ionoscloud-cert-manager
```

If the python package is hosted on a repository, you can install directly using:

```bash
pip install git+https://github.com/ionos-cloud/sdk-python-cert-manager.git
```

Note: you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python-cert-manager.git`

Then import the package:

```python
import ionoscloud_cert_manager
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```bash
python setup.py install --user
```

or `sudo python setup.py install` to install the package for all users

Then import the package:

```python
import ionoscloud_cert_manager
```

> **_NOTE:_**  The Python SDK does not support Python 2. It only supports Python >= 3.5.

### Authentication

All available server URLs are:

- *https://certificate-manager.de-fra.ionos.com* - Frankfurt

By default, *https://certificate-manager.de-fra.ionos.com* is used, however this can be overriden at authentication, either
by setting the `IONOS_API_URL` environment variable or by specifying the `host` parameter when
initializing the sdk client.

The username and password **or** the authentication token can be manually specified when initializing the SDK client:

```python
configuration = ionoscloud_cert_manager.Configuration(
                username='YOUR_USERNAME',
                password='YOUR_PASSWORD',
                token='YOUR_TOKEN',
                host='SERVER_API_URL'
                )
client = ionoscloud_cert_manager.ApiClient(configuration)
```

Environment variables can also be used. This is an example of how one would do that:

```python
import os

configuration = ionoscloud_cert_manager.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                token=os.environ.get('IONOS_TOKEN'),
                host=os.environ.get('IONOS_API_URL')
                )
client = ionoscloud_cert_manager.ApiClient(configuration)
```

**Warning**: Make sure to follow the Information Security Best Practices when using credentials within your code or storing them in a file.


### HTTP proxies

You can use http proxies by setting the following environment variables:
- `IONOS_HTTP_PROXY` - proxy URL
- `IONOS_HTTP_PROXY_HEADERS` - proxy headers

Each line in `IONOS_HTTP_PROXY_HEADERS` represents one header, where the header name and value is separated by a colon. Newline characters within a value need to be escaped. See this example:
```
Connection: Keep-Alive
User-Info: MyID
User-Group: my long\nheader value
```


### Changing the base URL

Base URL for the HTTP operation can be changed in the following way:

```python
import os

configuration = ionoscloud_cert_manager.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                host=os.environ.get('IONOS_API_URL'),
                server_index=None,
                )
client = ionoscloud_cert_manager.ApiClient(configuration)
```

## Certificate pinning:

You can enable certificate pinning if you want to bypass the normal certificate checking procedure,
by doing the following:

Set env variable IONOS_PINNED_CERT=<insert_sha256_public_fingerprint_here>

You can get the sha256 fingerprint most easily from the browser by inspecting the certificate.


## Documentation for API Endpoints

All URIs are relative to *https://certificate-manager.de-fra.ionos.com*
<details >
    <summary title="Click to toggle">API Endpoints table</summary>


| Class | Method | HTTP request | Description |
| ------------- | ------------- | ------------- | ------------- |
| AutoCertificateApi | [**auto_certificates_delete**](docs/api/AutoCertificateApi.md#auto_certificates_delete) | **DELETE** /auto-certificates/{autoCertificateId} | Delete AutoCertificate |
| AutoCertificateApi | [**auto_certificates_find_by_id**](docs/api/AutoCertificateApi.md#auto_certificates_find_by_id) | **GET** /auto-certificates/{autoCertificateId} | Retrieve AutoCertificate |
| AutoCertificateApi | [**auto_certificates_get**](docs/api/AutoCertificateApi.md#auto_certificates_get) | **GET** /auto-certificates | Retrieve all AutoCertificate |
| AutoCertificateApi | [**auto_certificates_patch**](docs/api/AutoCertificateApi.md#auto_certificates_patch) | **PATCH** /auto-certificates/{autoCertificateId} | Updates AutoCertificate |
| AutoCertificateApi | [**auto_certificates_post**](docs/api/AutoCertificateApi.md#auto_certificates_post) | **POST** /auto-certificates | Create AutoCertificate |
| CertificateApi | [**certificates_delete**](docs/api/CertificateApi.md#certificates_delete) | **DELETE** /certificates/{certificateId} | Delete Certificate |
| CertificateApi | [**certificates_find_by_id**](docs/api/CertificateApi.md#certificates_find_by_id) | **GET** /certificates/{certificateId} | Retrieve Certificate |
| CertificateApi | [**certificates_get**](docs/api/CertificateApi.md#certificates_get) | **GET** /certificates | Retrieve all Certificate |
| CertificateApi | [**certificates_patch**](docs/api/CertificateApi.md#certificates_patch) | **PATCH** /certificates/{certificateId} | Updates Certificate |
| CertificateApi | [**certificates_post**](docs/api/CertificateApi.md#certificates_post) | **POST** /certificates | Create Certificate |
| ProviderApi | [**providers_delete**](docs/api/ProviderApi.md#providers_delete) | **DELETE** /providers/{providerId} | Delete Provider |
| ProviderApi | [**providers_find_by_id**](docs/api/ProviderApi.md#providers_find_by_id) | **GET** /providers/{providerId} | Retrieve Provider |
| ProviderApi | [**providers_get**](docs/api/ProviderApi.md#providers_get) | **GET** /providers | Retrieve all Provider |
| ProviderApi | [**providers_patch**](docs/api/ProviderApi.md#providers_patch) | **PATCH** /providers/{providerId} | Updates Provider |
| ProviderApi | [**providers_post**](docs/api/ProviderApi.md#providers_post) | **POST** /providers | Create Provider |

</details>

## Documentation For Models

All URIs are relative to *https://certificate-manager.de-fra.ionos.com*
<details >
<summary title="Click to toggle">API models list</summary>

 - [AutoCertificate](docs/models/AutoCertificate)
 - [AutoCertificateCreate](docs/models/AutoCertificateCreate)
 - [AutoCertificatePatch](docs/models/AutoCertificatePatch)
 - [AutoCertificateRead](docs/models/AutoCertificateRead)
 - [AutoCertificateReadList](docs/models/AutoCertificateReadList)
 - [AutoCertificateReadListAllOf](docs/models/AutoCertificateReadListAllOf)
 - [Certificate](docs/models/Certificate)
 - [CertificateCreate](docs/models/CertificateCreate)
 - [CertificatePatch](docs/models/CertificatePatch)
 - [CertificateRead](docs/models/CertificateRead)
 - [CertificateReadList](docs/models/CertificateReadList)
 - [CertificateReadListAllOf](docs/models/CertificateReadListAllOf)
 - [Connection](docs/models/Connection)
 - [DayOfTheWeek](docs/models/DayOfTheWeek)
 - [Error](docs/models/Error)
 - [ErrorMessages](docs/models/ErrorMessages)
 - [Links](docs/models/Links)
 - [MaintenanceWindow](docs/models/MaintenanceWindow)
 - [Metadata](docs/models/Metadata)
 - [MetadataWithAutoCertificateInformation](docs/models/MetadataWithAutoCertificateInformation)
 - [MetadataWithAutoCertificateInformationAllOf](docs/models/MetadataWithAutoCertificateInformationAllOf)
 - [MetadataWithCertificateInformation](docs/models/MetadataWithCertificateInformation)
 - [MetadataWithCertificateInformationAllOf](docs/models/MetadataWithCertificateInformationAllOf)
 - [MetadataWithStatus](docs/models/MetadataWithStatus)
 - [MetadataWithStatusAllOf](docs/models/MetadataWithStatusAllOf)
 - [Pagination](docs/models/Pagination)
 - [PatchName](docs/models/PatchName)
 - [Provider](docs/models/Provider)
 - [ProviderCreate](docs/models/ProviderCreate)
 - [ProviderExternalAccountBinding](docs/models/ProviderExternalAccountBinding)
 - [ProviderPatch](docs/models/ProviderPatch)
 - [ProviderRead](docs/models/ProviderRead)
 - [ProviderReadList](docs/models/ProviderReadList)
 - [ProviderReadListAllOf](docs/models/ProviderReadListAllOf)


[[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

</details>
