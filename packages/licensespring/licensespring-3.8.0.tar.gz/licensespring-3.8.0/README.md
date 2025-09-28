# LicenseSpring Python Library

The LicenseSpring Python Library provides convenient access to the LicenseSpring API from
applications written in the Python language.

## Installation

Install `licensespring` library:

```
pip install licensespring
```

Requires: Python >=3.9

## Hardware (Device) IDs

This library provides preconfigured hardware identity providers:
- `HardwareIdProvider` (default)
- `PlatformIdProvider`
- `HardwareIdProviderSource` (recommended)

You can set the desired hardware identity provider when initializing the APIClient:
```python
from licensespring.hardware import PlatformIdProvider

api_client = APIClient(api_key="_your_api_key_", shared_key="_your_shared_key_", hardware_id_provider=PlatformIdProvider)
```

It also supports their customization and creation of your own hardware id provider.

### HardwareIdProvider

Uses [uuid.getnode()](https://docs.python.org/3/library/uuid.html#uuid.getnode) to generate unique ID per device as described:

> Get the hardware address as a 48-bit positive integer. The first time this runs, it may launch a separate program, which could be quite slow. If all attempts to obtain the hardware address fail, we choose a random 48-bit number with the multicast bit (least significant bit of the first octet) set to 1 as recommended in RFC 4122. “Hardware address” means the MAC address of a network interface. On a machine with multiple network interfaces, universally administered MAC addresses (i.e. where the second least significant bit of the first octet is unset) will be preferred over locally administered MAC addresses, but with no other ordering guarantees.

All of the methods exposed by `HardwareIdProvider`:
```python
class HardwareIdProvider:
    def get_id(self):
        return str(uuid.getnode())

    def get_os_ver(self):
        return platform.platform()

    def get_hostname(self):
        return platform.node()

    def get_ip(self):
        return socket.gethostbyname(self.get_hostname())

    def get_is_vm(self):
        return False

    def get_vm_info(self):
        return None

    def get_mac_address(self):
        return ":".join(("%012X" % uuid.getnode())[i : i + 2] for i in range(0, 12, 2))

    def get_request_id(self):
        return str(uuid.uuid4())
```
### HardwareIdProviderSource
Utilizes a proprietary in-house algorithm for our SDKs **(recommended algorithm)** [Hardware ID Algorithm](https://pypi.org/project/licensespring-hardware-id-generator/).
```python  

class HardwareIdProviderSource(HardwareIdProvider):
    def get_id(self):   
        hardware_id = get_hardware_id(HardwareIdAlgorithm.Default)
        
        if logging.getLogger().hasHandlers():
            logs = get_logs()
            version = get_version()
            logging.info("Version: ",version)
            logging.info("Hardware ID:",hardware_id)
            for log_line in logs:
                logging.info(log_line)
    
        return hardware_id
```
### PlatformIdProvider

Uses [sys.platform](https://docs.python.org/3/library/sys.html#sys.platform) and OS queries to find the raw GUID of the device.

Extends the `HardwareIdProvider` and overwrites only the `get_id` method:
```python
class PlatformIdProvider(HardwareIdProvider):
    def get_id(self):
        id = None

        if sys.platform == 'darwin':
            id = execute("ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'")

        if sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'msys':
            id = read_win_registry('HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography', 'MachineGuid')
            if not id:
                id = execute('wmic csproduct get uuid').split('\n')[2].strip()

        if sys.platform.startswith('linux'):
            id = read_file('/var/lib/dbus/machine-id')
            if not id:
                id = read_file('/etc/machine-id')

        if sys.platform.startswith('openbsd') or sys.platform.startswith('freebsd'):
            id = read_file('/etc/hostid')
            if not id:
                id = execute('kenv -q smbios.system.uuid')

        if not id:
            id = super().get_id()

        return id
```

### Customization

Extend any of the preconfigured hardware identity providers, overwrite the methods you want and provide it when initializing the APIClient:
```python
class CustomHardwareIdProvider(HardwareIdProvider):
    def get_id(self):
        return "_my_id_"

api_client = APIClient(api_key="_your_api_key_", shared_key="_your_shared_key_", hardware_id_provider=CustomHardwareIdProvider)
```

## APIClient Usage Examples

### Set app version
```python
import licensespring

licensespring.app_version = "MyApp 1.0.0"
```

### Create APIClient
An API client can use either **API keys** (`shared_key` and `api_key`) or **OAuth** (`client_id` and `client_secret`) for authorization.

#### API keys
```python
from licensespring.api import APIClient

api_client = APIClient(api_key="_your_api_key_", shared_key="_your_shared_key_")
```
#### OAuth
```python
from licensespring.api import APIClient

api_client = APIClient(client_id="_your_client_id_", client_secret="_your_client_secret_")
```

### Activate key based license
```python
product = "lkprod1"
license_key = "GPB7-279T-6MNK-CQLK"
license_data = api_client.activate_license(product=product, license_key=license_key)

print(license_data)
```

### Activate user based license
```python
product = "uprod1"
username = "user1@email.com"
password = "nq64k1!@"

license_data = api_client.activate_license(
    product=product, username=username, password=password
)

print(license_data)
```

### Activate key based bundle
```python
product = "lkprod1"
license_key = "GPB7-279T-6MNK-CQLK"
license_data = api_client.activate_bundle(product=product, license_key=license_key)

print(license_data)
```

### Activate user based bundle
```python
product = "uprod1"
username = "user1@email.com"
password = "nq64k1!@"

license_data = api_client.activate_bundle(
    product=product, username=username, password=password
)

print(license_data)
```

### Deactivate key based bundle
```python
product = "lkprod1"
license_key = "GPB7-279T-6MNK-CQLK""
license_data = api_client.activate_bundle(product=product, license_key=license_key)

print(license_data)
```

### Deactivate user based bundle
```python
product = "uprod1"
username = "user1@email.com"
password = "nq64k1!@"
license_data = api_client.deactivate_bundle(product=product, username=username, password=password)

print(license_data)
```

### Check key based bundle
```python
product = "lkprod1"
license_key = "GPB7-279T-6MNK-CQLK""
license_data = api_client.check_bundle(product=product, license_key=license_key)

print(license_data)
```

### Check user based bundle
```python
product = "uprod1"
username = "user1@email.com"
password = "nq64k1!@"
license_data = api_client.check_bundle(product=product, username=username, password=password)

print(license_data)
```

### Deactivate key based license
```python
product = "lkprod1"
license_key = "GPUB-J4PH-CGNK-C7LK"
api_client.deactivate_license(product=product, license_key=license_key)
```

### Deactivate user based license
```python
product = "uprod1"
username = "user1@email.com"

api_client.deactivate_license(
    product=product, username=username
)
```

### Check key based license
```python
product = "lkprod1"
license_key = "GPBQ-DZCP-E9SK-CQLK"

license_data = api_client.check_license(product=product, license_key=license_key)

print(license_data)
```

### Check user based license
```python
product = "uprod1"
username = "user2@email.com"
password = "1l48y#!b"

license_data = api_client.check_license(product=product, username=username)

print(license_data)
```

### Add consumption
```python
product = "lkprod1"
license_key = "GPSU-QTKQ-HSSK-C9LK"

# Add 1 consumption
consumption_data = api_client.add_consumption(
    product=product, license_key=license_key
)

print(consumption_data)

# Add 3 consumptions
consumption_data = api_client.add_consumption(
    product=product, license_key=license_key, consumptions=3
)

print(consumption_data)

# Add 1 consumption, allow overages and define max overages
consumption_data = api_client.add_consumption(
    product=product, license_key=license_key, allow_overages=True, max_overages=10
)

print(consumption_data)
```

### Add feature consumption
```python
product = "lkprod1"
license_key = "GPTJ-LSYZ-USEK-C8LK"
feature = "lkprod1cf1"

# Add 1 consumption
feature_consumption_data = api_client.add_feature_consumption(
    product=product, license_key=license_key, feature=feature
)

# Add 3 consumptions
feature_consumption_data = api_client.add_feature_consumption(
    product=product, license_key=license_key, feature=feature, consumptions=3
)

print(feature_consumption_data)
```

### Trial key
```python
product = "lkprod2"

trial_license_data = api_client.trial_key(product=product)

print(trial_license_data)
```

### Product details
```python
product = "lkprod1"

product_data = api_client.product_details(product=product)

print(product_data)
```

### Track device variables
```python
product = "lkprod1"
license_key = "GPUB-SZF9-AB2K-C7LK"
variables = {"variable_1_key": "variable_1_value", "variable_2_key": "variable_2_value"}

device_variables = api_client.track_device_variables(product=product, license_key=license_key, variables=variables)

print(device_variables)
```

### Get device variables
```python
product = "lkprod1"
license_key = "GPUB-SZF9-AB2K-C7LK"

device_variables = api_client.get_device_variables(product=product, license_key=license_key)

print(device_variables)
```

### Floating borrow
```python
product = "lkprod1"
license_key = "GPUC-NGWU-3NJK-C7LK"

# Borrow for 2 hours
borrowed_until = (datetime.utcnow() + timedelta(hours=2)).isoformat()
floating_borrow_data = api_client.floating_borrow(product=product, license_key=license_key, borrowed_until=borrowed_until)

print(floating_borrow_data)
```

### Floating release
```python
product = "lkprod1"
license_key = "GPUC-NGWU-3NJK-C7LK"

api_client.floating_release(product=product, license_key=license_key)
```

### Change password
```python
username = "user4@email.com"
password = "_old_password_"
new_password = "_new_password_"

is_password_changed = api_client.change_password(username=username, password=password, new_password=new_password)

print(is_password_changed)
```

### Versions
```python
product = "lkprod1"
license_key = "GPB7-279T-6MNK-CQLK"

# Get versions for all environments
versions_data = api_client.versions(product=product, license_key=license_key)

# Get versions for mac environment
mac_versions_data = api_client.versions(
    product=product, license_key=license_key, env="mac"
)

print(versions_data)
```

### Installation file
```python
product = "lkprod1"
license_key = "GPB7-279T-6MNK-CQLK"

# Get the latest installation file
installation_file_data = api_client.installation_file(
    product=product, license_key=license_key
)

# Get the latest installation file for linux environment
installation_file_data = api_client.installation_file(
    product=product, license_key=license_key, env="linux"
)

# Get the latest installation file for version 1.0.0
installation_file_data = api_client.installation_file(
    product=product, license_key=license_key, version="1.0.0"
)

print(installation_file_data)
```

### Customer license users
```python
product = "uprod1"
customer = 'c1@c.com'

customer_license_users_data = api_client.customer_license_users(
    product=product, customer=customer
)

print(customer_license_users_data)
```

### SSO URL
```python
product = "uprod1"
customer_account_code = "ccorp"

sso_url_data = api_client.sso_url(
    product=product, customer_account_code=customer_account_code
)

print(sso_url_data)
```


### SSO URL with `code` response type
```python
product = "uprod1"
customer_account_code = "ccorp"

sso_url_data = api_client.sso_url(
    product=product,
    customer_account_code=customer_account_code,
    response_type="code",
)

print(sso_url_data)
```

### Activate offline
```python
product = "lkprod1"
license_key = "GPY7-VHX9-MDSK-C3LK"

# Generate data for offline activation
activate_offline_data = api_client.activate_offline_dump(
    product=product, license_key=license_key
)

# Write to file
with open('activate_offline.req', mode='w') as f:
    print(activate_offline_data, file=f)

# Activate offline
license_data = api_client.activate_offline(data=activate_offline_data)

print(license_data)
```

### Activate offline load
```python
# Read from file
with open('./ls_activation.lic') as file:
    ls_activation_data = file.read()

license_data = api_client.activate_offline_load(ls_activation_data)

print(license_data)
```

### Check offline load
```python
# Read from file
with open('./license_refresh.lic') as file:
    license_refresh_data = file.read()

license_data = api_client.check_offline_load(license_refresh_data)

print(license_data)
```


### Deactivate offline
```python
product = "lkprod1"
license_key = "GPYC-X5J2-L5SK-C3LK"

# Generate data for offline deactivation
deactivate_offline_data = api_client.deactivate_offline_dump(
    product=product, license_key=license_key
)

# Write to file
with open('deactivate_offline.req', mode='w') as f:
    print(deactivate_offline_data, file=f)

# Deactivate offline
api_client.deactivate_offline(data=deactivate_offline_data)
```

### Key based license feature check
```python
product = "lkprod1"
license_key = "GPB7-279T-6MNK-CQLK"
feature = "lkprod1f1"

license_feature_data = api_client.check_license_feature(
    product=product, feature=feature, license_key=license_key
)

print(license_feature_data)
```

### Key based license floating feature release
```python
product = "lkprod1"
license_key = "GPB7-279T-6MNK-CQLK"
feature = "lkprod1f1"

api_client.floating_feature_release(
    product=product, feature=feature, license_key=license_key
)
```
### User licenses
```python
product = "userpr1"
username = "user123"
password = "password"

response = api_client.user_licenses(
    product=product,username=username,
    password=password)

print(response)
```

## Licensefile

### Licensefile setup  
To use licensefile inside a python SDK you should first setup your key and IV. Key and IV are used inside Python SDK for encryption and decryption process inside licensefile. For the first setup it is essenital to chose **password** and **salt** for key generation. This process is only required **once** at the setup.  
```python
from licensespring.licensefile.default_crypto import DefaultCryptoProvider

password = "YOUR_PASSWORD"
salt = "YOUR_SALT"


crypto = DefaultCryptoProvider()

key = crypto.derive_key(password=key_password,salt=key_salt)
iv = crypto.generate_random_iv()
```
### Configuration Setup
After you have successfully setup your key and IV you should setup your Configuration.
```python
from licensespring.licensefile.config import Configuration

conf = Configuration(product="your_product_short_code",
        api_key="your_api_key",
        shared_key="your_shared_key",
        file_key="your_key",
        file_iv="your_iv",
        hardware_id_provider=HardwareIdProvider,
        verify_license_signature=True,
        signature_verifier=SignatureVerifier,
        api_domain="api.licensespring.com",
        api_version="v4",
        filename="License",
        file_path=None,
        grace_period_conf=24,
        air_gap_public_key="your_air_gap_public_key",
        client_id="your_client_id",
        client_secret="your_client_secret",
        certificate_chain_path="path_to_certificate/chain.pem")
```

* **product (str)**: product short code.    
* **api_key (str,optional)**: Your unique API key used for authentication with the licensing server.   
* **shared_key (str,optional)**: A shared secret key used alongside the API key for enhanced security during the license verification process.  
* **file_key (str)**: The encryption key used for securing license files on the client side.   
* **file_iv (str)**: The initialization vector for the encryption algorithm. This complements the file_key for encrypting and decrypting license files.   
* **hardware_id_provider (object, optional)**: The provider class used for generating a unique hardware ID. This ID helps in binding the license to specific hardware. Defaults to HardwareIdProvider.  
* **verify_license_signature (bool, optional)**: A boolean flag indicating whether the license's digital signature should be verified. Defaults to True for enhanced security.  
* **signature_verifier (object, optional)**: The class responsible for verifying the digital signature of licenses. Defaults to SignatureVerifier.  
* **api_domain (str, optional)**: The domain name of the API server with which the licensing operations are performed. Defaults to "api.licensespring.com".  
* **api_version (str, optional)**: The version of the API to use for requests. This allows for compatibility with different versions of the licensing API. Defaults to "v4".  
* **filename (str, optional)**: The default filename for saved license files. This can be customized as needed. Defaults to "License".  
* **file_path (str, optional)**: The path where license files should be saved on the client system. If not specified, a **[default location](https://docs.licensespring.com/sdks/tutorials/best-practices/local-license-file#W8U6X)** is used.  
* **grace_period_conf (int, optional)**: The number of hours to allow as a grace period for  Defaults to 24 hours. 
* **air_gap_public_key (str, optional)**: Air gap public key from platform check **[here](https://docs.licensespring.com/sdks/tutorials/licensing-scenarios/air-gapped#Ws1BB)** for more
* **client_id (str, optional)**: Client ID for OAuth authorization purposes
* **client_secret (str, optional)**: Client Secret for OAuth authorization purposes
* **certificate_chain_path (str, optional)**: Used for singature verification for Floating Server v2 (e.g "path_to_cert_chain/chain.pem"). This file is provided by the platform.

**Warning:**  
* We advise for `hardware_id_provider` to use a newly developed [`HardwareIdProviderSource`](#hardwareidprovidersource) provider.
* On the next major version release [`HardwareIdProviderSource`](#hardwareidprovidersource) will be set as default `hardware_id_provider`
* if both **API keys** and **OAuth** is specified SDK will use OAuth for authorization
  
### LicenseID

* **from_key(cls, key)**: Class method to create a LicenseID instance for key-based activation  
* **from_user(cls, username, password)**: Class method to create a LicenseID instance for user-based activation.

#### Key-based setup
```python
license_id = LicenseID.from_key("your_license_key") 
```
#### User-based setup
```python
license_id = LicenseID.from_user(username="email@email.com",password="password")                          
```
### LicenseManager  
```python
from licensespring.licensefile.license_manager import LicenseManager,LicenseID

manager = LicenseManager(conf)
```
#### Configuration parametres

conf (Configuration): **[A configuration object](#configuration-setup)**

#### activate_license  
Activates a license with the license server and updates local license data. When activating user based license we advise that **unique_license_id** is set which represent **"id"** field within the [license check](https://docs.licensespring.com/license-api/check).  

**Key-based**
```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H6QM-6H5R-ZENJ-VBLK")

license = manager.activate_license(license_id)
```
**User-based**
```python
manager = LicenseManager(conf)

license_id = LicenseID.from_user(username="python@gmail.com",password="7t_x3!o9")

license = manager.activate_license(license_id,unique_license_id=1723642193958949)
```
**Parameters**:  
* **license_id** (LicenseID): An instance containing the license key or user credentials.    

**Return**:
**License** object representing the activated license.

#### load_license  
Loads the license file and sets attributes for the LicenseData instance. Returns an instance of the License class reflecting the loaded license.

```python
manager = LicenseManager(conf)

license = manager.load_license()
```
**Return**:
**License** object representing the activated license.
  
#### current_config
Get current configuration
```python
manager = LicenseManager(conf)

config = manager.current_config()
```

**Return** (dict): current configuration

#### reconfigure
Change the current configuration  

**Parameters**:
* **conf** (Configuration): Configuration object  

```python
manager = LicenseManager(conf)

manager.reconfigure(
        Configuration(
            product="lkprod2",
            api_key="new_key",
            shared_key="new_key",
            file_key="file_key",
            file_iv="file_iv",
            file_path="bb",
            grace_period_conf=12,
            is_guard_file_enabled=True,
        )
    )
```
#### is_license_file_corrupted
Checks if licensefile is corrupted  

```python
manager = LicenseManager(conf)
boolean = manager.is_license_file_corrupted()
```
**Return** (bool): If the file is corrupted return True, otherwise False

#### clear_local_storage
Clear all data from current product

```python
manager = LicenseManager(conf)
license_id = LicenseID.from_key("H6QM-6H5R-ZENJ-VBLK")  
license = manager.activate_license(license_id)  
manager.clear_local_storage()
```

#### data_location
Get licensefile location 

```python
manager = LicenseManager(conf)
folder_path = manager.data_location()
```
**Return** (str): Licensefile location  

#### set_data_location
Set data location

**Parameters**:
* **path** (str): new data location path

```python
manager = LicenseManager(conf)
manager.set_data_location()
```
**Return**: None

#### license_file_name
Get licensefile name 

```python
manager = LicenseManager(conf)
file_name = manager.license_file_name()
```
**Return** (str): Licensefile name  

#### set_license_file_name

Set licensefile name 

**Parameters**:
* **name** (str): license file name

```python
manager = LicenseManager(conf)
manager.set_license_file_name()
```
**Return**: None 

#### is_online  
Checks if the licensing server is accessible. Returns True if online, False otherwise.  

**Parameters**:  
* **throw_e** (bool,optional): If True throws exception, otherwise exception won't be raised.   

```python
manager = LicenseManager(conf)

license = manager.is_online()
```

#### get_air_gap_activation_code
Get activation code for air gap license

**Parameters**:

* **initialization_code** (str): initialization code    
* **license_key** (str): license key  
```python
initialization_code = "Q/MWfwp1NWAYARl8Q7KSo5Cg2YKqS2QLlnQ3nEeSBsk="
license_key = "UFF3-E9GA-VUJQ-GMLK"

manager = LicenseManager(conf)
activation_code = manager.get_air_gap_activation_code(initialization_code=initialization_code, license_key=license_key)

print("Activation code:",activation_code)
```
**Return** (str): activation code

#### activate_air_gap_license
Activate air gap license

**Parameters**:

* **confirmation_code** (str): confirmation code
* **policy_path** (str): policy path (file or folder)
* **license_key** (str): license_key
* **policy_id** (str): policy id

```python
confirmation = "ERbQBuE8giIjqMPj972Skipehqn0szQ8TH56INyo3OdtMHO1SuTVsoCOSnJWB6rml98PJ6SjybTPymOVZTG4hQ=="
policy_id = "998"
license_key = "UFF3-E9GA-VUJQ-GMLK"
policy_path = "path_to_air_lic"

manager = LicenseManager(conf)
license = manager.activate_air_gap_license(
                confirmation_code=confirmation, policy_path=policy_path, license_key=license_key, policy_id=policy_id
            )
```
**Raises**:
* **LicenseActivationException**: Signature verification failed

**Return** (License): License

#### create_offline_activation_file
Creates .req file for offline activation, including various optional parameters related to the device and software environment. 

**Parameters**:

* **license_id** (LicenseID): An instance containing the license key or user credentials.  
* **req_path** (str): Specify the path where to create .req file.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H94R-S6KB-L7AJ-SXLK")

req_file_path = manager.create_offline_activation_file(license_id,'offline_files/test')              
```
**Return** (str): Path of the .req file created for activation.

#### activate_license_offline
Activates a license offline using a .lic file provided via the specified path.

**Parameters**:

* **ls_activation_path** (str): Path to the activation file.

```python
file_path = 'offline_files/ls_activation.lic'

manager = LicenseManager(conf)

license = manager.activate_license_offline(file_path)
```
**Raises**:

* **LicenseActivationException**: Activation data is not valid.
* **LicenseActivationException**: Response file ID mismatch.
* **LicenseActivationException**: License does not belong to this device.

**Return**(License): Returns a License object representing the activated license.

#### get_trial_license
Creates LiceseID for trial licenses

**Parameters**:

* **customer** (Customer): Customer object
* **license_policy** (str,optional): license policy code. Defaults to None.

```python
customer = Customer(email='python_policy@gmail.com')  

manager = LicenseManager(conf)

license_id = manager.get_trial_license(customer=customer,license_policy='test')
    
license = manager.activate_license(license_id=license_id)
```

**Return**(LicenseID): Returns a LicenseID object.

#### get_version_list
Get versions

**Parameters**:

* **license_id** (LicenseID): license id object
* **channel** (str, optional): channel of the version 
* **unique_license_id** (int,optional): A unique identifier for the license.
* **env** (str,optional): Version of environment

```python

manager = LicenseManager(conf)

license_id = LicenseID.from_key("3ZG2-K25B-76VN-WXLK")

response = manager.get_version_list(license_id=license_id)
```

**Return**(list): List of versions

#### get_product_details
Get product details

**Parameters**:

* **include_latest_version** (bool, optional): include_latest_version. Defaults to False.
* **include_custom_fields** (bool, optional): include_custom_fields. Defaults to False.
* **env** (str, optional): env. Defaults to None.

```python

manager = LicenseManager(conf)

license_id = LicenseID.from_key("3ZG2-K25B-76VN-WXLK")

response = manager.get_product_details(license_id=license_id)
```

**Return**(dict): Product details

#### get_installation_file
Get installation file

**Parameters**:

* **license_id** (LicenseID): An instance containing the license key or user credentials  
* **channel** (str, optional): channel of the version   
*  **unique_license_id** (int, optional): A unique identifier for the license.   
* **env** (str, optional): Version of environment
* **version** (str, optional): Versions

```python

manager = LicenseManager(conf)

license_id = LicenseID.from_key("3ZG2-K25B-76VN-WXLK")

response = manager.get_installation_file(license_id=license_id)
```

**Return** (dict): installation file

#### get_customer_license_users
Get customer license users

**Parameters**:
* customer (Customer): customer
```python

manager = LicenseManager(conf)

customer = Customer(email="c1@c.com")

response = manager.get_customer_license_users(customer=customer)
```
**Return**(dict): customer license user

#### get_user_licenses

Get user licenses

**Parameters**:
* **license_id** (LicenseID): license_id

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_user(username="t@tt.com", password="d#2!17vi")

response = manager.get_user_licenses(license_id)
```

**Return**(list): User licenses

#### get_sso_url

Get user licenses

**Parameters**:
* **account_code** (str): account code
* **use_auth_code** (bool, optional): Use code for response_type. Defaults to True.

```python
manager = LicenseManager(conf)

response = manager.get_sso_url(account_code="your_account_code")
```

**Return**(dict): url

### Bundle Manager

Object responsible for Bundle operations

```python
from licensespring.licensefile.config import Configuration
from licensespring.licensefile.license_manager import LicenseID
from licensespring.licensefile.bundle_manager import BundleManager

conf = Configuration(
        product="your-product-code",
        api_key="your-api-key",
        shared_key="your-shared-key",
        file_key="d66db34b03c2d6961bb3e14ff40592c0c39ec7210113f194c0da50c2d4d002be",
        file_iv="a770af52b2aa3b73ad218b6cfc4e9707")

bundle_manager = BundleManager(conf)
```


#### activate_bundle

Activates the bundle

**Parameters**:

* **license_id** (LicenseID): An instance containing the license key or user credentials.  
* **hardware_id**(str, optional): A unique identifier for the hardware.  
* **unique_license_id** (int, optional): A unique identifier for the license.  
* **customer_account_code** (str, optional): An account code for the customer.  
* **id_token** (str, optional): Token for identity verification.  
* **code** (str, optional): An additional code for license verification.  
* **app_ver** (str, optional): The version of the application requesting activation.  
* **os_ver** (str, optional): The operating system version of the host.  
* **hostnam**e (str, optional): The hostname of the device requesting activation.  
* **ip** (str, optional): The IP address of the device.  
* **is_vm** (bool, optional): Indicates whether the application is running on a virtual machine.  
* **vm_info** (str, optional): Information about the virtual machine, if applicable.  
* **mac_address** (str, optional): The MAC address of the device.  

```python
#user based
license_id = LicenseID().from_user(username="ki@ki.com",password="!f53n!z2")
#key based
license_id = LicenseID().from_key("ASQU-AYHA-FX4S-FRLK")

bundles = bundle_manager.activate_bundle(license_id)
```  
**Return (dict[str, License])**: A dictionary where the keys are product short codes and the values are License objects.

#### get_current_bundle

Get current bundle from cache or licensefile.

```python

bundles = bundle_manager.get_current_bundle()

```  
**Return (dict[str, License])**: A dictionary where the keys are product short codes and the values are License objects.

#### create_offline_activation_file

Creates .req file for activation 

**Parameters**:
* **license_id** (LicenseID): An instance containing the license key or user credentials.  
* **req_path** (str): Specify place where to create .req file  
* **hardware_id** (str, optional): A unique identifier for the hardware.  
* **app_ver** (str, optional): The version of the application requesting activation.  
* **os_ver** (str, optional): The operating system version of the host.  
* **hostname** (str, optional): The hostname of the device requesting activation.  
* **ip** (str, optional):  The IP address of the device.  
* **is_vm** (bool, optional): Indicates whether the application is running on a virtual machine.  
* **vm_info** (str, optional): Information about the virtual machine.  
* **mac_address** (str, optional): The MAC address of the device.  
* **device_variables** (dict, optional): device varaibles.  

```python

license_id = LicenseID.from_key("VNFT-7KPY-D5BQ-5NLK")
    
req_file_path = bundle_manager.create_offline_activation_file(license_id, "file_path")

``` 

**Return(str)**: path of the .req file

#### activate_bundle_offline

Activate offline bundle licenses

**Parameters**:
* **ls_activation_path** (str): path to a .lic file

```python

bundle_manager.activate_bundle_offline("file_path_to_lic_file.lic")

``` 

**Return (dict[str, License])**: dictionary of licenses in a bundle


#### deactivate_bundle_offline

Generates .req file for the offline deactivation

**Parameters**:
**license_id** (LicenseID): license_id
**offline_path** (str): path of the .req file
**unique_license_id** (int): unique license id

```python

license_id = LicenseID.from_key("VNFT-7KPY-D5BQ-5NLK")
bundle_manager.deactivate_bundle_offline(license_id,"file_path")

``` 

**Return(str)**: path of the deactivation file

#### check_bundle
Check bundle and update the licensefile

**Parameters**:
* **license_id** (LicenseID): license_id  
* **hardware_id**(str, optional): A unique identifier for the hardware. Defaults to None.  
* **unique_license_id** (int, optional): A unique identifier for the license. Defaults to None.   
* **include_expired_features** (bool, optional): If True, includes expired license features in the check.   Defaults to False.  
* **env** (str, optional): optional param takes "win", "win32", "win64", "mac", "linux", "linux32" or "linux64". Defaults to None.  

```python

license_id = LicenseID.from_key("VNFT-7KPY-D5BQ-5NLK")
# make sure that bundle is activated
bundles = bundle_manager.check_bundle(license_id,"file_path")

``` 

**Returns (dict[str, License])**: A dictionary where the keys are product short codes and the values are License objects.  

#### deactivate_bundle
Deactivate bundle

**Parameters**:
* **license_id** (LicenseID): license_id
* **hardware_id** (str, optional): hardware id. Defaults to None.
* **unique_license_id** (int, optional): A unique identifier for the license. Defaults to None.
* **remove_local_data** (bool, optional): remove licensefile from storage. Defaults to False.

```python

license_id = LicenseID.from_key("VNFT-7KPY-D5BQ-5NLK")

bundle_manager.deactivate_bundle(license_id,"file_path")

``` 

### License object

Object responsible for license operations

#### is_floating_expired

Determines wheter the license floating period has expired

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.check()

response = license.is_floating_expired()                 
```
**Return (bool)**: True if license floating period has expired otherwise False

#### floating_timeout

Retrieve license flaoting timeout

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

print(license.floating_timeout())
```
**Return (int)**: License floating timeout

#### is_floating

Check if license is floating (Floating Server or Floating Cloud)

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

print(license.is_floating())
```

**Return (bool)**: True if license if floating, otherwise False

#### floating_client_id
Get floating client id

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

print(license.floating_client_id())
```

**Return (str)**: Floating client id

#### is_controlled_by_floating_server
Check if license is controlled by Floating Server

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

print(license.is_controlled_by_floating_server())
```

**Return (bool)**: True if license is controlled by floating server, otherwise False

#### floating_in_use_devices
Number of floating devices in use

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

print(license.floating_in_use_devices())
```

**Return (int)**: Number of floating devices in use

#### floating_end_date
Datetime when flaoting will be released

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

print(license.floating_end_date())
```

**Return (datetime)**: Datetime when device will be released

#### max_floating_users
Number of max floating users

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

print(license.max_floating_users())
```

**Return (int)**: Number of max floating users

#### is_validity_period_expired

Determines whether the license's validity period has expired

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.is_validity_period_expired()                 
```
**Return (bool)**: True if license expired;False if license is valid

#### validity_period

Gets validity period of the license

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.validity_period()                 
```
**Return (datetime)**: Datetime in UTC

#### validity_with_grace_period

Gets the validity period with grace period of the license

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.validity_with_grace_period()                 
```
**Return (datetime)**: Datetime in UTC

#### license_user
Gets the license user

```python
user_data = license.license_user()
    
print(user_data)               
```
**Return** (dict): license user


#### maintenance_days_remaining

Gets how many days are left until the maintenance ends

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.maintenance_days_remaining()                 
```
**Return (int)**: Maintenance days left

#### days_remaining

Gets how many days are left until the validity period ends

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.days_remaining()                 
```
**Return (int)**: Validity period days left

#### customer_information

Gets customer information

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.customer_information()            
```
**Return (dict)**: customer information

#### id
Gets license id

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.id()            
```
**Return (int)**: license id

#### max_transfers

Get the max transfers

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.max_transfers()            
```
**Return (int)**: max transfers

#### transfer_count

Get the transfer count

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.transfer_count()            
```
**Return (int)**: transfer count

#### is_device_transfer_allowed

Get if the device transfer is allowed

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.is_device_transfer_allowed()            
```
**Return (bool)**: True if device transfer is allowed otherwise False.

#### is_device_transfer_limited

Get if the device transfer is limited

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response = license.is_device_transfer_limited()            
```
**Return (bool)**: True if device transfer is limited otherwise False.

#### days_since_last_check

Get how many days passed since last check

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.check()
    
response = license.days_since_last_check()            
```
**Return (int)**: How many days have passed since last check. 

#### start_date

Get the start date of the license

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.start_date()            
```
**Return (datetime)**: Datetime in UTC

#### maintenance_period

Get the maintenance period of the license

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.maintenance_period()            
```
**Return (datetime)**: Datetime in UTC

#### is_maintence_period_expired
Checks if maintence period has expired

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.is_maintence_period_expired()            
```
**Return (bool)**: If maintence period expired returns True otherwise False

#### last_check
Gets when the last check was performed

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.last_check()            
```
**Return (datetime)**: Datetime in UTC

#### last_usage
Gets when the last license usage

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.last_usage()            
```
**Return (datetime)**: Datetime in UTC

#### license_type
Gets the license type

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.license_type()            
```
**Return (str)**: License type

#### max_activations
Gets the license max activations

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.max_activations()            
```
**Return (int)**: max activations

#### metadata
Gets the license metadata

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.metadata()            
```
**Return (dict)**: metadata

#### allow_unlimited_activations
Check if unlimited activationsis allowed

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.allow_unlimited_activations()            
```
**Return (bool)**: If unlimited activations is allowed returns True otherwise False

#### allow_grace_subscription_period
Check if grace subscription period is allowed

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.allow_grace_subscription_period()            
```
**Return (bool)**: If grace subscription period is allowed returns True otherwise False

#### is_subscription_grace_period_started
Check if grace subscription period has started

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.is_subscription_grace_period_started()            
```
**Return (bool)**: If grace subscription period has started returns True otherwise False

#### is_grace_period_started
Check if license is in grace period

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.is_grace_period_started()            
```
**Return (bool)**: True if grace period has started, otherwise False

#### grace_period_hours_remaining

Get remain hours of grace period

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.grace_period_hours_remaining()            
```
**Return (int)**: Number of hours left in grace period


#### get_grace_period
Get grace period 

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.get_grace_period()            
```
**Return (int)**: grace period

#### subscription_grace_period
Get subscription grace period 

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.subscription_grace_period()            
```
**Return (int)**: subscription grace period

#### is_expired
Checks if the license validity has expired

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.is_expired()            
```
**Return (bool)**: True if license has expired otherwise False

#### license_enabled
Checks if the license is enabled

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.license_enabled()            
```
**Return (bool)**: True if license is enabled otherwise False

#### license_active
Checks if the license is active

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.license_active()            
```
**Return (bool)**: True if license is active otherwise False

#### is_valid
Checks if the license is valid (license is active, enabled and didn't expired)

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.is_valid()            
```
**Return (bool)**: True if license is valid otherwise False


#### prevent_vm
Checks if the license prevents virtual machines

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.prevent_vm()            
```
**Return (bool)**: True if license prevents VM's otherwise False

#### is_trial
Checks if the license is trial 

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.is_trial()            
```
**Return (bool)**: True if license is trial otherwise False

#### expiry_date
Get expiry date of floating license

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.expiry_date()            
```
**Return (datetime)**: Expiry date in UTC

#### borrow_until
Get the date until a license is borrwed

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.borrow_until()            
```
**Return (datetime)**: borrow_until in UTC

#### is_borrowed
Check if a license is borrowed

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.is_borrowed()            
```
**Return (bool)**: True if license is borrowed otherwise False

#### local_consumptions
Get local consumptions

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.local_consumptions()            
```
**Return (int)**: local consumptions

#### max_consumptions
Get max consumptions

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.max_consumptions()            
```
**Return (int)**: max consumptions

#### total_consumptions
Get total consumptions

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.total_consumptions()            
```
**Return (int)**: total consumptions

#### max_overages
Get max overages

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.max_overages()            
```
**Return (int)**: max_overages

#### allow_unlimited_consumptions
Check if unlimited consumptions is allowed

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.allow_unlimited_consumptions()            
```
**Return (int)**: If unlimited consumptions are allowed return True otherwise False

#### consumption_reset
Check if there is consumption reset

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.consumption_reset()            
```
**Return (bool)**: If there is consumption reset returns True otherwise False

#### allow_overages
Check if overages are allowed

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.allow_overages()            
```
**Return (bool)**: If overages are allowed returns True otherwise False

#### consumption_period
Get consumption period

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

response = license.allow_overages()            
```
**Return (str)**: Consumption period

#### get_feature_data
Get feature data

**Parameters**:
* feature_code (str): feature code


```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

feature_code = "feature1"

response = license.get_feature_data(feature_code)            
```
**Return (dict)**: Feature

#### features
Get feature list

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

print(license.features())         
```
**Return (list)**: Features

#### check_license_status

Verifies the current status of the license. It raises exceptions if the license is not enabled, not active, or expired

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
license.check_license_status()                                       
```
**Raises**:  
**LicenseStateException**: Raised if the license fails one of the following checks:
* License is not enabled.
* License is not active.
* License validity period has expired.  

**Return**: None

#### check

Performs an online check to synchronize the license data with the backend. This includes syncing consumptions for consumption-based licenses.

**Parameters**:

* **include_expired_features (bool, optional)**: Includes expired license features in the check.
* **env (str, optional)**: "win", "win32", "win64", "mac", "linux", "linux32" or "linux64"

  
```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
response=license.check()                                                            
```
**Raises**:

**ClientError**: Raised if there's an issue with the API client's request, such as invalid credentials or unauthorized access.

**RequestException**: Raised if there's a problem with the request to the licensing server, such as network issues or server unavailability.

**Return (dict)**: The updated license cache.

#### deactivate

Deactivates the license and optionally deletes the local license file.

**Parameters**:

* **delete_license (bool, optional)**: If **True**, deletes the local license file upon deactivation.

  
```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
license.deactivate()                                                       
```

**Return**: None


#### local_check

This method ensures the integrity and consistency of the licensing information by comparing the data stored in the local license file with the predefined configurations in the **Configuration object**.

  
```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
license.local_check()                                                                      
```
**Raises**:

**ConfigurationMismatch**: Raised if the product code or hardware ID in the license file does not match the expected values provided in the Configuration  
**VMIsNotAllowedException**: Raised if the license is used in a VM environment when the license explicitly disallows it.  
**TimeoutExpiredException**: Raised if a floating license has expired. This is more relevant if is_floating_expired is later implemented to perform actual checks.
**ClockTamperedException**: Raised if there is evidence of tampering with the system's clock, detected by comparing the system's current time with the last usage time recorded in the license file.

**Return**: None

#### add_local_consumption

Adds local consumption records for **consumption-based licenses**.
**Parameters**:

* **consumptions (bool, optional)**: The number of consumptions to add locally
  
```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)
    
license.add_local_consumption()           
```

**Raises**:  
**LicenseSpringTypeError**: Raised if the license type does not support consumption (i.e., not a consumption-based license).  
**ConsumptionError**: Raised if adding the specified number of consumptions would exceed the allowed maximum for the license.

**Return**: None

#### sync_consumption

Synchronizes local consumption data with the server, adjusting for overages if specified.

Parameters:
* **req_overages (int, optional)**: Specifies behavior for consumption overages.
 
```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.add_local_consumption(5)
    
license.sync_consumption()
```
**Raises**:    
**RequestException**: Raised if the request to synchronize consumption data with the server fails, for instance, due to network issues or server unavailability.

Return (bool): True if the consumption data was successfully synchronized; False otherwise.

#### is_grace_period

Determines if the current license state is within its grace period following a specific exception.

**Parameters**:

* **ex** (Exception): Raised Exception
 
```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

try:
    license.check()

except Exception as ex
    boolean = license.is_grace_period(ex)
```

**Return (bool)**: True if the license is within its grace period, False otherwise

#### change_password

Changes password of a user

**Parameters**:

* **password** (str): Old password of license user
* **new_password**(str): New password of license user

 
```python
manager = LicenseManager(conf)

license_id = LicenseID.from_user(username="python@gmail.com",password="7t_x3!o9")

license = manager.activate_license(license_id)

license.change_password(password="7t_x3!o9",new_password="12345678")                    
```
**Return (str)**: "password_changed"


#### setup_license_watch_dog

Initializes and starts the license watchdog with the specified callback and timeout settings.

**Parameters**:

**callback** (Callable): A callable to be executed by the watchdog in response to specific events or conditions.  
**timeout** (int): The period in minutes after which the watchdog should perform its checks.
**deamon** (bool, optional): Run thread as deamon. Defaults to False.  
**run_immediately** (bool,optional): run license check immediately, if False wait for timeout first.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.setup_license_watch_dog(callback,timeout)                   
```

**Return**: None

#### stop_license_watch_dog

Stops the license watchdog if it is currently running, effectively halting its monitoring and callback activities.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.setup_license_watch_dog(callback,timeout)
                                
license.stop_license_watch_dog()                  
```
**Return**: None

#### setup_feature_watch_dog

Initializes and starts the feature watchdog with the specified callback and timeout.

**Parameters**:

**callback** (Callable): A callable to be executed by the watchdog in response to specific events or conditions.  
**timeout** (int): The period in minutes after which the watchdog should perform its checks.  
**deamon** (bool, optional): Run thread as deamon. Defaults to False.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.setup_feature_watch_dog(callback,timeout)                   
```

**Return**: None

#### stop_feature_watch_dog

Stops the feature watchdog if it is currently running.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.setup_feature_watch_dog(callback,timeout)
                                
license.stop_feature_watch_dog()                  
```
**Return**: None


#### add_local_feature_consumption
Adds local consumption to the feature.

**Parameters**:
* **feature** (str): feature code.
* **consumptions** (int,optional): Number of consumptions.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.add_local_feature_consumption("lkprod1cf1",3) 
```    

**Raises**:

* **ItemNotFoundError**: If the feature specified by `feature_code` does not exist.

* **LicenseSpringTypeError**: If the identified feature is not of the "consumption" type.

* **ConsumptionError**: If adding the specified number of consumptions would exceed the feature's consumption limits.



**Return**: None


#### sync_feature_consumption
Synchronizes local consumption data with the server.
**Parameters**:

* **feature** (str): feature code.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.add_local_feature_consumption("lkprod1cf1",3)

license.sync_feature_consumption("lkprod1cf1")
```             

**Return** (bool): True if the consumption data was successfully synchronized; False otherwise.


#### floating_borrow
Attempts to borrow a floating license until the specified date, updating the system status based on the outcome of the borrow attempt.

**Parameters**:

* **borrow_until** (str): A string representing the date until which the license should be borrowed.
* **password** (str,optional): Password for the license if required.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.floating_borrow("2031-05-06T00:00:00Z")    
```  
**Return**: None

#### floating_release
Releases a borrowed floating license and updates the license status accordingly.

**Parameters**:

* **throw_e**(bool): A boolean indicating whether to raise an exception on failure.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.check()

license.floating_release(False)   
```  

**Return**: None

#### check_feature
Checks for a specific license feature and updates the license cache accordingly.

**Parameters**:

* **feature**(str): feature code.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.check_feature("lkprod1f1fc1")    
```  

**Return**: None

#### release_feature
Releases a borrowed license feature and updates the license cache accordingly.

**Parameters**:

* **feature**(str): feature code.

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

license.check_feature("lkprod1f1fc1")

license.release_feature("lkprod1f1fc1")   
```  

**Return**: None

#### update_offline
Updates license via refresh file

**Parameters**:

* **path** (str): path of the refresh file
* **reset_consumption** (bool): True resets consumption otherwise False


```python
file_path = 'path_to_lic_file/license.lic'

manager = LicenseManager(conf)

license = manager.activate_license_offline(file_path)

license.update_offline('offline_files/license_refresh.lic',False)                      
```  
**Raises**:

* **ConfigurationMismatch**: The update file does not belong to this device
* **ConfigurationMismatch**: The update file does not belong to this product  

**Return**(bool): True if license was successfully updated otherwise False

#### get_deactivation_code

Get deactivation code for air gap licenses

**Parameters**:
* **initialization_code** (str): initialization_code

```python
initialization_code="your_initialization_code"
manager = LicenseManager(conf)
#load air gap license
license = manager.load_license()

deactivation_code = license.get_deactivation_code(initialization_code)

print("Deactivation code:",deactivation_code)
```  

**Return** (str): deactivation code

#### deactivate_air_gap

Deactivate air gap license and clear storage

**Parameters**:
* **confirmation_code** (str): confirmation_code


```python
confirmation_code="your_confirmation_code"
manager = LicenseManager(conf)
#load air gap license
license = manager.load_license()
license.deactivate_air_gap(confirmation_code)
```
**Raises**:
* **LicenseActivationException**: VerificationError

**Return**: None
#### deactivate_offline
Generates .req file for the offline deactivation

**Parameters**:

* **offline_path**(str): path of the .req file


```python
file_path = 'path_to_lic_file/license.lic'

manager = LicenseManager(conf)

license = manager.activate_license_offline(file_path)

license.deactivate_offline('path_where_to_create_req_file')                     
```  
**Raises**:

* **ConfigurationMismatch**: The update file does not belong to this device
* **ConfigurationMismatch**: The update file does not belong to this product  

**Return**(bool): True if license was successfully updated otherwise False

#### product_details
Update product details from LicenseSpring server

**Parameters**:

* **include_custom_fields** (bool, optional): custom fields information. Defaults to False.
* **include_latest_version** (bool, optional): Lateset version information. Defaults to False.
* **env (str, optional)**: "win", "win32", "win64", "mac", "linux", "linux32" or "linux64"
            

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H9V3-72XX-ZRAJ-S6LK")

license = manager.activate_license(license_id)
    
response = license.product_details()                    
```  
**Raises**:
 

**Return**(dict): response

#### get_product_details
Get product details from licensefile (offline)

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H7G3-F4PJ-4AEJ-UKYL")

license = manager.activate_license(license_id)

feature_code = "feature1"

response = license.get_product_details()            
```
**Return (dict)**: Product details

#### get_device_variables
Get device variable if exists

**Parameters**:

* **variable_name** (str): variable name            

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H9V3-72XX-ZRAJ-S6LK")

license = manager.activate_license(license_id)
    
device_var = license.get_device_variable('english')               
```  
**Raises**:
 

**Return**(dict): variable dictionary

#### set_device_variables
Set device variables locally 

**Parameters**:

* **variables** (dict): variables dict
* **save** (bool, optional): Save cache to licensefile. Defaults to True.
            

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H9V3-72XX-ZRAJ-S6LK")

license = manager.activate_license(license_id)
    
license.set_device_variables({"english":"value"})                   
```  
**Raises**:
 

**Return**: None

#### get_device_variables
Get device variables from server or locally

**Parameters**:

* **get_from_be** (bool, optional): If True collects data from LicenseSpring server. Defaults to True.
            

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H9V3-72XX-ZRAJ-S6LK")

license = manager.activate_license(license_id)
    
license.get_device_variables(get_from_be=True)                 
```  
**Raises**:
 * **RequestException** (Grace period not allowed)

**Return**(list): List of device variables

#### send_device_variables
Send device variables to LicenseSpring server. Handles GracePeriod
            

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H9V3-72XX-ZRAJ-S6LK")

license = manager.activate_license(license_id)
    
license.send_device_variables()                   
```  
**Raises**:
 * **RequestException** (Grace period not allowed)

**Return**(bool): True if new variables are sent to LicenseSpring server otherwise, False

#### custom_fields
Get custom fields from licensefile

```python
manager = LicenseManager(conf)

license_id = LicenseID.from_key("H9V3-72XX-ZRAJ-S6LK")

license = manager.activate_license(license_id)
    
response = license.custom_fields()                   
``` 
**Return**(list): Custom fields

## Floating Server

The user has the ability to utilize either a **Floating Client** or a **Floating Manager**:

**Floating Client**:
* This object is responsible for managing the operations on Floating Server

**Floating Manager**:
* This object is responsible for managing operations with the Floating Server, while also integrating the license file

### Floating Client

#### Intialization

To initialize a Floating Client, the user must specify the API protocol and domain.

* **api_protocol**: Defines the communication protocol between the client and the server (e.g., "http").
* **api_domain**: Specifies the domain or IP address and port of the Floating Server (e.g., "localhost:8080").
* **hardware_id_provider** (optional): Provides the client's hardware ID, which can be used to uniquely identify the client machine.

```python
from licensespring.floating_server import FloatingAPIClient
from licensespring.hardware import HardwareIdProvider

api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080",hardware_id_provider=HardwareIdProvider)
```
#### auth
Authenticate

**Parameters**:
* **username** (str): username
* **password** (str): password

```python
from licensespring.floating_server import FloatingAPIClient

api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")
api_client.auth(username="admin",password="tetejac")
```
**Return**(dict): Response

#### register_user

Register user

**Parameters**:

* **product** (str): product short code.
* **user** (str,optional): user. Defaults uses hardware id.
* **os_hostname** (str, optional): os hostname. Defaults to None.
* **ip_local** (str, optional): ip local. Defaults to None.
* **user_info** (str, optional): user info. Defaults to None.
* **license_id** (int, optional):license id. Defaults to None.

```python
api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")

response = api_client.register_user(
    product="lkprod1",
    user="user_1",
    os_hostname="bla",
    ip_local="bla",
    user_info="bla",
    license_id=1728377159207169
)

print(response)
```
**Return**(dict): Response

#### unregister

**Parameters**

* **product** (str): product short code.
* **user** (str,optional): user. Defaults uses hardware id.
* **license_id** (int, optional): license id. Defaults to None.


Unregister user

```python

api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")

response = api_client.unregister_user(product="lkprod1",user="user_1",license_id=1728377159207169)

print(response)
```

**Return**(str): "user_unregistered"

#### unregister_all

Unregister all users

```python
api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")

api_client.unregister_all()
```

#### borrow 

Borrow license

**Parameters**

* **product** (str): product short code.
* **user** (str,optional): user. Defaults uses hardware id.
* **borrowed_until** (str): borrow until date
* **os_hostname** (str, optional): os hostname. Defaults to None.
* **ip_local** (str, optional): ip local. Defaults to None.
* **user_info** (str, optional): user info. Defaults to None.
* **license_id**(int, optional):license id. Defaults to None.

```python
api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")

response = api_client.borrow(
        product="lkprod1",
        user="user_1",
        borrowed_until="2029-05-06T00:00:00Z",
        os_hostname="bla",
        ip_local="bla",
        user_info="bla",
        license_id=1728377159207169,
    )
```

**Return**(dict): Response

#### add_consumption

Add license consumption

**Parameters**

* **product** (str): product short code
* **consumptions** (int, optional): consumptions. Defaults to 1.
* **max_overages** (int, optional): max overages. Defaults to None.
* **allow_overages** (bool, optional): allow overages. Defaults to None.
* **user** (str, optional): user (default uses hardware id)
* **license_id** (int, optional): license id. Defaults to None.


```python
api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")

response = api_client.add_consumption(product="fs", consumptions=1)
```

**Return**(dict): Response

#### add_feature_consumption

Add feature consumption

**Parameters**
* **product** (str): product short code
* **feature_code** (str): feature code
* **user** (str, optional): user (default uses hardware id)
* **consumptions** (int, optional): consumptions. Defaults to 1.
* **license_id** (int, optional): license id. Defaults to None.

```python
api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")

response = api_client.add_feature_consumption(product="fs", feature_code="f2", consumptions=1)
```

**Return**(dict): Response

#### feature_register

Register feature

**Parameters**

* **product** (str): product short code
* **feature_code** (str): feature short code
* **user** (str, optional): user (default uses hardware id)
* **license_id** (int, optional): license id. Defaults to None.
* **borrowed_until** (str): borrow until (e.g. 2029-05-06T00:00:00Z) 
* **os_hostname** (str, optional): os hostname. Defaults to None.
* **ip_local** (str, optional): ip local. Defaults to None.
* **user_info** (str, optional): user info. Defaults to None.

```python
api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")

response = api_client.feature_register(
        product="fs", feature_code="f1", os_hostname="w", ip_local="1.0", user_info="info"
    )
print(response)
```

**Return**(dict): Response

#### feature_release

Feature release

**Parameters**
* **product** (str): product short code
* **feature_code** (str): feature short code
* **user** (str, optional): user (default uses hardware id)
* **license_id** (int, optional): license id. Defaults to None.

```python
api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")

response = api_client.feature_register(
        product="fs", feature_code="f1", os_hostname="w", ip_local="1.0", user_info="info"
    )

response = api_client.feature_release(product="fs", feature_code="f1")
```

**Return**(str): "feature_released"

#### fetch_licenses

List licenses

**Parameters**

* **product** (str,optional): product short code filter

```python
api_client = FloatingAPIClient(api_protocol="http", api_domain="localhost:8080")

response = api_client.fetch_licenses(product="test")
print(response)
```

**Return**(dict): Response

### Floating Manager

#### Intialization

To intialize Floating Manager [Configuration](#configuration-setup) needs to be created. For Floating server you can set arbitrary values for `shared_key` and `api_key` keys. To enable signature verification in Floating Server v2, set the certificate_chain_path in the Configuration object.


#### auth
Authenticate

**Parameters**:
* **username** (str): username
* **password** (str): password

```python
from licensespring.licensefile.config import Configuration
from licensespring.licensefile.floating_manager import FloatingManager

fs_manager = FloatingManager(conf=conf)
fs_manager.auth(username="admin",password="tetejac")
```
**Return**(dict): Response

#### register 

Register license

**Parameters**:

* **os_hostname** (str, optional): os hostname. Defaults to None.
* **ip_local** (str, optional): ip local. Defaults to None.
* **user_info** (str, optional): user info. Defaults to None.
* **license_id** (int, optional):license id. Defaults to None.

```python
from licensespring.licensefile.config import Configuration
from licensespring.licensefile.floating_manager import FloatingManager

conf = Configuration(
    product=product,
    api_key="arbitrary",
    shared_key="arbitrary",
    file_key="your_file_key",
    file_iv="your_file_iv",
    api_domain="api_domain",
    api_protocol="http/https",
    certificate_chain_path="certificate_chain_path/chain.pem" # used for signature verification
)

fs_manager = FloatingManager(conf=conf)
license = fs_manager.register()
```
**Return**(License): License object

#### unregister

**Parameters**

* license_id (int, optional): license id. Defaults to None.

Unregister license

```python
fs_manager = FloatingManager(conf=conf)
# There are multiple options to unregister a license
# 1. floating client -> this one is documanted
fs_manager.unregister()
# 2.1. license object -> deactivate method
license.deactivate() 
#2.2 license object -> floating release
license.floating_release(False)
```

**Return**(str): "user_unregistered"


#### unregister_all

Unregister all users

```python
fs_manager = FloatingManager(conf=conf)
fs_manager.unregister_all()
```

#### borrow_license

Borrow license

**Parameters**

* **borrowed_until** (str): borrow until date
* **os_hostname** (str, optional): os hostname. Defaults to None.
* **ip_local** (str, optional): ip local. Defaults to None.
* **user_info** (str, optional): user info. Defaults to None.
* **license_id**(int, optional):license id. Defaults to None.

```python
fs_manager = FloatingManager(conf=conf)
license = fs_manager.borrow("2031-05-06T00:00:00Z")
# borrow can be also used within the License object
license.floating_borrow("2031-05-06T00:00:00Z")
```

**Return**(License): License object

#### is_online

Checks if floating server is online

**Parameters**

* **throw_e** (bool, optional): True if you want raise exception. Defaults to False.

```python
fs_manager = FloatingManager(conf=conf)
response = fs_manager.is_online()
```

**Raises**:
* **ex**: Exception

**Return**(bool): True if server is online, otherwise False

#### fetch_licenses

List licenses

**Parameters**

* **product** (str,optional): product short code filter

```python
fs_manager = FloatingManager(conf=conf)

response = fs_manager.fetch_licenses(product="test")
print(response)
```

**Return**(dict): Response

### Methods supported inside License object
[License consumptions](#add-consumption), [feature consumptions](#add-feature-consumption), [register feature](#check_feature), [release feature](#release_feature) are supported within `License` object for Floating Server
                           
## License

LicenseSpring SDK Source Code License (LSSCL)

Preamble:
This LicenseSpring SDK Source Code License (LSSCL) governs the use, distribution, and modification of the source code for this LicenseSpring SDKs. This SDK is designed to facilitate the integration of LicenseSpring's license management service into your applications. By accessing, using, or modifying the SDK, you agree to the terms and conditions set forth in this license.

1. Permissions:

	* You are permitted to access, read, and modify the source code of this LicenseSpring SDK.
	* You may create derivative works that include this SDK, provided all derivative works are used solely as part of the LicenseSpring service.

2. Distribution:

	* You may distribute the original or modified versions of software that incorporates the SDK, provided that all distributed versions retain this LSSCL license.
	* Distributed versions, including modifications, must be used to facilitate the integration of LicenseSpring’s service and may not be:
		* Provided as part of a hosted or cloud-based service that allows others to access the SDK’s functionality without interacting directly with the LicenseSpring service.
		* Integrated into other services which compete with or do not use the LicenseSpring service.

3. Usage Restrictions:

	* The SDK, in its original or modified form, may only be used as part of the LicenseSpring service, whether on a free or paid plan.
	* You are prohibited from using the SDK independently or as part of any service that does not interact with the LicenseSpring service.

4. Prohibited Actions:

	* You may not circumvent or disable any technical measures that control access to the SDK.
	* You must not remove, alter, or obscure any license notices, copyright notices, or other proprietary notices from the SDK.

5. Termination:

	* Any violation of these terms will result in the automatic termination of your rights under this license.
	* Upon termination, you must cease all use and distribution of the SDK and destroy all copies in your possession.

6. Disclaimer of Warranty and Liability:

	THE SOFTWARE IS PROVIDED "AS IS" AND LICENSESPRING DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. LICENSESPRING SHALL NOT BE LIABLE FOR ANY DAMAGES ARISING OUT OF OR RELATED TO THE USE OR PERFORMANCE OF THE SOFTWARE.

Copyright 2024 Cense Data Inc DBA LicenseSpring
Contact: support@licensespring.com

### Dependency licenses

| Name               | Version   | License                                             | URL                                                      |
|--------------------|-----------|-----------------------------------------------------|----------------------------------------------------------|
| certifi            | 25.1.0 | Mozilla Public License 2.0 (MPL 2.0)                | https://github.com/certifi/python-certifi                |
| charset-normalizer | 3.4.1     | MIT License                                         | https://github.com/Ousret/charset_normalizer             |
| idna               | 3.10      | BSD License                                         | https://github.com/kjd/idna                              |
| pycryptodome       | 3.21.0    | Apache Software License; BSD License; Public Domain | https://www.pycryptodome.org                             |
| requests           | 2.32.3    | Apache Software License                             | https://requests.readthedocs.io                          |
| urllib3            | 2.3.0     | MIT License                                         | https://github.com/urllib3/urllib3/blob/main/CHANGES.rst |
| winregistry        | 2.1.0     | UNKNOWN                                             | https://github.com/shpaker/winregistry                   |
