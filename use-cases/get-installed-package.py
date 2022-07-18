#!/usr/bin/env python3

import salesforce_scripts

(instance, token) = salesforce_scripts.get_instance_and_access_token()
assert salesforce_scripts.list_installed_packages(instance, token)
