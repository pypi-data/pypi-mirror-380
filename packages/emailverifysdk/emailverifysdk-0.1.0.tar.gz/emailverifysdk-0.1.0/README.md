## Email Verify Python SDK
This SDK contains methods for interacting easily with Email Verify API.
More information about EmailVerify you can find in the [official webiste](https://www.emailverify.io/).

Official Python SDK for [EmailVerify.io](https://app.emailverify.io) - A comprehensive email verification service.

## Features

- ✅ **Single Email Validation** - Validate individual email addresses
- 💰 **Account Balance Checking** - Monitor your credits and API status
- 📦 **Batch Validation** - Process up to 5,000 emails at once
- 🔍 **Email Finder** - Find email addresses by name and domain

## INSTALLATION
```bash
pip install emailverifysdk
```

## USAGE
Import the sdk in your file:

```python
from emailverifysdk import EmailVerify
```

Initialize the sdk with your api key:

```python
email_verify = EmailVerify("<YOUR_API_KEY>")
```

## Examples
Then you can use any of the SDK methods, for example:

* ##### Check how many credits you have left on your account
```python
from emailverifysdk import EmailVerify, EmailVerifyException

try:
    email_verify = EmailVerify("<YOUR_API_KEY>")
    response = email_verify.check_balance()
    print("Email Verify response: " + str(response))
except EmailVerifyException as e:
    print("EmailVerifyException error: " + str(e))
```

Sample response:
```python
BalanceResponse = {
    'api_status': 'enabled',
    'daily_credits_limit': 0,
    'referral_credits': 0,
    'remaining_credits': 9986
}
```

Note: You can access any value of the response using attribute access, e.g. response.api_status

Sample response for appsumo users:
```python
BalanceResponse = {
    'api_status': 'enabled', 
    'daily_credits_limit': 1000, 
    'remaining_daily_credits': 998, 
    'bonus_credits': 35000
}
```

* ##### Validate an email address
```python
from emailverifysdk import EmailVerify, EmailVerifyException

try:
    email_verify = EmailVerify("<YOUR_API_KEY>")
    response = email_verify.validate("<EMAIL_ADDRESS>") # EMAIL ADDRESS MUST BE STRING
    print("Email Verify response: " + str(response))
except EmailVerifyException as e:
    print("EmailVerifyException error: " + str(e))
```

Sample response:
```python
ValidateResponse = {
    'email': '<EMAIL_ADDRESS>', 
    'status': 'do_not_mail', 
    'sub_status': 'mailbox_quota_exceeded'
}
```

Status can be any of the following:
- valid
- invalid
- catch_all
- do_not_mail
- unknown
- role_based
- skipped

Sub Status can be any of the following:
- permitted
- failed_syntax_check
- mailbox_quota_exceeded
- mailbox_not_found
- no_dns_entries
- disposable
- none
- opt_out
- blocked_domain    


* ##### Batch Validation
```python
from emailverifysdk import EmailVerify, EmailVerifyException

try:
    email_verify = EmailVerify("<YOUR_API_KEY>")
    emails = ['email1@example.com', 'email2@example.com', 'email3@example.com']
    response = email_verify.validate_batch(emails, "<TITLE>") # title and emails are required fields
    print("Email Verify response: " + str(response))
except EmailVerifyException as e:
    print("EmailVerifyException error: " + str(e))
```

Sample response:
```python
BatchValidateResponse= {
    'status': 'queued', 
    'task_id': 2922, 
    'count_submitted': 5, 
    'count_duplicates_removed': 0, 
    'count_rejected_emails': 1, 
    'count_processing': 4
}
```

* ##### Get Batch Validation Result
```python
from emailverifysdk import EmailVerify, EmailVerifyException

task_id = 1 #TASK_ID must be your task_id received in bulk validation api

try:
    email_verify = EmailVerify("<YOUR_API_KEY>")
    response = email_verify.get_batch_result(task_id) 
    print("Email Verify response: " + str(response))
except EmailVerifyException as e:
    print("EmailVerifyException error: " + str(e))
```

Sample response when task stil under verification:
```python
BatchResultResponse = {
    'count_checked': 0, 
    'count_total': 4, 
    'name': 'Title', 
    'progress_percentage': 0.0, 
    'task_id': 2922, 
    'status': 'queued',
    'results': None
}
```

Sample response when verification completed
```python
BatchResultResponse = {
    'count_checked': 4, 
    'count_total': 4, 
    'name': 'Title', 
    'progress_percentage': 100, 
    'task_id': 2922, 
    'status': 'verified', 
    'results': {
        'email_batch': [
            {
                'address': 'email1@example.com', 
                'status': 'do_not_mail', 
                'sub_status': 'mailbox_quota_exceeded'
            }, 
            {   
                'address': 'email2@example.com', 
                'status': 'do_not_mail',
                'sub_status': 'mailbox_quota_exceeded'
            }, 
            {   
                'address': 'email3@example.com', 
                'status': 'do_not_mail', 
                'sub_status': 'mailbox_quota_exceeded'}, 
        ]
    }
}
```

* ##### Email Finder
```python
from emailverifysdk import EmailVerify, EmailVerifyException

try:
    email_verify = EmailVerify("<YOUR_API_KEY>")
    response = email_verify.find_email('<NAME>', '<DOMAIN.COM>')
    print("Email Verify response: " + str(response))
except EmailVerifyException as e:
    print("EmailVerifyException error: " + str(e))
```

Sample response when email found:
```python
FinderResponse = {
    'email': 'email1@example.com', 
    'status': 'found'
}
```

Sample response when email not found:
```python
FinderResponse = {
    'email': 'null', 
    'status': 'not_found'
}
```
## Exception Handling
The EmailVerify SDK raises custom exceptions for API errors, invalid input, and network issues. You should always wrap SDK calls in a try/except block to handle these cases gracefully.

### Common Exceptions
- `EmailVerifyAPIException`: Raised for API errors (invalid key, disable key, insufficient credits, invalid paramets etc.)
- `EmailVerifyClientException`: Raised for client-side errors (missing parameters, invalid input)
- `EmailVerifyNetworkException`: Raised for network connection errors
- `EmailVerifyTimeoutException`: Raised when a request times out

### Example Usage
```python
from emailverifysdk import EmailVerify, EmailVerifyAPIException, EmailVerifyClientException

email_verify = EmailVerify("<YOUR_API_KEY>")
try:
    response = email_verify.validate("test@example.com")
    print("Validation result:", response.status)
except EmailVerifyAPIException as api_err:
    print("API error:", api_err)
except EmailVerifyClientException as client_err:
    print("Client error:", client_err)
except Exception as e:
    print("Unexpected error:", e)
```

### Accessing Error Details
If an EmailVerifyAPIException is raised, you can access additional details:
```python
from emailverifysdk import EmailVerify, EmailVerifyAPIException

email_verify = EmailVerify("<YOUR_API_KEY>")
try:
    response = email_verify.validate("email@example.com")
except EmailVerifyAPIException as e:
    print("Message", str(e))
    print("Status code:", e.status_code)
    print("Response data:", e.response_data)
```


## Context Manager Usage

```python
from emailverifysdk import EmailVerify

email_verify = EmailVerify("<YOUR_API_KEY>")

with EmailVerify("<YOUR_API_KEY>") as email_verify:
    response = email_verify.validate("test@example.com")
    print(str(response))
```