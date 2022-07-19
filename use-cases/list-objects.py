#!/usr/bin/env python3

import salesforce_scripts

(instance, token) = salesforce_scripts.get_instance_and_access_token()
sobjects = salesforce_scripts.list_objects(instance, token)["sobjects"]
i =0
for obj in sobjects:
    print(obj["name"], "\t", obj["label"])
    i = i+1
    if i == 5:
        print("...")
        break
