#!/usr/bin/env python3

import salesforce_scripts

def test_query_users():
    (instance, token) = salesforce_scripts.get_instance_and_access_token()
    assert salesforce_scripts.query_users(instance, token)
