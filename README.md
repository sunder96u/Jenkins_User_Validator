# Jenkins User Validator

This python script checks if a Jenkins user exists by attempting to log in with a provided username and password. The script berifies whether a user exists in Jenkins by checking the response code from the Jenkins server. It can be useful for validating user access or for auditing Jenkins users.

## Features

- Tested on Jenkins 2.440.3
- Checks if a Jenkins user exists by accessing their user profile via the Jenkins API.
- Returns different outcomes based on the status code:
  - **200**: User exists and authentication is successful.
  - **404**: User does not exist.
  - **403**: User exists but lacks permissions to view their profile.
- Prints results to the console with user information in color.

## Username File

Jenkins only allows alphanumeric characters, slashes, or dashes in the username

## Prerequisites

Before running the script, you will need to have Python installed on your system. Additionally, the script requires the `requests` library to interact with the Jenkins API. You can install the required dependencies using:

```bash
pip install requests
```

## Usage

```
python3 User_check.py --url http://<jenkins_url> --userfile <username file> --password <password>
```


## ToDo

Add ability to use Password list <br>
Add ability to use single user (without a file)


