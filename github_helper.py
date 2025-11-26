import os
import jwt
import time
import requests
from dotenv import load_dotenv

load_dotenv()

def get_installation_access_token(installation_id):
    # Read the private key file directly
    try:
        with open("private_key.pem", "r") as f:
            private_key = f.read()
    except FileNotFoundError:
        print("❌ Error: private_key.pem not found in folder!")
        return None

    app_id = os.getenv("GITHUB_APP_ID")
    
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + 600,
        "iss": app_id
    }
    encoded_jwt = jwt.encode(payload, private_key, algorithm="RS256")

    # Exchange JWT for Access Token
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
    headers = {
        "Authorization": f"Bearer {encoded_jwt}",
        "Accept": "application/vnd.github+json"
    }
    response = requests.post(url, headers=headers)
    
    if response.status_code != 201:
        print(f"❌ GitHub Auth Failed: {response.text}")
        return None
        
    return response.json()["token"]

def post_comment(owner, repo, pr_number, token, message):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    resp = requests.post(url, headers=headers, json={"body": message})
    if resp.status_code == 201:
        print("✅ Comment posted successfully!")
    else:
        print(f"❌ Failed to post comment: {resp.text}")