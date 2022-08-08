#!/usr/bin/env python3

import json
import requests

requests.packages.urllib3.disable_warnings()

def get_token(base_path, user, passwd):
    url = f"{base_path}/dna/system/api/v1/auth/token"
    auth = (user, passwd)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, auth=auth, verify=False)
    response.raise_for_status()
    Token = json.loads(response.text)["Token"]
    return Token