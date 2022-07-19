#!/usr/bin/env python3

import salesforce_scripts
import json

(instance, token) = salesforce_scripts.get_instance_and_access_token()
custom_object = salesforce_scripts.describe_object(instance, token, "Account")
for field in custom_object["fields"]:
    print("%s\t|\t%s\t|\t%s" % (field['fullName'], field['label'], field['type']))
