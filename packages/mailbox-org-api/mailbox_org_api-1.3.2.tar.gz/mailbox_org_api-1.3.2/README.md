# mailbox-org-api
A library to access the mailbox.org Business API.

## Motivation and purpose 
The goal is to provide a comprehensive library that can easily be used to integrate the business features at mailbox.org.

## Installation
### Using pip:
```bash
pip install mailbox-org-api
```

### Directly from source:
```bash
pip install git+https://github.com/heshsum/mailbox-org-api
```

## Usage
Basic usage is fairly straightforward. The naming scheme of the functions is similar to the naming at mailbox.org,
but instead of points, it uses underscores (e.g. instead of `mail.add` it's `mail_add`).  
Additionally, some helper functions for common or more complicated tasks are included to make life a bit easier, 
e.g. for changing plans, password and to retrieve invoices.  

```python
from mailbox_org_api import APIClient

username = 'foo'
password = 'bar'

# Initializing
api = APIClient.APIClient()

# Testing with hello.world
api.hello_world()

# Creating a new API session
api.auth(username, password)

# Testing the session with hello.innerworld
api.hello_innerworld()

# Changing account settings
api.account_set('foo', {'payment_type':'invoice'})

# Creating an inbox
api.mail_add('foo@bar.com', 's3cr3tp4ssw0rd', 'standard', 'First Name', 'Last Name')

# Here are some examples for helper functions provided by this package

# Changing an inbox password
api.mail_set_password('foo@bar.com', 'an0th3rS3cr3t')

# Changing an inbox plan
api.mail_set_plan('foo@bar.com', 'premium')

# Deactivating an inbox
api.mail_set_state('foo@bar.com', False)

# Changing alias addresses
api.mail_set_aliases('foo@bar.com', ['alias1@bar.com', 'alias2@bar.com'])

# Changing forward addresses
api.mail_set_forwards('foo@bar.com', ['forward1@bar.com', 'forward2@bar.com'])

# Closing the session
api.deauth()
```

## Common tasks
mailbox_org_api includes a number of helper functions to make common tasks simpler. These include:

### mail_set_password
This is a function to send a `mail.set`command and set a user's password.

Usage:
```
api.mail_set_password('user@testmail.tech', 'theNewPassword')
```

### mail_set_password_require_reset
This function sends a `mail.set` command to set a user's password and require the user to change it upon the next login.

Usage:
```python
api.mail_set_password('user@testmail.tech', 'theNewPassword')
```

The function will automatically set `'require_reset':True` when sending the request.

### mail_set_plan
This function sets the plan for an inbox.

Usage:
```python
api.mail_set_plan('user@testmail.tech', 'standard')
```


### mail_set_forwards
This function sets the forwards of an inbox.

Usage:
```python
api.mail_set_forwards('user@testmail.tech', ['forward@testmail.tech', 'forward@testmail.tech'])
```

### mail_set_aliases
This function sets the aliases of an inbox.

Usage:
```python
api.mail_set_forwards('user@testmail.tech', ['alias1@testmail.tech', 'alias2@testmail.tech'])
```

### mail_set_state
With this function an inbox can be (de-)activated. It sends a `mail.set` command with the `active` parameter.

Usage:
```python
# Deactivates an inbox
api.mail_set_state('user@testmail.tech', 'False')

# Activates an inbox
api.mail_set_state('user@testmail.tech', 'True')
```

### account_invoice_get_list
This function makes retrieving a list of all invoices easier.  
It returns a list of all invoice id's for a given account.

Usage:
```python
api.account_invoice_get_list('account_name')
```

### account_invoice_get_token
In order to retrieve an invoice, a token is needed. Tokens change periodically.  
This function helps to get the token for a given invoice ID.

Usage:
```python
api.account_invoice_get_token('BMBO-1234-24')
```

### account_invoice_get_pdf
Invoices are provided as Based64 encoded gz Strings. This function
1. takes the invoice ID
2. retrieves the token for the invoice
3. gets the binary data
4. decodes the Base64
5. decompresses it
6. returns the bytes of the actual PDF

Usage
```python
invoice_id = 'BMBO-1234-24'
account_name = 'some_user'
with open(invoice_id + '.pdf', 'w') as file:
    file.write(api.account_invoice_get_pdf(account_name, invoice_id))
```

## Here be dragons
1. I'm not a programmer. I'm not very good at this. Be aware of my incompetence.
2. Implementation is not complete. Not all functions of the API have been implemented
3. Type hinting is available for most functions, but not all of them.  
E.g. `mail_set()` accepts kwargs due to the number of available attributes. 
In that case type errors will be returned if wrong types are provided.

## API documentation
mailbox.org provides API documentation here: [https://api.mailbox.org](https://api.mailbox.org)
