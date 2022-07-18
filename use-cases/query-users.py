#!/usr/bin/env python3

import salesforce_scripts
import json

(instance, token) = salesforce_scripts.get_instance_and_access_token()
print(json.dumps(salesforce_scripts.query_users(instance, token), indent=4))
